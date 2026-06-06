import requests
import schedule as sc
import time

URL = "https://google.com"

def check_website():
    try:
        respones = requests.get(URL)

        if respones.status_code == 200:
            print("Google is online!!!")
        else:
            print("Google is offline!!!")
    except Exception as e:
        print("URL is not found...")
    
sc.every(5).seconds.do(check_website)

while True:
    sc.run_pending()
    time.sleep(1)