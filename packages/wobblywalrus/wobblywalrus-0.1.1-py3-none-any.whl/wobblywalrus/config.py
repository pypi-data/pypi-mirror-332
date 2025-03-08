import logging
import pathlib

import platformdirs

logger = logging.getLogger(__name__)

dirs = platformdirs.PlatformDirs("wobblywalrus")
CACHE_DIR = pathlib.Path(dirs.user_cache_dir)
PLACE_ID_CACHE_FILE = CACHE_DIR / "place_id_cache.json"
SEARCH_CACHE_FILE = CACHE_DIR / "search_cache.json"
