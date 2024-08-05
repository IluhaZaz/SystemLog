from core import SystemCoreSync


s = SystemCoreSync()

s.create_tables()
s.add_user("Safronov", "boss")
s.add_user("Kostenko", "worker")
s.show_users()
s.insert_logs([
    {"user_id": 1, "action": "enter"},
    {"user_id": 2, "action": "enter"},
    {"user_id": 1, "action": "quit"}
])
s.update_worker_data(user_id=1, new_role="worker")
s.show_logs()