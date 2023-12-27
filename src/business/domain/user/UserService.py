from src.infrastructure.data.DataService import DataService


class UserService:
    data = DataService()

    async def create_user(self):
        return await self.data.create_user()
