
import random
import matplotlib.pyplot as plt
from IPython import display
import time

group_affinity_threshold = .51

class Agent():
    def __init__(self,xlocation, ylocation):
        self.x = xlocation
        self.y = ylocation


def map_all_agents(listofagents):
    agents_XCoordinate = [] # this is an empty list that will store our X-coordinates, don't change this command
    agents_YCoordinate = [] # this is an empty list that will store our y-coordinates, don't change this command
    
    ### use a for loop to add all the x attributes from our list of objects to the agents_XCoordinate list and all the y attributes from our list of objects to the agents_YCoordinate list 
    for item in listofagents:
      agents_XCoordinate.append(item.x)
      agents_YCoordinate.append(item.y)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(agents_XCoordinate, agents_YCoordinate, 'o', markerfacecolor='purple')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()


def moveagents(listofagents):
    for each_agent in listofagents:
        each_agent.x = random.randint(0,100)
        each_agent.y = random.randint(0,100)
        
def make_agents_dance(agentslist, num_steps=10):
  for i in range(num_steps):
    moveagents(agentslist)
    map_all_agents(agentslist)
    time.sleep(1) # keep this command 4th
    display.clear_output(wait=True) # keep this command last


class AgentNew(Agent):
    # pass # LAB PROB 10; COPY ONLY THE FUNCTION (NOT THE FUNCTION CALLS)
    def __init__(self, xlocation,ylocation,group, status="unhappy"):
        super().__init__(xlocation,ylocation)
        self.group = group
        self.status = status


class PurpleAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)
class GoldAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)

#### Note CombinedList Must have the PurpleAgents before the GoldAgents

def map_colorful_agents(CombinedList):  # what argument should go in this function?

    Purple_XCoordinate = [item.x for item in CombinedList if item.group=="Purple"] ### fill in the blanks to make this list comprehension work
    Purple_YCoordinate = [item.y for item in CombinedList if item.group=="Purple"] # model this after the above list comprehension
    Gold_XCoordinate = [item.x for item in CombinedList if item.group=="Gold"]
    Gold_YCoordinate = [item.y for item in CombinedList if item.group=="Gold"]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(Purple_XCoordinate, Purple_YCoordinate, 'o', markerfacecolor='purple')
    ax.plot(Gold_XCoordinate, Gold_YCoordinate, 'o', markerfacecolor='gold')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()

class AgentNew(Agent):
    def __init__(self, xlocation,ylocation,group, status="unhappy"):
        super().__init__(xlocation,ylocation)
        self.group = group
        self.status = status

    def move_if_unhappy(self):  # what arguement(s) are needed here?
        if self.status=="unhappy":  ### there is a mistake in this command - fix it
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)


class AgentNew(Agent):

    ### PASTE IN YOUR CONSTRUCTOR
    def __init__(self, xlocation,ylocation,group, status="unhappy"):
        super().__init__(xlocation,ylocation)
        self.group = group
        self.status = status
    ### paste in move_if_unhappy method
    def move_if_unhappy(self):  # what arguement(s) are needed here?
        if self.status=="unhappy":  ### there is a mistake in this command - fix it
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

    def check_neighbors(self, agentlist):  # note this method needs not only the self attributes - it also needs a list of agents
        zlist = list(filter(lambda x : self.x - 10 < x.x < self.x + 10, agentlist))### here, use a filter and a lambda function to find all agents in a list who are within 10 spaces in the X direction of the agent that is calling the method
        zlist = list(filter(lambda x : self.y - 10 < x.y < self.y + 10, zlist))### do the same thing now to filter for agents within 10 spaces in the y direction - what list do you want to apply this lambda function to?
        same_group_neighbor =  [item for item in zlist if item.group == self.group]### use list comprehension to only keep members of zlist who are of the same group as this agent
        opposite_group_neighbor = [item for item in zlist if item.group != self.group]### use list comprehension to only keep members of zlist who are of the opposite group as this agent
        # print(len(same_group_neighbor), "same group neighbors, and ", len(zlist), " total neibhors" ) # this is commented out but you can use this as a diagnostic to make sure its working
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold: # this command works; it checks the percentage of same group neighbors against some threshold to determine the agents happiness
            self.status="happy"
        else:
            self.status="unhappy"

class PurpleAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)
class GoldAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)


for x in range(15):
    for agent in testlist:
        agent.check_neighbors(testlist)  # does this need any arguments?
    for agent in testlist:
        agent.move_if_unhappy() # does this need any arguments?
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)

class PurpleDiversitySeekers(PurpleAgents):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)
    def check_neighbors(self, agentlist):
        zlist = list(filter(lambda x : self.x - 10 < x.x < self.x + 10, agentlist))### here, use a filter and a lambda function to find all agents in a list who are within 10 spaces in the X direction of the agent that is calling the method
        zlist = list(filter(lambda x : self.y - 10 < x.y < self.y + 10, zlist))### do the same thing now to filter for agents within 10 spaces in the y direction - what list do you want to apply this lambda function to?
        same_group_neighbor =  [item for item in zlist if item.group == self.group]### use list comprehension to only keep members of zlist who are of the same group as this agent
        opposite_group_neighbor = [item for item in zlist if item.group != self.group]### use list comprehension to only keep members of zlist who are of the opposite group as this agent
  
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) <= group_affinity_threshold: # this command works; it checks the percentage of same group neighbors against some threshold to determine the agents happiness
            self.status="happy"
        else:
            self.status="unhappy"
class GoldDiversitySeekers(GoldAgents):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)
    def check_neighbors(self, agentlist):
        zlist = list(filter(lambda x : self.x - 10 < x.x < self.x + 10, agentlist))### here, use a filter and a lambda function to find all agents in a list who are within 10 spaces in the X direction of the agent that is calling the method
        zlist = list(filter(lambda x : self.y - 10 < x.y < self.y + 10, zlist))### do the same thing now to filter for agents within 10 spaces in the y direction - what list do you want to apply this lambda function to?
        same_group_neighbor =  [item for item in zlist if item.group == self.group]### use list comprehension to only keep members of zlist who are of the same group as this agent
        opposite_group_neighbor = [item for item in zlist if item.group != self.group]### use list comprehension to only keep members of zlist who are of the opposite group as this agent
  
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) <= group_affinity_threshold: # this command works; it checks the percentage of same group neighbors against some threshold to determine the agents happiness
            self.status="happy"
        else:
            self.status="unhappy"

