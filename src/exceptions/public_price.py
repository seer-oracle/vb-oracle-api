# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from lib.decorators.http import make_response
from lib.enums.http import StatusInt
from src.enums.http import ErrorCode


class ExPublicPrice(Exception):
    def __init__(self, message='Oracle_get_price_not_valid', *args: object) -> None:
        super().__init__(*args)
        self.response = make_response(
            error_code=ErrorCode.ErrorOraclePrice,
            msg=message
        ), StatusInt.Bad

    pass
