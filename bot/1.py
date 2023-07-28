import asyncio
from redis.asyncio import Redis

redis = Redis(port=16379)

async def receive_message_from_queue():
    message = await redis.lpop('parser')

    return message

async def main():
    # Получение сообщения из очереди

    message = await receive_message_from_queue()

    if message:
        print(f"Получено сообщение: {message.decode()}")

# Создание цикла событий asyncio и запуск программы
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
