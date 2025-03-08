import logging

# Add custom TRACE level
TRACE_LEVEL = 5
logging.addLevelName(TRACE_LEVEL, "TRACE")


def trace(self, message, *args, **kwargs):
    if self.isEnabledFor(TRACE_LEVEL):
        self._log(TRACE_LEVEL, message, args, **kwargs)


logging.Logger.trace = trace

LOGGING_LEVELS = {
    0: logging.WARNING,
    1: logging.INFO,
    2: logging.DEBUG,
    3: TRACE_LEVEL,
}


def configure_logging(verbosity):
    verbosity = min(verbosity, max(LOGGING_LEVELS.keys()))
    level = LOGGING_LEVELS.get(verbosity, logging.WARNING)
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=level)


class CacheStats:
    def __init__(self):
        self.hits = 0
        self.misses = 0

    def add_hit(self):
        self.hits += 1

    def add_miss(self):
        self.misses += 1

    def summary(self):
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return f"Cache stats: {self.hits} hits, {self.misses} misses ({hit_rate:.1f}% hit rate)"  # noqa: E501
