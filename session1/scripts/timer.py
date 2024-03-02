import time
import sys

seconds = sys.argv[1]

for i in range(int(seconds)):
    print(i+1)
    time.sleep(1)