from mss import mss
import time
from datetime import datetime
 
# Set interval (600 sec = 10 min)
interval = 600
 
while True:
    with mss() as screen:
        # Filepath will have the current datetime (e.g., 2022-02-02 13:17:21.png)
        filepath = f"{datetime.now().strftime('%Y-%m-%m %H:%M:%S')}.png"
        screen.shot(output=filepath)
 
    print(filepath)
    time.sleep(interval) # Wait 600 sec/ 10 min
