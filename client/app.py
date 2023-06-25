

import asyncio
import grpc
import users_pb2
import users_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = await stub.GetUsers(users_pb2.GetUsersRequest())
    print(response.users)


if __name__ == "__main__":
    asyncio.run(run())