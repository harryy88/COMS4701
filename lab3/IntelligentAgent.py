
import random
from BaseAI import BaseAI
import sys
import math
import time

class IntelligentAgent(BaseAI):

    INF = 999999999999
    exponent = 1
    
    def getMove(self, grid):
    
        action = self.e_minimax(grid)
        if not action:
             random.choice(grid.getAvailableMoves())[1]
        return action 

	
    
    def e_minimax(self, grid):
       return (self.maxisize(grid, -self.INF, self.INF, 0))[0]
   
    
    def goal_state(slef, grid):
        return False
    
    def maxisize(self, grid, alpha, beta, rec_depth):
        
        if rec_depth > 4:
            return (None, self.evaluate(grid)) 
        
        max_child = None #direction
        max_util = -self.INF #
        
        for child in grid.getAvailableMoves(): #move
            cur_util = self.chance_node(child[1], alpha, beta, (rec_depth+1))
            
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

        if rec_depth > 4: #timeout 
             return (None, self.evaluate(grid))
             #return 20

        left = 0.9 * self.minisize(grid, 2, alpha, beta, (1+rec_depth))
        right = 0.1 * self.minisize(grid, 4, alpha, beta, (1+rec_depth))
        return (left + right) / 2
    
    
    
    def minisize(self, grid, node_value, alpha, beta, rec_depth):
        
        if rec_depth > 4: # or timeout
            #return 20
            return self.evaluate(grid)
            
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
    
    def evaluate(self, grid):
        self.exponent = math.ceil(grid.getMaxTile() / 2048)
        possible_merges = self.countPossibleMerges(grid)
        grid_value = self.calculateGridValue(grid)
        motonicity = self.monotonicity(grid) 
        open_tiles = math.pow(len(grid.getAvailableCells()), self.exponent)
        weights = [40, 200, 270, 500]
        """
        print("self.exponent", self.exponent)
        print("possible_merges", possible_merges)
        print("grid_value", grid_value)
        print("motonicity", motonicity)
        print("open_tiles", open_tiles)
        """
        score = 0
        score += weights[0]*grid_value 
        score += weights[1]*motonicity 
        score += weights[2]*possible_merges 
        score += weights[3]*open_tiles

        return score


    def monotonicity(self, grid):
        motonicity = 0	
        for row in range(3):
            for col in range(3):
                if grid.map[row][col] >= grid.map[row][col+1]:
                    motonicity += 1
                    if grid.map[col][row] >= grid.map[col][row+1]:
                        motonicity += 1
					
        return math.pow(motonicity, self.exponent)

    def calculateGridValue(self, grid):
        topLeft = [[128, 64, 16, 8], [32, 16, 8, 4], [16, 8, 4, 2], [8, 4, 2, 2]]
        count = 0
        for row in range(len(grid.map)):
            for col in range(len(grid.map[row])):
                count += topLeft[row][col] * grid.map[row][col]
        return math.pow(count, 2)
    
    def countPossibleMerges(self, grid):
        open_cells = len(grid.getAvailableCells())
        most_merges = 0
        for move in grid.getAvailableMoves():
            next_grid = move[1]
            next_open_cells = len(next_grid.getAvailableCells())
            most_merges += open_cells - next_open_cells
        return math.pow(most_merges, self.exponent)

    
    
    
    