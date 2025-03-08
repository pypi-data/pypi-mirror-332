import os

import requests
from loguru import logger
from typing_extensions import override

from notte.browser.pool.base import BrowserWithContexts
from notte.browser.pool.cdp_pool import CDPBrowserPool, CDPSession


class SteelBrowserPool(CDPBrowserPool):
    def __init__(
        self,
        local_host: bool = False,
        verbose: bool = False,
    ):
        super().__init__(verbose)
        self.steel_api_key: str | None = os.getenv("STEEL_API_KEY")
        if self.steel_api_key is None:
            raise ValueError("STEEL_API_KEY is not set")
        self.steel_base_url: str = "localhost:3000" if local_host else "api.steel.dev"

    @override
    def create_session_cdp(self) -> CDPSession:
        logger.info("Creating Steel session...")

        url = f"https://{self.steel_base_url}/v1/sessions"

        headers = {"Steel-Api-Key": self.steel_api_key}

        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data: dict[str, str] = response.json()
        if "localhost" in self.steel_base_url:
            cdp_url = f"ws://{self.steel_base_url}/v1/devtools/browser/{data['id']}"
        else:
            cdp_url = f"wss://connect.steel.dev?apiKey={self.steel_api_key}&sessionId={data['id']}"
        return CDPSession(session_id=data["id"], cdp_url=cdp_url)

    @override
    async def close_playwright_browser(self, browser: BrowserWithContexts, force: bool = True) -> bool:
        if self.verbose:
            logger.info(f"Closing CDP session for URL {browser.cdp_url}")
        steel_session = self.sessions[browser.browser_id]

        url = f"https://{self.steel_base_url}/v1/sessions/{steel_session.session_id}/release"

        headers = {"Steel-Api-Key": self.steel_api_key}

        response = requests.post(url, headers=headers)
        if response.status_code != 200:
            if self.verbose:
                logger.error(f"Failed to release Steel session {steel_session.session_id}: {response.json()}")
            return False
        del self.sessions[browser.browser_id]
        return True
