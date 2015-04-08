import socket
import time
import sys

if not len(sys.argv) == 3:
  print("Usage: getip.exe <max_time_in_sec> <filter>")
  sys.exit(1)

COUNT = int(sys.argv[1])
FILTER = sys.argv[2]

for i in range(COUNT):
  ipaddrlist = socket.gethostbyname_ex(socket.gethostname())[2]

  for ip in ipaddrlist:
    if FILTER in ip:
      with open("ip.txt", "w") as f:
        f.write(ip)
      sys.exit(0)

  time.sleep(1)

with open("ip.txt", "w") as f:
  f.write("")