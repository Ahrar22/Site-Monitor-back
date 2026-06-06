import shutil
import schedule as sc
import time

SOURCE_DIR = ".//Game"
DEST_DIR = "D://BACKUP"


def backup():
    shutil.copytree(SOURCE_DIR, DEST_DIR, dirs_exist_ok=True)
    print("Backup completed successfully.")


# Schedule the backup to run every day at 2:00 AM
# sc.every().day.at("02:00").do(backup)
sc.every(10).seconds.do(backup)

while True:
    sc.run_pending()
    time.sleep(1)
