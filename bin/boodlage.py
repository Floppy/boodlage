#!/usr/bin/env python

import urllib, time, re, telnetlib

url = "http://www.nationalgrid.com/ngrealtime/realtime/systemdata.aspx"
match = ".*Frequency: (.*?)Hz.*"
in_min = 49.8
in_max = 50.2
interval = 15

host = "localhost"
event = "pitch"
out_min = 140.0
out_max = 260.0

in_range = in_max - in_min
out_range = out_max - out_min
multiplier = out_range / in_range

while(1):
  # Load frequency data
  result = urllib.urlopen(url).read()
  regexp = re.compile(match)
  f = regexp.findall(result)[0]
  # scale up
  x = float(f) - in_min
  f = out_min + (x * multiplier)
  # set pitch
  tn = telnetlib.Telnet(host, 31863)
  tn.write("{0} {1}\n".format(event, f))
  # Wait
  time.sleep(interval)
  
