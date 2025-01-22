import asyncio
from app.parsers.parser import FacebookParser
from app.database.db import MongoDB


async def main():
    db = MongoDB(uri="mongodb://localhost:27017", db_name="facebook_data")
    await db.connect()

    parser = FacebookParser(db)
    await parser.start()


if __name__ == "__main__":
    asyncio.run(main())
