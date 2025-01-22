import asyncio
import os
from arsenic import get_session, browsers, services
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")


async def authorization(session):
    await session.get("https://www.facebook.com/")

    email_elem = await session.get_element("#email")
    await email_elem.send_keys(LOGIN)

    password_elem = await session.get_element("#pass")
    await password_elem.send_keys(PASSWORD)

    await password_elem.send_keys("\n")

    await asyncio.sleep(5)
