from core import create_tables, insert_logs, show_logs, add_user, show_users, update_worker_surname


create_tables()
add_user("Safronov", "boss")
add_user("Kostenko", "worker")
show_users()
insert_logs([
    {"user_id": 1, "action": "enter"},
    {"user_id": 2, "action": "enter"},
    {"user_id": 1, "action": "quit"}
])
show_logs()