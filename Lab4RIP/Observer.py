from __future__ import annotations
from abc import ABC, abstractmethod
#from icecream_cafe.IcecreamBuilder import Iceman

class IcecreamObserver(ABC):

    @abstractmethod
    def update(self, subject: Iceman) -> None:
        pass


class StartIcecreamObserver(IcecreamObserver):
    def update(self, subject: Iceman) -> None:
        print(f"{subject.name} makes {subject.builder.icecream_type}\n")


class FinishIcecreamObserver(IcecreamObserver):
    def update(self, subject: Iceman) -> None:
        print(f"{subject.name} finished {subject.builder.icecream_type}")
        print(f"Parts:")
        subject.builder.icecream.list_parts()