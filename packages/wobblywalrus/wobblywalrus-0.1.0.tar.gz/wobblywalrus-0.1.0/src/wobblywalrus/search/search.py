import hashlib
import json
import logging
import urllib.parse
import urllib.request
import yaml
import wobblywalrus.search_cache
import wobblywalrus.utils
from wobblywalrus.search.strategies import SearchStrategyFactory

logger = logging.getLogger(__name__)
cache = wobblywalrus.search_cache.SearchCache()

def make_cache_key(params):
    """Create deterministic cache key from search parameters"""
    param_str = urllib.parse.urlencode(sorted(params.items()))
    return hashlib.sha256(param_str.encode()).hexdigest()

class SearchService:
    def __init__(self, api_key: str, search_engine_id: str, strategy_type: str):
        self.strategy = SearchStrategyFactory.create_strategy(
            strategy_type, api_key, search_engine_id
        )

    def get_search_results(self, business_data: dict, skip_cache=False):
        params = self.strategy.build_search_query(business_data)
        if not skip_cache:
            cache_key = make_cache_key(params)
            cached_result = cache.get(cache_key)
            if cached_result:
                return cached_result, True  # Cache hit

        base_url = "https://www.googleapis.com/customsearch/v1"
        query_string = urllib.parse.urlencode(params)
        url = f"{base_url}?{query_string}"
        logger.trace("Making Custom Search API request:")
        logger.trace(f"URL: {url}")
        logger.trace(f"Parameters: {params}")

        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    if not skip_cache:
                        cache_key = make_cache_key(params)
                        cache.set(cache_key, data)
                    return data, False  # Cache miss
                else:
                    logger.error(
                        f"Search API request failed with status {response.status}"
                    )
                    return None, False
        except urllib.error.HTTPError as e:
            logger.error(f"Search API request failed: {str(e)}")
            return None, False
        except urllib.error.URLError as e:
            logger.error(f"Search API request failed: {str(e)}")
            return None, False

def parse_search_results(results):
    if not results or "items" not in results:
        return []

    parsed_results = []
    for item in results["items"]:
        parsed_result = {
            "title": item.get("title", ""),
            "snippet": item.get("snippet", ""),
            "url": item.get("link", ""),
            "date": item.get("pagemap", {})
            .get("metatags", [{}])[0]
            .get("article:published_time", ""),
            "thumbnails": [
                img.get("src", "")
                for img in item.get("pagemap", {}).get("cse_thumbnail", [])
            ],
            "metadata": item.get("pagemap", {}).get("metatags", [{}])[0],
        }
        if "rating" in item.get("pagemap", {}).get("aggregaterating", [{}])[0]:
            parsed_result["rating"] = item["pagemap"]["aggregaterating"][0]["rating"]
        parsed_results.append(parsed_result)

    return parsed_results

def process_search(
    file_path, api_key, search_engine_id, strategy_type="yelp", skip_cache=False, debug_json=False
):
    logger.debug(f"Processing search for file: {file_path}")
    cache_stats = wobblywalrus.utils.CacheStats()

    with open(file_path, "r") as f:
        business_data = yaml.safe_load(f)

    if not business_data.get("name"):
        logger.error(f"Missing business name in {file_path}")
        return

    search_service = SearchService(api_key, search_engine_id, strategy_type)
    results, is_cached = search_service.get_search_results(business_data, skip_cache)

    if not results:
        logger.error(f"No search results found for {business_data['name']}")
        return

    if is_cached:
        cache_stats.add_hit()
    else:
        cache_stats.add_miss()

    # Display raw JSON if debug_json flag is set
    if debug_json:
        logger.info(f"\nRaw JSON response for {business_data['name']}:")
        logger.info(json.dumps(results, indent=2))

    parsed_results = parse_search_results(results)
    uuid_str = business_data.get("uuid", "N/A")
    logger.info(f"\nSearch results for {business_data['name']} (UUID: {uuid_str}):")

    for idx, result in enumerate(parsed_results, 1):
        logger.info(f"\n--- Result {idx} ---")
        logger.info(f"UUID: {uuid_str}")
        logger.info(f"Title: {result['title']}")
        logger.info(f"Description: {result['snippet']}")
        logger.info(f"URL: {result['url']}")
        logger.info(f"Date: {result['date']}")
        if result.get("rating"):
            logger.info(f"Rating: {result['rating']}")
        if result["thumbnails"]:
            logger.info("Thumbnails:")
            for thumb in result["thumbnails"]:
                logger.info(f"- {thumb}")

    return cache_stats
