import asyncio

from time import sleep

from core import SystemCoreSync, SystemCoreAsync
from orm import SystemORMSync, SystemORMAsync
from models import Action, LogTable, Role

async def main():
    await SystemORMAsync.create_tables()
    await SystemORMAsync.add_user("Safronov", Role.chief)
    await SystemORMAsync.add_user("Kostenko", Role.worker)
    await SystemORMAsync.add_user("Nesterenko", Role.user)
    await SystemORMAsync.add_user("Lukacheva", Role.worker)
    await SystemORMAsync.add_user("Borivova", Role.fired)

    await SystemORMAsync.update_worker_data(2, new_surname="Popov", new_role=Role.deputy_chief)

    await SystemORMAsync.insert_logs([
                    LogTable(user_id=1, action = Action.enter),
                    LogTable(user_id=2, action = Action.enter),
                    LogTable(user_id=1, action = Action.quit)
                    ])
    sleep(5)
    await SystemORMAsync.insert_logs([
                    LogTable(user_id=2, action = Action.quit),
                    LogTable(user_id=3, action = Action.enter),
                    LogTable(user_id=5, action = Action.enter),
                    LogTable(user_id=5, action = Action.quit),
                    LogTable(user_id=4, action = Action.enter),
                    LogTable(user_id=3, action = Action.quit)
                    ])
    await SystemORMAsync.show_users()
    await SystemORMAsync.show_logs()
    await SystemORMAsync.show_logs_by_user()

asyncio.get_event_loop().run_until_complete(main())


# async def main():
#     await SystemCoreAsync.create_tables()
#     await SystemCoreAsync.add_user("Safronov", "boss")
#     await SystemCoreAsync.add_user("Kostenko", "worker")
#     await SystemCoreAsync.show_users()
#     await SystemCoreAsync.insert_logs([
#         {"user_id": 1, "action": "enter"},
#         {"user_id": 2, "action": "enter"},
#         {"user_id": 1, "action": "quit"}
#     ])
#     await SystemCoreAsync.update_worker_data(user_id=1, new_role="worker")
#     await SystemCoreAsync.show_logs()

# asyncio.get_event_loop().run_until_complete(main())

# SystemORMSync.create_tables()
# SystemORMSync.add_user("Safronov", Role.chief)
# SystemORMSync.add_user("Kostenko", Role.worker)
# SystemORMSync.add_user("Nesterenko", Role.user)
# SystemORMSync.add_user("Lukacheva", Role.worker)
# SystemORMSync.add_user("Borivova", Role.fired)

# SystemORMSync.update_worker_data(2, new_surname="Popov", new_role=Role.deputy_chief)

# SystemORMSync.insert_logs([
#                 LogTable(user_id=1, action = Action.enter),
#                 LogTable(user_id=2, action = Action.enter),
#                 LogTable(user_id=1, action = Action.quit)
#                 ])
# sleep(5)
# SystemORMSync.insert_logs([
#                 LogTable(user_id=2, action = Action.quit),
#                 LogTable(user_id=3, action = Action.enter),
#                 LogTable(user_id=5, action = Action.enter),
#                 LogTable(user_id=5, action = Action.quit),
#                 LogTable(user_id=4, action = Action.enter),
#                 LogTable(user_id=3, action = Action.quit)
#                 ])
# SystemORMSync.show_users()
# SystemORMSync.show_logs()
# SystemORMSync.show_logs_by_user()


# s = SystemCoreSync()

# SystemCoreSync.create_tables()
# SystemCoreSync.add_user("Safronov", "boss")
# SystemCoreSync.add_user("Kostenko", "worker")
# SystemCoreSync.show_users()
# SystemCoreSync.insert_logs([
#     {"user_id": 1, "action": "enter"},
#     {"user_id": 2, "action": "enter"},
#     {"user_id": 1, "action": "quit"}
# ])
# SystemCoreSync.update_worker_data(user_id=1, new_role="worker")
# SystemCoreSync.show_logs()