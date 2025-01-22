from motor.motor_asyncio import AsyncIOMotorClient


class MongoDB:
    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(self.uri)
        self.db = self.client[self.db_name]

    async def save_post(self, post_data):
        await self.db.posts.insert_one(post_data)
