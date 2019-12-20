
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from dustbin_updater import updaterApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(updaterApi.update_dusbin_stat, 'interval', minutes=0.1)
    scheduler.start()