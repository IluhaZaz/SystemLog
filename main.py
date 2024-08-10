import asyncio

from time import sleep

from core import SystemCoreSync, SystemCoreAsync
from orm import SystemORMSync
from models import Action, LogTable, Role

async def main():
    await SystemCoreAsync.create_tables()
    await SystemCoreAsync.add_user("Safronov", "boss")
    await SystemCoreAsync.add_user("Kostenko", "worker")
    await SystemCoreAsync.show_users()
    await SystemCoreAsync.insert_logs([
        {"user_id": 1, "action": "enter"},
        {"user_id": 2, "action": "enter"},
        {"user_id": 1, "action": "quit"}
    ])
    await SystemCoreAsync.update_worker_data(user_id=1, new_role="worker")
    await SystemCoreAsync.show_logs()

asyncio.get_event_loop().run_until_complete(main())

# s = SystemORMSync()
# s.create_tables()
# s.add_user("Safronov", Role.chief)
# s.add_user("Kostenko", Role.worker)
# s.add_user("Nesterenko", Role.user)
# s.add_user("Lukacheva", Role.worker)
# s.add_user("Borivova", Role.fired)

# s.update_worker_data(2, new_surname="Popov", new_role=Role.deputy_chief)

# s.insert_logs([
#                 LogTable(user_id=1, action = Action.enter),
#                 LogTable(user_id=2, action = Action.enter),
#                 LogTable(user_id=1, action = Action.quit)
#                 ])
# sleep(5)
# s.insert_logs([
#                 LogTable(user_id=2, action = Action.quit),
#                 LogTable(user_id=3, action = Action.enter),
#                 LogTable(user_id=5, action = Action.enter),
#                 LogTable(user_id=5, action = Action.quit),
#                 LogTable(user_id=4, action = Action.enter),
#                 LogTable(user_id=3, action = Action.quit)
#                 ])
# s.show_users()
# s.show_logs()
# s.show_logs_by_user()


# s = SystemCoreSync()

# s.create_tables()
# s.add_user("Safronov", "boss")
# s.add_user("Kostenko", "worker")
# s.show_users()
# s.insert_logs([
#     {"user_id": 1, "action": "enter"},
#     {"user_id": 2, "action": "enter"},
#     {"user_id": 1, "action": "quit"}
# ])
# s.update_worker_data(user_id=1, new_role="worker")
# s.show_logs()