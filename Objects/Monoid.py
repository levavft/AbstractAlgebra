from __future__ import annotations
from collections.abc import Callable, Mapping
from Common.Types import T


class Monoid:
    """
    We use the multiplicative notation, e.g: 1, S, f where:
    for all a,b in S:
    f(1,a)=f(a,1)=a
    f(a,b) in S
    """
    def __init__(self, one: T, elements: set[T], function: Callable[[T, T], T]):
        """
        :param one: 1
        :param elements: S
        :param function: f
        """
        assert one in elements
        self.one = one
        self.elements = elements
        self.function = function

    @staticmethod
    def monoid_from_generators(generators: set[T], equivalence_relation: Mapping[[T], T]) -> Monoid:
        raise NotImplementedError

    def submonoid_from_equivalence_relation(self, equivalence_relation: Mapping[[T], T]) -> Monoid:
        raise NotImplementedError

    def submonoids(self):
        raise NotImplementedError
