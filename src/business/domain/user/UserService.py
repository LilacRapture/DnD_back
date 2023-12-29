from src.infrastructure.data.DataService import DataService


class UserService:
    data = DataService()

    async def create_user(self):
        return await self.data.create_user()

    async def delete_user(self, user_id):
        await self.data.delete_user(user_id)
