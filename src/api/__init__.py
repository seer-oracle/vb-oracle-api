from .public_price import rest_public_price
from .root import rest_root
from .asset import rest_asset

DEFAULT_BLUEPRINTS = [
    rest_root,
    rest_public_price,
    rest_asset
]
