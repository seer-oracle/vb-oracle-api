
from datetime import datetime as dt
from datetime import timezone
from src.extensions import redis_cluster
from src.constants import AppConstants
from src.exceptions.public_price import ExPublicPrice


class OraclePublicPriceService(object):

    @staticmethod
    def utc_timestamp_now():
        """ * Get time now in UTC by timestamp * """
        return dt.utcnow().replace(tzinfo=timezone.utc).timestamp()

    @classmethod
    def get_latest_value_was_stored(cls, key):
        """
            Function: Get latest key available
            @return: latest timestamp have
        """
        print(f"** Get latest {key} :")
        _list = redis_cluster.keys(pattern=key)
        if not len(_list):
            return None
        _max = _list[0]
        for _item in _list:
            if int(_item.split("_")[2]) > int(_item.split("_")[2]):
                _max = _item
        return redis_cluster.get(name=_max)

    @staticmethod
    def gen_redis_stored_key_for_pair(symbol_pair):
        return f"Oracle:calculated_price:{symbol_pair}_*"

    @classmethod
    def get_latest_public_price_feed(cls):
        _feed = []
        for _pair in AppConstants.AVAILABLE_SYMBOL_PAIR:
            _latest = cls.get_latest_value_was_stored(key=cls.gen_redis_stored_key_for_pair(_pair))
            _feed.append(_latest)
        return dict(zip(AppConstants.AVAILABLE_SYMBOL_PAIR, _feed))

    @classmethod
    def get_latest_public_price_by_symbol_pair(cls, symbol_pair):
        if symbol_pair not in AppConstants.AVAILABLE_SYMBOL_PAIR:
            raise ExPublicPrice("Invalid symbol pair")
        return {
            "price": cls.get_latest_value_was_stored(key=cls.gen_redis_stored_key_for_pair(symbol_pair))
        }

    @classmethod
    def get_price_by_symbol(cls, symbol):
        if symbol not in AppConstants.AVAILABLE_SYMBOLS:
            raise ExPublicPrice("Invalid symbol")
        _list_price = []
        for _pair in AppConstants.AVAILABLE_SYMBOL_PAIR:
            if symbol in _pair:
                _list_price.append(
                    {
                        _pair: cls.get_latest_value_was_stored(key=cls.gen_redis_stored_key_for_pair(_pair))
                    }
                )
        return _list_price
