from core import create_tables, insert_logs, show_logs, update_worker_name_in_logs


create_tables()
insert_logs([
    {"user_id": 1, "surname": "Safronov", "action": "enter"},
    {"user_id": 2, "surname": "Kostenko", "action": "enter"}
])
update_worker_name_in_logs(1, "Petrov")
show_logs()