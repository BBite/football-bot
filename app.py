import asyncio


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.db_api import db
    db.check_db_exists()

    # from utils.notify_admins import on_startup_notify
    # await on_startup_notify(dp)


DELAY = 3600


def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    from data.fill_data import fill_all

    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, fill_all, loop)

    fill_all()

    executor.start_polling(dp, loop=loop, on_startup=on_startup)
