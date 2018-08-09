from typing import TypeVar, Callable
from abc import ABC, abstractmethod

S = TypeVar('S')
A = TypeVar('A')
Type1 = Callable[[S], float]
Type2 = Callable[[S], Callable[[A], float]]


class OptBase(ABC):

    @abstractmethod
    def get_value_func(self, pol_func: Type2) -> Type1:
        pass

    @abstractmethod
    def get_act_value_func(self, pol_func: Type2) -> Type2:
        pass

    @abstractmethod
    def get_optimal_det_policy_func(self) -> Callable[[S], A]:
        pass

