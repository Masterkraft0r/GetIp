import socket
import time
import sys

# CONSTANTS
# COUNT = 3
# FILTER = '192.100.125'

if not len(sys.argv) == 3:
  print("Usage: getip.exe <max_time_in_sec> <filter>")
  sys.exit(1)

COUNT = int(sys.argv[1])
FILTER = sys.argv[2]

hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex(socket.gethostname())

for i in range(COUNT):
  for ip in ipaddrlist:
    if FILTER in ip:
      with open("ip.txt", "w") as f:
        f.write(ip)
      sys.exit(0)
  time.sleep(1)

with open("ip.txt", "w") as f:
  f.write("")