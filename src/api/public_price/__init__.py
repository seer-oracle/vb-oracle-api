
from flask import Blueprint
from .controller import *

rest_public_price = Blueprint('rest_public_price', __name__, url_prefix='price')

rest_public_price.add_url_rule('/<symbol_pair>/latest',
                               methods=['GET'],
                               view_func=get_latest_public_price_by_symbol_pair)

rest_public_price.add_url_rule('latest', methods=['GET'], view_func=get_latest_price_feed)

rest_public_price.add_url_rule('symbol/<symbol>', methods=['GET'], view_func=get_price_by_symbol)