from notte.browser.observation import Observation
from notte.env import NotteEnv

from dataclasses import dataclass

@dataclass
class TryObservation:
    observation: Observation | None
    is_success: bool
    error_msg: str | None
    
    @staticmethod
    def from_observation(obs: Observation) -> "TryObservation":
        return TryObservation(observation=obs, is_success=True, error_msg=None)
    
    @staticmethod
    def from_error(error_msg: str) -> "TryObservation":
        return TryObservation(observation=None, is_success=False, error_msg=error_msg)

# TODO: use specific exceptions for each error case and handle them accordingly

class TryNotteEnv:
    
    def __init__(self, base_env: NotteEnv):
        self.base_env: NotteEnv = base_env
    
    async def try_observe(self, url: str) -> TryObservation:
        try:
            obs = await self.base_env.goto(url)
            return TryObservation.from_observation(obs)
        except Exception as e:
            return TryObservation.from_error(str(e))

    async def try_step(self, action: str) -> TryObservation:
        try:
            obs = await self.base_env.step(action)
            return TryObservation.from_observation(obs)
        except Exception as e:
            return TryObservation.from_error(str(e))

    async def try_scrape(self, url: str) -> TryObservation:
        try:
            obs = await self.base_env.scrape(url)
            return TryObservation.from_observation(obs)
        except Exception as e:
            return TryObservation.from_error(str(e))
