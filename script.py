import asyncio
import datetime
import os

from playwright import async_api


async def main():
    print("Hello world")

    pw = await async_api.async_playwright().start()
    browser = await pw.chromium.connect_over_cdp(os.environ["CHROME_URL"])
    context = await browser.new_context()

    page = await context.new_page()
    await page.goto("https://google.com", wait_until="networkidle")

    t = datetime.datetime.now().isoformat()
    await page.screenshot(path=f"/opt/app/screenshots/{t}.png")

    print("Goodbye world")


if __name__ == "__main__":
    asyncio.run(main())
