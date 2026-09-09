"""Day 13: Await async work and collect actual values."""

import asyncio

async def fetch_user(user_id):
    await asyncio.sleep(0.01)
    return {"id": user_id, "active": True}

async def main():
    users = [fetch_user(user_id) for user_id in range(1, 4)]
    assert users == [
        {"id": 1, "active": True},
        {"id": 2, "active": True},
        {"id": 3, "active": True},
    ]
    print("Day 13 passed")

asyncio.run(main())
