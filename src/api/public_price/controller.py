# -*- coding: utf-8 -*-

""""
    Copyright (C) 2022 ESOLLABS - All Rights Reserved.

    You may use, distribute and modify this code under the
    terms of the XYZ license, which unfortunately won't be
    written for another century.

    You should have received a copy of the XYZ license with
    this file. If not, please write to: , or visit :
"""

# File: controller.py
# Created at May 17th, 2022
# Author: taipa

"""
   Description:
        -
        -
"""
import lib
from lib.logger import Logger
from src.services.public_price import OraclePublicPriceService
from src.schemas.public_price import *


@lib.handle_res(res_schema=PublicPriceBySymbol, login=False)
def get_latest_public_price_by_symbol_pair(symbol_pair, *args, **kwargs):
    _res = OraclePublicPriceService.get_latest_public_price_by_symbol_pair(symbol_pair)
    return _res or {}


@lib.handle_res(res_schema=PublicPriceFeed, login=False)
def get_latest_price_feed(*args, **kwargs):
    _feed_res = OraclePublicPriceService.get_latest_public_price_feed()
    return {
        "feed": _feed_res
    } or {}


@lib.handle_res(login=False)
def get_price_by_symbol(symbol, *args, **kwargs):
    _price = OraclePublicPriceService.get_price_by_symbol(symbol)
    return {
                'list_price': _price
           } or {}
