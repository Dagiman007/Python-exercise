import webbrowser
import time
import random

while True:
    sites = random.choice(["Python.org", "apple.com", "google.com"])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = rand.randrange(5, 20)
    time.sleep(seconds)
    
