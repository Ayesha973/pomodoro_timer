# test_log.py
from data.db import init_db, log_session
from datetime import datetime

init_db()
log_session("Study", "Focus", datetime.now(), 1500)
