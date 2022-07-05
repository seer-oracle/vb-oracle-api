
from flask import Blueprint
from .controller import *

rest_asset = Blueprint('rest_asset', __name__, url_prefix='asset')

rest_asset.add_url_rule('now_available', methods=['GET'], view_func=get_now_available_assets)