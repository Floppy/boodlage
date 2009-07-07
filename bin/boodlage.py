#!/usr/bin/env python

import urllib, time, re, telnetlib, sys
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read(sys.argv[1:])

url = config.get('Main', 'url')
match = config.get('Main', 'match')
in_min = config.getfloat('Main', 'in_min')
in_max = config.getfloat('Main', 'in_max')
interval = config.getfloat('Main', 'interval')
host = config.get('Main', 'host')
event = config.get('Main', 'event')
out_min = config.getfloat('Main', 'out_min')
out_max = config.getfloat('Main', 'out_max')

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
  print("{0} {1}".format(event, f))
  tn = telnetlib.Telnet(host, 31863)
  tn.write("{0} {1}\n".format(event, f))
  # Wait
  time.sleep(interval)
  
