import datetime
import json
import logging

import wobblywalrus.config

logger = logging.getLogger(__name__)

CACHE_TTL = datetime.timedelta(days=2)


class SearchCache:
    def __init__(self, cache_file=wobblywalrus.config.SEARCH_CACHE_FILE):
        self.cache_file = cache_file
        logger.debug(f"Initializing search cache at: {self.cache_file}")
        self.cache = self._load_cache()

    def _load_cache(self):
        try:
            if self.cache_file.exists():
                with self.cache_file.open("r") as f:
                    data = json.load(f)
                    logger.debug(f"Loaded {len(data)} entries from cache")
                    return data
            logger.debug("No existing cache file found")
            return {}
        except json.JSONDecodeError:
            logger.warning(f"Error reading cache file {self.cache_file}")
            return {}

    def _save_cache(self):
        # Create directory if it doesn't exist
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with self.cache_file.open("w") as f:
            json.dump(self.cache, f, indent=2)
            logger.debug(f"Saved {len(self.cache)} entries to cache")

    def get(self, key):
        if key not in self.cache:
            return None

        entry = self.cache[key]
        entry_datetime = datetime.datetime.fromtimestamp(entry["timestamp"])
        if datetime.datetime.now() - entry_datetime > CACHE_TTL:
            del self.cache[key]
            self._save_cache()
            return None

        return entry["data"]

    def set(self, key, data):
        self.cache[key] = {
            "timestamp": datetime.datetime.now().timestamp(),
            "data": data,
        }
        self._save_cache()
