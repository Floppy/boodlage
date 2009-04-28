from boopak.package import *
from boodle import agent

tones = bimport('org.boodler.puretone')

class Sine(agent.Agent):

  def init(self):
    self.pitch = 100.0
  
  def run(self):
    if (self.firsttime):
      self.listen('pitch')
    dur = self.sched_note(tones.sine, self.pitch / 452.0, 1, 0.1)
    self.resched(dur)
    
  def receive(self, event, pitch):
    self.pitch = float(pitch)

