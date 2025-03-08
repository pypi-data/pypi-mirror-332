import datetime
import json
import logging
import os

import wobblywalrus.config

logger = logging.getLogger(__name__)
CACHE_TTL = datetime.timedelta(days=2)


class CacheManager:
    def __init__(self, cache_file=wobblywalrus.config.PLACE_ID_CACHE_FILE):
        self.cache_file = cache_file
        logger.debug(f"Initializing place ID cache at: {self.cache_file}")
        self.cache = self._load_cache()

    def _load_cache(self):
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, "r") as f:
                    cache_data = json.load(f)
                    logger.debug(f"Loaded {len(cache_data)} entries from cache")
                    return cache_data
            logger.debug("No existing cache file found")
            return {}
        except json.JSONDecodeError:
            logger.warning(f"Error reading cache file {self.cache_file}")
            return {}

    def _save_cache(self):
        # Create directory if it doesn't exist
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cache_file, "w") as f:
            json.dump(self.cache, f, indent=2)
            logger.debug(f"Saved {len(self.cache)} entries to cache")

    def get_cached_place_id(self, cache_key):
        cache_entry = self.cache.get(cache_key)
        if cache_entry is None:
            return None
        # Handle both old (string) and new (dict) formats
        if isinstance(cache_entry, str):
            return cache_entry
        return cache_entry.get("place_id")

    def get_cached_uuid(self, cache_key):
        cache_entry = self.cache.get(cache_key)
        if cache_entry is None or isinstance(cache_entry, str):
            return None
        return cache_entry.get("uuid")

    def cache_place_id(self, cache_key, place_id, uuid=None):
        if place_id:
            self.cache[cache_key] = {
                "place_id": place_id,
                "uuid": uuid,
                "timestamp": datetime.datetime.now().timestamp(),
            }
            self._save_cache()
