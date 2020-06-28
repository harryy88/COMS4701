
import random
from BaseAI import BaseAI
import sys
import math
import time

class IntelligentAgent(BaseAI):

    INF = 999999999999
    time_limit = None
    #start_time = time.process_time()
    def getMove(self, grid):
    
        self.time_limit = time.process_time() + .24
        action = self.e_minimax(grid)
        if not action:
             random.choice(grid.getAvailableMoves())[1]
        return action 

	
    
    def e_minimax(self, grid):
       return (self.maxisize(grid, -self.INF, self.INF, 0))[0]
   
    
    def goal_state(slef, grid):
        return False
    
    def maxisize(self, grid, alpha, beta, rec_depth):
        
        if rec_depth > 8 or time.process_time() >= self.time_limit:
            return (None, self.heuristic(grid)) 
        
        max_child = None #direction
        max_util = -self.INF #
        
        for child in grid.getAvailableMoves(): #move
            x = self.chance_node(child[1], alpha, beta, (rec_depth+1)) 
            cur_util = x
            if type(x) is tuple: 
              cur_util = x[1]
            
            if cur_util > max_util:
                max_util = cur_util 
                max_child = child[0]
                
            if max_util >= beta: 
                break
    
            if max_util > alpha: 
                alpha = max_util
        
        return max_child, max_util
        
        

    
    #here
    def chance_node(self, grid, alpha, beta, rec_depth):
        
        
        if rec_depth > 8 or time.process_time() >= self.time_limit: #timeout 
             return (None, self.heuristic(grid))
             #return 20

        left = 0.9 * self.minisize(grid, 2, alpha, beta, (1+rec_depth))
        right = 0.1 * self.minisize(grid, 4, alpha, beta, (1+rec_depth))
        return ((left + right) / 2)
    
    
    
    def minisize(self, grid, node_value, alpha, beta, rec_depth):
    
        if rec_depth > 8 or time.process_time() >= self.time_limit:
            #return 20
            return self.heuristic(grid)
            
        min_child = None
        min_util = self.INF
        
        for child in grid.getAvailableCells():
            
            temp_board = grid.clone()
            temp_board.insertTile(child, node_value)
            
            
            cur_util = self.maxisize(temp_board, alpha, beta, (rec_depth + 1))
            if (cur_util[1] < min_util):
                min_util = cur_util[1]
                
            if min_util <= beta: #or time limit 
                break    
            
            if min_util < beta: 
                beta = min_util
                
        return min_util
       
    # start
    """
    def heuristic(self, grid):
  
        score = 0
      
        for col in grid.map:
            for cell in col:
                if cell == 0:
                    score += 1
        #print("ZERO SCORE = ", score)

        mono = self.monotonicity(grid) 
       # print("MONO SCORE = ", mono)
        score += mono
        
        grid_value = self.calculateGridValue(grid)
        #print("Grid SCORE = ", grid_value)
        score += grid_value
       # end = time.process_time() 
       # print("TOTAL = ", end - self.start_time)
        return score

    """
    def heuristic(self, grid):
  
        score = 0
      
        for col in grid.map:
            for cell in col:
                if cell == 0:
                    score += 1
        #print("ZERO SCORE = ", score)

        
        motonicity = 0	
        for row in range(3):
            for col in range(3):
                if grid.map[row][col] >= grid.map[row][col+1]:
                    motonicity += 1
                    if grid.map[col][row] >= grid.map[col][row+1]:
                        motonicity += 1
					
       # print("MONO SCORE = ", mono)
        score += motonicity
        
        #grid_value = self.calculateGridValue(grid)
        
        
        count = 0
   
        for row in range(len(grid.map)):
            for col in range(len(grid.map[row])):
                
                
                if col == 0: 
                    if row == 0: 
                        count += 20 * grid.map[row][col]
                    elif row == 1: 
                        count += 10 * grid.map[row][col]
                    elif row == 2: 
                        count += 5 * grid.map[row][col]
                    elif row == 3: 
                        count += 2 * grid.map[row][col]
                        
                elif col == 1: 
                    if row == 0: 
                        count += 7 * grid.map[row][col]
                    elif row == 1: 
                        count += 5 * grid.map[row][col]
                    elif row == 2: 
                        count += 2 * grid.map[row][col]
                    elif row == 3: 
                        count += 1 * grid.map[row][col]
                elif col == 2: 
                    if row == 0: 
                        count += 5 * grid.map[row][col]
                    elif row == 1: 
                        count += 2 * grid.map[row][col]
                    elif row == 2: 
                        count += 1 * grid.map[row][col]
                    elif row == 3: 
                        count += .5 * grid.map[row][col]
                elif col == 3: 
                    if row == 0: 
                        count += 1 * grid.map[row][col]
                    elif row == 1: 
                        count += 1 * grid.map[row][col]
                    elif row == 2: 
                        count += .5 * grid.map[row][col]
                    elif row == 3: 
                        count += .2 * grid.map[row][col]
                
                
        
        
        #print("Grid SCORE = ", grid_value)
        #score += grid_value
        score += count
       # end = time.process_time() 
       # print("TOTAL = ", end - self.start_time)
        return score

    """
    def monotonicity(self, grid):
        motonicity = 0	
        for row in range(3):
            for col in range(3):
                if grid.map[row][col] >= grid.map[row][col+1]:
                    motonicity += 1
                    if grid.map[col][row] >= grid.map[col][row+1]:
                        motonicity += 1
					
        return motonicity
    """
    """
    def calculateGridValue(self, grid):
        #topLeft = [[128, 64, 16, 8], [32, 16, 8, 4], [16, 8, 4, 2], [8, 4, 2, 2]]
        
       # topLeft = [[20, 10, 5, 2], [7, 5, 2, 1], [5, 2, 1, 0], [1, 1, 0, 0]]
    """
    """
        count = 0
        for row in range(len(grid.map)):
            for col in range(len(grid.map[row])):
                count += topLeft[row][col] * grid.map[row][col]
        return count
    """
    """
        count = 0
   
        for row in range(len(grid.map)):
            for col in range(len(grid.map[row])):
                
                
                if col == 0: 
                    if row == 0: 
                        count += 20 * grid.map[row][col]
                    elif row == 1: 
                        count += 10 * grid.map[row][col]
                    elif row == 2: 
                        count += 5 * grid.map[row][col]
                    elif row == 3: 
                        count += 2 * grid.map[row][col]
                        
                elif col == 1: 
                    if row == 0: 
                        count += 7 * grid.map[row][col]
                    elif row == 1: 
                        count += 5 * grid.map[row][col]
                    elif row == 2: 
                        count += 2 * grid.map[row][col]
                    elif row == 3: 
                        count += 1 * grid.map[row][col]
                elif col == 2: 
                    if row == 0: 
                        count += 5 * grid.map[row][col]
                    elif row == 1: 
                        count += 2 * grid.map[row][col]
                    elif row == 2: 
                        count += 1 * grid.map[row][col]
                    elif row == 3: 
                        count += .5 * grid.map[row][col]
                elif col == 3: 
                    if row == 0: 
                        count += 1 * grid.map[row][col]
                    elif row == 1: 
                        count += 1 * grid.map[row][col]
                    elif row == 2: 
                        count += .5 * grid.map[row][col]
                    elif row == 3: 
                        count += .2 * grid.map[row][col]
                
                
        
        return count
    """
    """
        topLeft = [[128, 64, 16, 8], [32, 16, 8, 4], [16, 8, 4, 2], [8, 4, 2, 2]]
        count = 0
        for row in range(len(grid.map)):
            for col in range(len(grid.map[row])):
                count += topLeft[row][col] * grid.map[row][col]
        return math.pow(count, 2)
    """
 
    
    
    