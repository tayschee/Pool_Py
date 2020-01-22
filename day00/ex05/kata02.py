import sys

(hour, minutes, year, month, day) = (3, 30, 2019, 9, 25)
sys.stdout.write("%02d/%02d/%04d %02d:%02d" % (month, day, year, hour, minutes))
