from src.constants import AppConstants


class OracleAssetService(object):

    @staticmethod
    def get_now_available():
        return [
            {
                'symbol': _symbol,
                'symbol_name': AppConstants.MAPPING_SYMBOL_NAMES[_symbol]
            }
            for _symbol in AppConstants.AVAILABLE_SYMBOLS
        ]
