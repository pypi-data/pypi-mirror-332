import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class SearchStrategy(ABC):
    def __init__(self, api_key: str, search_engine_id: str):
        self.api_key = api_key
        self.search_engine_id = search_engine_id

    @abstractmethod
    def build_search_query(self, business_data: dict) -> dict:
        """Build search parameters for the strategy"""
        pass


class YelpSearchStrategy(SearchStrategy):
    def build_search_query(self, business_data: dict) -> dict:
        return {
            "key": self.api_key,
            "cx": self.search_engine_id,
            "q": f"{business_data['name']} site:yelp.com",
            "num": 5,
        }


class BusinessNameSearchStrategy(SearchStrategy):
    def build_search_query(self, business_data: dict) -> dict:
        return {
            "key": self.api_key,
            "cx": self.search_engine_id,
            "q": business_data["name"],
            "num": 5,
        }


class AddressSearchStrategy(SearchStrategy):
    def build_search_query(self, business_data: dict) -> dict:
        name = business_data["name"]
        addr = business_data.get("address", "")
        city = business_data.get("city", "")
        query = f"{name} {addr} {city}"
        return {
            "key": self.api_key,
            "cx": self.search_engine_id,
            "q": query.strip(),
            "num": 5,
        }


class SearchStrategyFactory:
    _strategies = {
        "yelp": YelpSearchStrategy,
        "business_name": BusinessNameSearchStrategy,
        "address": AddressSearchStrategy,
    }

    @classmethod
    def create_strategy(
        cls, strategy_type: str, api_key: str, search_engine_id: str
    ) -> SearchStrategy:
        strategy_class = cls._strategies.get(strategy_type)
        if not strategy_class:
            available = list(cls._strategies.keys())
            raise ValueError(
                f"Unknown strategy type: {strategy_type}. Available types: {available}"
            )
        return strategy_class(api_key, search_engine_id)
