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
from src.services.asset import OracleAssetService


@lib.handle_res(login=False)
def get_now_available_assets( *args, **kwargs):
    _res = OracleAssetService.get_now_available()
    return {
                'list_asset': _res
           } or {}
