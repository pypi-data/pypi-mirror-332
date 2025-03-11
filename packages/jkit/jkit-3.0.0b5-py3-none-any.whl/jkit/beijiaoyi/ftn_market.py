from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import Literal

from jkit._base import DataObject, ResourceObject
from jkit._network import send_request
from jkit._normalization import normalize_datetime
from jkit.constraints import (
    NonEmptyStr,
    NonNegativeInt,
    NormalizedDatetime,
    PositiveFloat,
    PositiveInt,
)
from jkit.credentials import BeijiaoyiCredential

AVATAR_URL_PREFIX = "https://testapi.beijiaoyi.com/"

OrderSupportedPaymentChannelsType = Literal["WECHAT_PAY", "ALIPAY"]


class _PublisherInfoField(DataObject, frozen=True):
    id: PositiveInt
    name: NonEmptyStr

    avatar_url: NonEmptyStr


class OrderData(DataObject, frozen=True):
    id: PositiveInt

    price: PositiveFloat
    total_amount: PositiveInt
    traded_amount: NonNegativeInt
    remaining_amount: NonNegativeInt
    minimum_trade_amount: PositiveInt
    maximum_trade_amount: PositiveInt | None

    completed_trades_count: NonNegativeInt
    publish_time: NormalizedDatetime
    supported_payment_channels: tuple[OrderSupportedPaymentChannelsType, ...]

    publisher_info: _PublisherInfoField


class FtnMarket(ResourceObject):
    def __init__(self, *, credential: BeijiaoyiCredential) -> None:
        self._credential = credential

    async def iter_orders(
        self, *, type: Literal["BUY", "SELL"], start_page: int = 1
    ) -> AsyncGenerator[OrderData, None]:
        current_page = start_page

        while True:
            data = await send_request(
                datasource="BEIJIAOYI",
                method="POST",
                path="/jsb_product/GetBuyProductList"
                if type == "BUY"
                else "/jsb_product/GetSellProductList",
                body={"page": current_page, "rows": 20},
                credential=self._credential,
                response_type="JSON",
            )

            if not data["data"]:
                return

            for item in data["data"]:
                if item["isWeXin"] and item["isZfb"]:
                    supported_payment_channels = ("WECHAT_PAY", "ALIPAY")
                elif item["isWeXin"] and not item["isZfb"]:
                    supported_payment_channels = ("WECHAT_PAY",)
                elif not item["isWeXin"] and item["isZfb"]:
                    supported_payment_channels = ("ALIPAY",)
                else:
                    supported_payment_channels = ()

                yield OrderData(
                    id=int(item["productId"]),
                    price=item["unitPrice"],
                    total_amount=int(item["totalQty"]),
                    traded_amount=int(item["totalQty"] - item["availableQty"]),
                    remaining_amount=int(item["availableQty"]),
                    minimum_trade_amount=item["Limit"],
                    maximum_trade_amount=item["MaxLimit"],
                    completed_trades_count=item["tradeQty"],
                    publish_time=normalize_datetime(item["CreateDate"]),
                    supported_payment_channels=supported_payment_channels,
                    publisher_info=_PublisherInfoField(
                        id=item["userId"],
                        name=item["userName"],
                        avatar_url=AVATAR_URL_PREFIX + item["userImage"],
                    ),
                )._validate()

            current_page += 1
