from bittorrent import Tracker
import time

AGENTS = (("",0))

tracker = Tracker()
tracker.run()

EXIT_FLAG = False

while not EXIT_FLAG:
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        tracker.stop()
        EXIT_FLAG = True