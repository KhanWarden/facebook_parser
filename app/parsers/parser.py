import asyncio
from arsenic import get_session, browsers, services


class FacebookParser:
    def __init__(self, db):
        self.db = db

    async def start(self):
        service = services.Geckodriver(log_file="geckodriver.log")
        browser = browsers.Chrome()

        async with get_session(service, browser) as session:
            await self.parse_groups(session)

    async def parse_groups(self, session):
        await session.get('https://www.facebook.com/')
