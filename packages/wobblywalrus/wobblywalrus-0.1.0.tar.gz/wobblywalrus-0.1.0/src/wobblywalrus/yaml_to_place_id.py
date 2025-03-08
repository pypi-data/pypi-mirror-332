import argparse
import logging
import os
import sys

import dotenv
import yaml

import wobblywalrus
import wobblywalrus.get_place_id
import wobblywalrus.utils

# Add custom TRACE level
TRACE_LEVEL = 5  # Lower than DEBUG (10)
logging.addLevelName(TRACE_LEVEL, "TRACE")


def trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE_LEVEL):
        self._log(TRACE_LEVEL, message, args, **kwargs)


logging.Logger.trace = trace

# Configure logging levels
LOGGING_LEVELS = {
    0: logging.WARNING,  # Default
    1: logging.INFO,  # -v
    2: logging.DEBUG,  # -vv
    3: TRACE_LEVEL,  # -vvv
}


def configure_logging(verbosity):
    # Cap verbosity to max level
    verbosity = min(verbosity, max(LOGGING_LEVELS.keys()))
    # Set log level based on verbosity
    level = LOGGING_LEVELS.get(verbosity, logging.WARNING)
    # Configure logging
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=level)


def load_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def save_yaml(file_path, data):
    with open(file_path, "w") as f:
        yaml.dump(data, f, sort_keys=False)


def process_yaml_file(file_path, api_key, cache_stats, skip_cache=False):
    logger = logging.getLogger(__name__)
    logger.debug(f"Processing file: {file_path}")
    data = load_yaml(file_path)

    # Extract required fields
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    name = data.get("name", "")
    uuid = data.get("uuid")

    if not (latitude and longitude and name):
        logger.warning(f"Missing coordinates or business name in {file_path}")
        return

    logger.debug(f"Looking up place ID for {name} at ({latitude}, {longitude})")

    # Get place ID using both coordinates and business name
    place_id = wobblywalrus.get_place_id.get_place_id_by_coordinates_and_name(
        latitude,
        longitude,
        name,
        api_key,
        cache_stats,
        uuid=uuid,
        skip_cache=skip_cache,
    )

    if place_id:
        logger.info(f"Processed: {file_path}")
        logger.info(f"Business: {name}")
        logger.info(f"UUID: {uuid}")
        logger.info(f"Coordinates: ({latitude}, {longitude})")
        logger.info(f"Place ID: {place_id}")
        logger.info(f"Maps URL: {wobblywalrus.get_place_id.get_maps_url(place_id)}")

        # Update the source YAML with the place_id if it changed
        if data.get("google_place_id") != place_id:
            data["google_place_id"] = place_id
            save_yaml(file_path, data)
            logger.debug(f"Updated {file_path} with place_id: {place_id}")
    else:
        logger.error(f"Failed to get place ID for {name} at {file_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Process YAML files to fetch Google Place IDs"
    )
    parser.add_argument("files", nargs="+", help="YAML file paths to process")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (can be used multiple times)",
    )
    args = parser.parse_args()

    # Configure logging based on verbosity
    configure_logging(args.verbose)
    logger = logging.getLogger(__name__)

    # Load environment variables
    dotenv.load_dotenv()
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        logger.error("GOOGLE_MAPS_API_KEY environment variable not set")
        sys.exit(1)

    cache_stats = wobblywalrus.utils.CacheStats()

    # Process each file
    for file_path in args.files:
        if not os.path.exists(file_path):
            logger.error(f"File not found - {file_path}")
            continue
        process_yaml_file(file_path, api_key, cache_stats)

    # Print cache statistics
    logger.debug(cache_stats.summary())


if __name__ == "__main__":
    main()
