import json
import logging
import urllib.parse
import urllib.request

import wobblywalrus.cache_manager

cache = wobblywalrus.cache_manager.CacheManager()
logger = logging.getLogger(__name__)


def get_place_id_by_coordinates_and_name(
    latitude,
    longitude,
    business_name,
    api_key,
    cache_stats,
    uuid=None,
    radius_meters=100,
    skip_cache=False,
):
    # Check cache first
    cache_key = f"{latitude},{longitude},{business_name}"
    if not skip_cache:
        cached_place_id = cache.get_cached_place_id(cache_key)
        if cached_place_id:
            logger.debug(f"Cache hit for {business_name}")
            cache_stats.add_hit()
            return cached_place_id

    logger.debug(f"Cache miss for {business_name}")
    cache_stats.add_miss()

    # Use Places API Nearby Search
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{latitude},{longitude}",
        "radius": radius_meters,
        "keyword": business_name,
        "key": api_key,
    }

    # Construct URL with parameters
    query_string = urllib.parse.urlencode(params)
    url = f"{base_url}?{query_string}"

    logger.debug(f"Making API request for {business_name}")
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                result = json.loads(response.read().decode())
                if result.get("results"):
                    # Get the first result
                    place_id = result["results"][0]["place_id"]
                    # Cache the result if caching is enabled
                    if not skip_cache:
                        cache.cache_place_id(cache_key, place_id, uuid)
                        logger.debug(
                            f"Cached new place_id for {business_name} with UUID {uuid}"
                        )
                    return place_id
                else:
                    logger.debug(f"No results found for {business_name}")
            else:
                logger.debug(f"API request failed with status {response.status}")
    except urllib.error.URLError as e:
        logger.debug(f"API request failed: {str(e)}")
    return None


def get_maps_url(place_id, use_search=False):
    if use_search:
        return f"https://google.com/maps/search/?api=1&query=&query_place_id={place_id}"
    return f"https://www.google.com/maps/place?q=place_id:{place_id}"


def get_detailed_maps_url(business_name, latitude, longitude, zoom=17):
    encoded_name = urllib.parse.quote(business_name)
    return f"https://www.google.com/maps/place/{encoded_name}/@{latitude},{longitude},{zoom}z"
