from boopak.package import *
from boodle import agent

water = bimport('org.boodler.old.water')

class Drip(agent.Agent):

  def init(self):
    self.delay = 1
  
  def run(self):
    if (self.firsttime):
      self.listen('delay')
    self.sched_note(water.droplet_plink)
    self.resched(self.delay)
    
  def receive(self, event, delay):
    self.delay = float(delay)

