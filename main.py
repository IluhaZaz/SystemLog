from core import create_tables, insert_logs


create_tables()
insert_logs([
    {"user_id": 1, "surname": "Safronov"}
])