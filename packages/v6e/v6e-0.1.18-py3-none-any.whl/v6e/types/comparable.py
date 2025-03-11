from __future__ import annotations

import typing as t

from v6e.types.base import V6eType, parser


class _Comparable(t.Protocol):
    def __lt__(self, other: t.Self, /) -> bool: ...
    def __gt__(self, other: t.Self, /) -> bool: ...
    def __le__(self, other: t.Self, /) -> bool: ...
    def __ge__(self, other: t.Self, /) -> bool: ...


Comparable = t.TypeVar("Comparable", bound=_Comparable)


class V6eComparableMixin(V6eType[Comparable]):
    @parser
    def gt(self, value: Comparable, x: Comparable, /, msg: str | None = None):
        if value <= x:
            raise ValueError(
                f"Value {value} must be greater than {x}",
            )

    @parser
    def gte(self, value: Comparable, x: Comparable, /, msg: str | None = None):
        if value < x:
            raise ValueError(
                f"Value {value} must be greater than or equal to {x}",
            )

    @parser
    def lt(self, value: Comparable, x: Comparable, /, msg: str | None = None):
        if value >= x:
            raise ValueError(
                f"Value {value} must less than {x}",
            )

    @parser
    def lte(self, value: Comparable, x: Comparable, /, msg: str | None = None):
        if value > x:
            raise ValueError(
                f"Value {value} must less than or equal to {x}",
            )

    @parser
    def min(self, value: Comparable, x: Comparable, /, msg: str | None = None):
        if value < x:
            raise ValueError(
                f"Value {value} must be greater than or equal to {x}",
            )

    @parser
    def max(self, value: Comparable, x: Comparable, /, msg: str | None = None):
        if value > x:
            raise ValueError(
                f"Value {value} must less than or equal to {x}",
            )
