from __future__ import division
from __future__ import print_function

import sys
import math
import time
import queue as Q


#### SKELETON CODE ####
## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        print("CREATING PUZZE STATE")
        print("CONFIG=", config)
        print("N=", n)
        print("PARENT=", parent)
        print("action=", action)
        print("COST=", cost)
        print("CREATING PUZZE COMPLETE")
        """
       

        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)
        
    def __str___(self):
        return str(self.config)

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3*i : 3*(i+1)])
        

    def move_up(self):
        ### STUDENT CODE GOES HERE ###
        """ 
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index < self.n:
            return None

        new_config = self.config[:]
        temp = new_config[self.blank_index - self.n]
        new_config[self.blank_index - self.n] = 0
        new_config[self.blank_index] = temp
        return PuzzleState(config=new_config, n=self.n)
        
      
    def move_down(self):
        ### STUDENT CODE GOES HERE ###
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        if self.blank_index >= (math.pow(self.n, 2) - self.n):
            return None

        new_config = self.config[:]
        temp = new_config[self.blank_index + self.n]
        new_config[self.blank_index + self.n] = 0
        new_config[self.blank_index] = temp
        return PuzzleState(config=new_config, n=self.n)
   
      
    def move_left(self):
        ### STUDENT CODE GOES HERE ###
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """
        left = 0
        illegal = []
        while left < (math.pow(self.n, 2)):
            illegal.append(left)
            left += self.n
        if self.blank_index in illegal: return None
        
        new_config = self.config[:]
        temp = new_config[self.blank_index - 1]
        new_config[self.blank_index - 1] = 0
        new_config[self.blank_index] = temp
        return PuzzleState(config=new_config, n=self.n)


    def move_right(self):
        ### STUDENT CODE GOES HERE ###
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """
        left = (self.n - 1)
        illegal = []
        while left < (math.pow(self.n, 2)):
            illegal.append(left)
            left += self.n
        if self.blank_index in illegal: return None
        
        new_config = self.config[:]
        temp = new_config[self.blank_index + 1]
        new_config[self.blank_index + 1] = 0
        new_config[self.blank_index] = temp
        return PuzzleState(config=new_config, n=self.n)
      
    def expand(self):
        """ Generate the child nodes of this node """
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children
        
        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        i = -1
        final_children = []
        for child in children: 
            i += 1
            if child is None: 
                continue
            if i == 0: child.action = "Up"
            elif i == 1: child.action = "Down"
            elif i == 2: child.action = "Left"
            elif i == 3: child.action = "Right"
        
            final_children.append(child)
        
        self.children = [state for state in children if state is not None]
        return final_children

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput(path,nodes_expanded):
    print("PATH = ", path)
    print("Number of Nodes Expanded= ", nodes_expanded)


def get_path(state):

    path = []
    el = state
    while el is not None:
        path.append(el.action)
        el = el.parent
    
    path.remove("Initial")
    path.reverse()
    return path


def bfs_search(initial_state):
    """BFS search"""
    path_to_goal = []
    fList = {}
    eList = {}
    cost_of_path = 0
    nodes_expanded = -1
    search_depth = 0
    max_search_depth = 0
    ### STUDENT CODE GOES HERE ###
    frontier = Q.Queue()
    frontier.put(initial_state)
    t = tuple(initial_state.config)
    fList[t] = True
    explored = set()
    while frontier:
        state = frontier.get()
        t = tuple(state.config)
        fList[t] = False
        nodes_expanded += 1
        explored.add(state)
        t = tuple(state.config)
        eList[t] = True
        if test_goal(state.config): 
            writeOutput(get_path(state), nodes_expanded)
            return state
        
        for neighbor in state.expand(): 

                
            # if neighbor.config in eList: continue
            # if neighbor.config in fList: continue
            
            
            try: 
                if fList[tuple(neighbor.config)] == True:
                    continue
                if eList[tuple(neighbor.config)] == True:
                    continue
            except: 
                pass
            neighbor.parent = state
            
            """
            new = True 
            for fq in frontier.queue: 
                if neighbor.config == fq.config:
                    new = False
                    break 
            if new == True: 
                for fs in explored: 
                    if neighbor.config == fs.config: 
                        new = False
                        break
            if new == False: continue 
           """
            frontier.put(neighbor)
            t = tuple(neighbor.config)
            fList[t] = True
            #nodes_expanded += 1
           # if neighbor not in frontier.queue or neighbor not in explored:
           #    frontier.put(neighbor)
         
    return False


def dfs_search(initial_state):
 

    fList = {}
    eList = {}
    cost_of_path = 0
    nodes_expanded = -1
    search_depth = 0
    max_search_depth = 0
    ### STUDENT CODE GOES HERE ###
    frontier = list()
    frontier.append(initial_state)
    t = tuple(initial_state.config)
    fList[t] = True
    explored = set()
    while frontier:
        state = frontier.pop()
        t = tuple(state.config)
        fList[t] = False
        nodes_expanded += 1
        explored.add(state)
        t = tuple(state.config)
        eList[t] = True
        if test_goal(state.config): 
            writeOutput(get_path(state), nodes_expanded)
            return state
        xxx = state.expand()
        xxx.reverse()
        for neighbor in xxx: 

                
            # if neighbor.config in eList: continue
            # if neighbor.config in fList: continue
            
            
            try: 
                if fList[tuple(neighbor.config)] == True:
                    continue
                if eList[tuple(neighbor.config)] == True:
                    continue
            except: 
                pass
            neighbor.parent = state
            
            """
            new = True 
            for fq in frontier.queue: 
                if neighbor.config == fq.config:
                    new = False
                    break 
            if new == True: 
                for fs in explored: 
                    if neighbor.config == fs.config: 
                        new = False
                        break
            if new == False: continue 
           """
            frontier.append(neighbor)
            t = tuple(neighbor.config)
            fList[t] = True
            #nodes_expanded += 1
           # if neighbor not in frontier.queue or neighbor not in explored:
           #    frontier.put(neighbor)
         
    return False
    """
    frontier = list()
    explored = set()
    frontier.append(initial_state)
    nodes_expanded = -1
    state = None
    while len(frontier) > 0: 
        state = frontier.pop()
        nodes_expanded += 1
        explored.add(str(state.config))
        print("NODES=",nodes_expanded )
        if test_goal(state.config): 
            writeOutput(get_path(state), nodes_expanded)
            print("NODES_DONE=", nodes_expanded)
            return state
        
        for nb in state.expand(): 
            skip = False
            x = str(nb.config)
            if x in explored: 
               
                continue
            for ab in frontier: 
                if ab.config == nb.config: 
                    skip = True
                    break
            if skip == True: continue
            
            nb.parent = state
            frontier.append(nb)
         
    return False
    """
   

def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###
    pass

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###
    pass

def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###
    pass

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### STUDENT CODE GOES HERE ###
    return (puzzle_state == [n for n in range(len(puzzle_state))])


# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(config=begin_state, n=board_size)

    print("Running...")
    start_time  = time.time()
    final_state = None
    if   search_mode == "bfs": 
        final_state = bfs_search(hard_state)
    elif search_mode == "dfs": dfs_search(hard_state)
    elif search_mode == "ast": A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")
        
    end_time = time.time()
    print("Program completed in %.3f second(s)"%(end_time-start_time))
    #print(final_state)
    
    

if __name__ == '__main__':
    main()