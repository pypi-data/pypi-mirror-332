import argparse
import logging
import os
import sys
import dotenv
import wobblywalrus.config
import wobblywalrus.utils
logger = logging.getLogger(__name__)

def places_command(args, api_key):
    import wobblywalrus.yaml_to_place_id
    cache_stats = wobblywalrus.utils.CacheStats()
    for file_path in args.files:
        if not os.path.exists(file_path):
            logger.error(f"File not found - {file_path}")
            continue
        wobblywalrus.yaml_to_place_id.process_yaml_file(
            file_path, api_key, cache_stats, skip_cache=args.no_cache
        )
    logger.debug(cache_stats.summary())
    logger.debug(f"Using cache directory: {wobblywalrus.config.CACHE_DIR}")

def search_command(args, api_key):
    import wobblywalrus.search
    search_engine_id = os.getenv("GOOGLE_CUSTOM_SEARCH_ENGINE_ID")
    if not search_engine_id:
        logger.error("GOOGLE_CUSTOM_SEARCH_ENGINE_ID environment variable not set")
        sys.exit(1)
    cache_stats = wobblywalrus.utils.CacheStats()
    for file_path in args.files:
        if not os.path.exists(file_path):
            logger.error(f"File not found - {file_path}")
            continue
        file_stats = wobblywalrus.search.process_search(
            file_path,
            api_key,
            search_engine_id,
            strategy_type=args.search_type,
            skip_cache=args.no_cache,
            debug_json=args.debug_json,
        )
        if file_stats:
            cache_stats.hits += file_stats.hits
            cache_stats.misses += file_stats.misses
    logger.debug(cache_stats.summary())
    logger.debug(f"Using cache directory: {wobblywalrus.config.CACHE_DIR}")

def main():
    parser = argparse.ArgumentParser(description="Google Places API utilities")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (can be used multiple times)",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Places command
    places_parser = subparsers.add_parser(
        "places", help="Process YAML files to fetch Google Place IDs"
    )
    places_parser.add_argument("files", nargs="+", help="YAML file paths to process")
    places_parser.add_argument(
        "--no-cache", action="store_true", help="Skip cache lookups"
    )

    # Search command
    search_parser = subparsers.add_parser(
        "search", help="Search for business information using Google Custom Search"
    )
    search_parser.add_argument("files", nargs="+", help="YAML file paths to process")
    search_parser.add_argument(
        "--no-cache", action="store_true", help="Skip cache lookups"
    )
    search_parser.add_argument(
        "--search-type",
        choices=["yelp", "business_name", "address"],
        default="yelp",
        help="Type of search strategy to use",
    )
    search_parser.add_argument(
        "--debug-json",
        action="store_true",
        help="Display raw JSON response from Google Custom Search API",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    wobblywalrus.utils.configure_logging(args.verbose)

    dotenv.load_dotenv()
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        logger.error("GOOGLE_MAPS_API_KEY environment variable not set in .env file")
        sys.exit(1)

    if args.command == "places":
        places_command(args, api_key)
    elif args.command == "search":
        search_command(args, api_key)

if __name__ == "__main__":
    main()
