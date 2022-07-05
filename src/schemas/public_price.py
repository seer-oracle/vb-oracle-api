# -*- coding: utf-8 -*-

""""
    Copyright (C) 2022 ESOL LABS - All Rights Reserved.

    You may use, distribute and modify this code under the
    terms of the XYZ license, which unfortunately won't be
    written for another century.

    You should have received a copy of the XYZ license with
    this file. If not, please write to: , or visit :
"""

# File: __init__.py
# Created at June 29th, 2022
# Author: taipa

"""
   Description:
        -
        -
"""

from marshmallow import EXCLUDE, fields, Schema

"""
    Public Price by Symbol
"""


class PublicPriceBySymbol(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    price = fields.Str(allow_none=True, missing={})


"""
    Public Price Feed
"""


class PublicPriceFeed(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    feed = fields.Dict(allow_none=True, missing={})
