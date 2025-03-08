from pathlib import Path
from typing import Any
from dotenv import load_dotenv
from patchright.async_api import async_playwright
from steel import Steel
import asyncio
import os

# Load environment variables from .env file
load_dotenv()

STEEL_API_KEY = os.getenv('STEEL_API_KEY')
STEEL_BASE_URL = "localhost:3000"

# Initialize Steel client with the API key from environment variables
client = Steel(steel_api_key=STEEL_API_KEY, base_url=f"http://{STEEL_BASE_URL}")


async def extract_story_details(row: Any) -> dict[str, str]:
    title_element = row.locator(".titleline > a")
    title = await title_element.text_content()
    link = await title_element.get_attribute("href")

    points_element = row.locator("xpath=following-sibling::tr[1]").locator(".score")
    points = "0"
    if await points_element.count() > 0:
        points = (await points_element.text_content()).split()[0]

    return {
        "title": title,
        "link": link,
        "points": points
    }


async def main() -> None:
    session = None
    browser = None

    try:
        print("Creating Steel session...")
        session = client.sessions.create()

        print(f"""Session created successfully with Session ID: {session.id}.
You can view the session live at {session.session_viewer_url}
        """)

        # Connect Playwright to the Steel session
        playwright = await async_playwright().start()
        browser = await playwright.chromium.connect_over_cdp(
            f"ws://{STEEL_BASE_URL}/devtools/browser/{session.id}"
        )

        print("Connected to browser via Playwright")

        # Create page at existing context to ensure session is recorded
        current_context = browser.contexts[0]
        page = await current_context.new_page()

        # Navigate to Hacker News and extract the top 5 stories
        print("Navigating to Hacker News...")
        await page.goto("https://news.ycombinator.com", wait_until="networkidle")

        # Find all story rows
        story_rows = await page.locator("tr.athing").all()
        story_rows = story_rows[:5]  # Get first 5 stories

        # Extract the top 5 stories using Playwright's locators
        print("\nTop 5 Hacker News Stories:")
        for i, row in enumerate(story_rows, 1):
            story = await extract_story_details(row)
            print(f"\n{i}. {story['title']}")
            print(f"   Link: {story['link']}")
            print(f"   Points: {story['points']}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cleanup: Gracefully close browser and release session when done
        if browser:
            await browser.close()
            print("Browser closed")

        if session:
            print("Releasing session...")
            client.sessions.release(session.id)
            print("Session released")

        print("Done!")


# Run the script
if __name__ == "__main__":
    asyncio.run(main())