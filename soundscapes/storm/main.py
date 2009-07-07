from boopak.package import *
from boodle import agent, builtin

storms = bimport('com.eblong.ow.storm')

class Storm(agent.Agent):

  def run(self):
    if (self.firsttime):
      self.listen('intensity')
      self.agent = storms.NoStormYet()
    fader = builtin.FadeInOutAgent(self.agent, 3600, 0.1)
    self.sched_agent(fader)
    self.resched(3600)
    
  def receive(self, event, intensity):
    if (float(intensity) > 0.75):
      self.agent = storms.HeavyStorm()
    elif (float(intensity) > 0.5):
      self.agent = storms.MediumStorm()
    elif (float(intensity) > 0.25):
      self.agent = storms.LightStorm()
    else:
      self.agent = storms.NoStormYet()
    fader = builtin.FadeInOutAgent(self.agent, 3600, 0.1)
    self.sched_agent(fader)
      

