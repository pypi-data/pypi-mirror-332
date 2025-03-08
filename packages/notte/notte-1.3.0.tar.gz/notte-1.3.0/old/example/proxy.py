from typing_extensions import override
from loguru import logger

from notte.browser.observation import Observation
from notte.common.agent.proxy import BaseProxy, ProxyObservation
from notte.env import NotteEnv

from .parser import GufoParser
from .perception import GufoPerception
from .prompt import GufoPrompt


class GufoProxy(BaseProxy):
    def __init__(
        self,
        prompt: GufoPrompt,
        parser: GufoParser,
        perception: GufoPerception,
        env: NotteEnv,
    ):
        self.parser: GufoParser = parser
        self.prompt: GufoPrompt = prompt
        self.perception: GufoPerception = perception
        self.env: NotteEnv = env or NotteEnv()

    def perceive(self, obs: Observation | None = None) -> str:
        if obs is None:
            return self.prompt.env_rules()
        return f"""
{self.perception.perceive(obs)}
{self.prompt.select_action_rules()}
{self.prompt.completion_rules()}
"""

    @override
    async def step(self, text: str) -> ProxyObservation:
        """
        Executes actions in the Notte environment based on LLM decisions.

        This method demonstrates how to:
        1. Parse LLM output into Notte commands
        2. Execute those commands in the environment
        3. Format the results back into text for the LLM

        Users should customize this method to:
        - Handle additional Notte endpoints
        - Implement custom error handling
        - Format observations specifically for their LLM

        Args:
            env: The Notte environment instance
            text: The LLM's response containing the desired action

        Returns:
            str: Formatted observation from the environment
        """
        params = self.parser.parse(text)
        if params.output is not None:
            return ProxyObservation(
                obs=params.output.answer,
                output=params.output,
                snapshot=self.env.context.snapshot,
            )
        logger.debug(f"Picking Notte endpoint: {params.endpoint}")
        obs: Observation | None = None
        match params.endpoint:
            case "observe":
                if params.obs_request is None:
                    raise ValueError("No URL provided")
                obs = await self.env.observe(params.obs_request.url)
            case "step":
                if params.step_request is None:
                    raise ValueError("No action provided")
                obs = await self.env.step(
                    params.step_request.action_id,
                    params.step_request.value,
                    params.step_request.enter,
                )
            case "scrape":
                if params.scrape_request is None:
                    raise ValueError("No URL provided")
                obs = await self.env.scrape(params.scrape_request.url)
            case _:
                logger.debug(f"Unknown provided endpoint: {params.endpoint} so we'll just recap the rules...")
        return ProxyObservation(
            obs=self.perceive(obs),
            output=params.output,
            snapshot=self.env.context.snapshot,
        )
