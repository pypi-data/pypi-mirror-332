from abc import ABC, abstractmethod
from pydantic import BaseModel

from notte.browser.snapshot import BrowserSnapshot
from notte.controller.actions import BaseAction, CompletionAction


class ProxyObservation(BaseModel):
    obs: str
    action: BaseAction | None = None
    output: CompletionAction | None = None
    snapshot: BrowserSnapshot | None = None


class BaseProxy(ABC):

    @abstractmethod
    async def step(self, text: str) -> ProxyObservation:
        raise NotImplementedError