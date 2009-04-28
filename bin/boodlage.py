#!/usr/bin/env python

import simplejson, urllib, os, time

while(1):
  # Load frequency data
  url = "http://caniturniton.com/api/json"  
  result = simplejson.load(urllib.urlopen(url))
  f = result['decision']['frequency']
  print f
  # scale up
  diff = f - 50.0
  diff = diff * 300
  f = 200.0 + diff
  # set pitch
  os.system("boodle-event.py pitch {0}".format(f))
  # Wait
  time.sleep(60)
  
