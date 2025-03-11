from __future__ import annotations

from collections.abc import AsyncGenerator
from datetime import date, datetime, timedelta
from typing import TYPE_CHECKING

from jkit._base import DataObject, ResourceObject
from jkit._network import send_request
from jkit._normalization import normalize_assets_amount
from jkit.constraints import (
    ArticleSlug,
    NonEmptyStr,
    PositiveFloat,
    PositiveInt,
    UserName,
    UserUploadedUrl,
)
from jkit.exceptions import APIUnsupportedError, ResourceUnavailableError

if TYPE_CHECKING:
    from jkit.article import Article


class SummaryData(DataObject, frozen=True):
    fp_to_author_amount_sum: PositiveFloat
    fp_to_voter_amount_sum: PositiveFloat
    total_fp_amount_sum: PositiveFloat


class _AuthorInfoField(DataObject, frozen=True):
    name: UserName | None
    avatar_url: UserUploadedUrl | None


class RecordData(DataObject, frozen=True):
    ranking: PositiveInt
    slug: ArticleSlug | None
    title: NonEmptyStr | None
    fp_to_author_amount: PositiveFloat
    fp_to_voter_amount: PositiveFloat
    total_fp_amount: PositiveFloat
    author_info: _AuthorInfoField

    def to_article_obj(self) -> Article:
        if not self.slug:
            raise ResourceUnavailableError("文章已被删除 / 私密 / 锁定")

        from jkit.article import Article

        return Article.from_slug(self.slug)


class ArticleEarningRanking(ResourceObject):
    def __init__(self, *, date_: date | None = None) -> None:
        if not date_:
            date_ = datetime.now().date() - timedelta(days=1)

        if date_ < date(2020, 6, 20):
            raise APIUnsupportedError("受 API 限制，无法获取 2020.06.20 前的排行榜数据")
        if date_ >= datetime.now().date():
            raise ResourceUnavailableError("无法获取未来的排行榜数据")

        self._date = date_

    async def get_summary(self) -> SummaryData:
        data = await send_request(
            datasource="JIANSHU",
            method="GET",
            path="/asimov/fp_rankings/voter_notes",
            params={"date": self._date.strftime(r"%Y%m%d")},
            response_type="JSON",
        )

        return SummaryData(
            fp_to_author_amount_sum=normalize_assets_amount(data["author_fp"]),
            fp_to_voter_amount_sum=normalize_assets_amount(data["voter_fp"]),
            total_fp_amount_sum=normalize_assets_amount(data["fp"]),
        )._validate()

    async def iter_records(self) -> AsyncGenerator[RecordData, None]:
        data = await send_request(
            datasource="JIANSHU",
            method="GET",
            path="/asimov/fp_rankings/voter_notes",
            params={"date": self._date.strftime(r"%Y%m%d")},
            response_type="JSON",
        )

        for ranking, item in enumerate(data["notes"], start=1):
            yield RecordData(
                ranking=ranking,
                title=item["title"],
                slug=item["slug"],
                total_fp_amount=normalize_assets_amount(item["fp"]),
                fp_to_author_amount=normalize_assets_amount(item["author_fp"]),
                fp_to_voter_amount=normalize_assets_amount(item["voter_fp"]),
                author_info=_AuthorInfoField(
                    name=item["author_nickname"],
                    avatar_url=item["author_avatar"],
                ),
            )
