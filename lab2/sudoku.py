#!/usr/bin/env python
#coding:utf-8
import sys

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)



class Node(object):
   def __init__(self, key):
        self.key = key    #A1
        self.val = 0    #4
        
   def add_something(self, x):
       self.val += x
   def __gt__(self, other): 
       return self.val > other.val
   
def find_constraints(node, csp):
    
    row = str(node.key[0]) #A
    col = str(node.key[1]) #'2'
    
    legal = [1,2,3,4,5,6,7,8,9]
    actions = set()
    # ROW CONTS
    for i in range(1,10):
        if csp[row + str(i)] != 0: 
            actions.add(csp[row + str(i)])
      
    # COL CONTS
    for r in ['A','B','C','D','E','F','G','H','I']:
        if csp[r+ col] != 0: 
            actions.add(csp[r+ col])
    
    
    
    # BOX CONTS
    if (col == "1" or col == "2" or col == "3"): 
        if (row >= "A" and row <= "C"): 
            box = 1
        elif (row >= "D" and row <= "F"):
            box = 4
        else: box = 7
    elif col == '4' or col == '5' or col == '6': 
        if (row >= "A" and row <= "C"): 
            box = 2
        elif (row >= "D" and row <= "F"):
            box = 5
        else: box = 8
    else: 
        if (row >= "A" and row <= "C"): 
            box = 3
        elif (row >= "D" and row <= "F"):
            box = 6
        else: box = 9
    
    if box == 1:
        actions.add(csp['A1'])
        actions.add(csp['A2'])
        actions.add(csp['A3'])
        actions.add(csp['B1'])
        actions.add(csp['B2'])
        actions.add(csp['B3'])
        actions.add(csp['C1'])
        actions.add(csp['C2'])
        actions.add(csp['C3'])
    elif box == 2:
       actions.add(csp['A4'])
       actions.add(csp['A5'])
       actions.add(csp['A6'])
       actions.add(csp['B4'])
       actions.add(csp['B5'])
       actions.add(csp['B6'])
       actions.add(csp['C4'])
       actions.add(csp['C5'])
       actions.add(csp['C6'])
    elif box == 3:
        actions.add(csp['A7'])
        actions.add(csp['A8'])
        actions.add(csp['A9'])
        actions.add(csp['B7'])
        actions.add(csp['B8'])
        actions.add(csp['B9'])
        actions.add(csp['C7'])
        actions.add(csp['C8'])
        actions.add(csp['C9'])
    elif box == 4:
        actions.add(csp['D1'])
        actions.add(csp['D2'])
        actions.add(csp['D3'])
        actions.add(csp['E1'])
        actions.add(csp['E2'])
        actions.add(csp['E3'])
        actions.add(csp['F1'])
        actions.add(csp['F2'])
        actions.add(csp['F3'])
    elif box == 5:
        actions.add(csp['D4'])
        actions.add(csp['D5'])
        actions.add(csp['D6'])
        actions.add(csp['E4'])
        actions.add(csp['E5'])
        actions.add(csp['E6'])
        actions.add(csp['F4'])
        actions.add(csp['F5'])
        actions.add(csp['F6'])
    elif box == 6:
        actions.add(csp['D7'])
        actions.add(csp['D8'])
        actions.add(csp['D9'])
        actions.add(csp['E7'])
        actions.add(csp['E8'])
        actions.add(csp['E9'])
        actions.add(csp['F7'])
        actions.add(csp['F8'])
        actions.add(csp['F9'])
    elif box == 7:
        actions.add(csp['G1'])
        actions.add(csp['G2'])
        actions.add(csp['G3'])
        actions.add(csp['H1'])
        actions.add(csp['H2'])
        actions.add(csp['H3'])
        actions.add(csp['I1'])
        actions.add(csp['I2'])
        actions.add(csp['I3'])
    elif box == 8:
        actions.add(csp['G4'])
        actions.add(csp['G5'])
        actions.add(csp['G6'])
        actions.add(csp['H4'])
        actions.add(csp['H5'])
        actions.add(csp['H6'])
        actions.add(csp['I4'])
        actions.add(csp['I5'])
        actions.add(csp['I6'])
    elif box == 9:
        actions.add(csp['G7'])
        actions.add(csp['G8'])
        actions.add(csp['G9'])
        actions.add(csp['H7'])
        actions.add(csp['H8'])
        actions.add(csp['H9'])
        actions.add(csp['I7'])
        actions.add(csp['I8'])
        actions.add(csp['I9'])        
    
    for n in actions:
        try:
            legal.remove(n)
        except:
            continue
        
    return len(legal)
       
def get_next(csp):

    """
    for key in csp: 
        if csp[val] == 0:
            return val
    return False
    """
    potential_next = []
    for val in csp: 
        if csp[val] == 0:
            node = Node(val)
            constr = find_constraints(node, csp)
            node.val = constr
            potential_next.append(node)
            
    
    if len(potential_next) == 0: 
         return False
    least_contraining = min(potential_next)
            
    return least_contraining.key

#A1 3 board
def legal(val, try_value, csp):
    
    row = val[0] #A
    col = str(val[1]) #'2'
    
    #check row
    for i in range(1,10):
        if csp[row + str(i)] == try_value: return False
    # check col 
    for r in ['A','B','C','D','E','F','G','H','I']:
        if csp[r+ col] == try_value: return False
    #check box 
    box = None
    if (col == "1" or col == "2" or col == "3"): 
        if (row >= "A" and row <= "C"): 
            box = 1
        elif (row >= "D" and row <= "F"):
            box = 4
        else: box = 7
    elif col == '4' or col == '5' or col == '6': 
        if (row >= "A" and row <= "C"): 
            box = 2
        elif (row >= "D" and row <= "F"):
            box = 5
        else: box = 8
    else: 
        if (row >= "A" and row <= "C"): 
            box = 3
        elif (row >= "D" and row <= "F"):
            box = 6
        else: box = 9
    

    if box == 1:
        v = try_value
        if (csp["A1"] == v or csp["A2"] == v or csp["A3"] == v or csp["B1"] == v or csp["B2"] == v or csp["B3"] == v or csp["C1"] == v or csp["C2"] == v or csp["C3"] == v):
            return False
        return True
    if box == 2:
        v = try_value
        if csp["A4"] == v or csp["A5"] == v or csp["A6"] == v or csp["B4"] == v or csp["B5"] == v or csp["B6"] == v or csp["C4"] == v or csp["C5"] == v or csp["C6"] == v:
            return False
        return True
    if box == 3:
        v = try_value
        if csp["A7"] == v or csp["A8"] == v or csp["A9"] == v or csp["B7"] == v or csp["B8"] == v or csp["B9"] == v or csp["C7"] == v or csp["C8"] == v or csp["C9"] == v:
            return False
        return True
    if box == 4:
        v = try_value
        if csp["D1"] == v or csp["D2"] == v or csp["D3"] == v or csp["E1"] == v or csp["E2"] == v or csp["E3"] == v or csp["F1"] == v or csp["F2"] == v or csp["F3"] == v:
            return False
        return True
    if box == 5:
        v = try_value
        if csp["D4"] == v or csp["D5"] == v or csp["D6"] == v or csp["E4"] == v or csp["E5"] == v or csp["E6"] == v or csp["F4"] == v or csp["F5"] == v or csp["F6"] == v:
            return False
        return True
    if box == 6:
        v = try_value
        if csp["D7"] == v or csp["D8"] == v or csp["D9"] == v or csp["E7"] == v or csp["E8"] == v or csp["E9"] == v or csp["F7"] == v or csp["F8"] == v or csp["F9"] == v:
            return False
        return True
    if box == 7:
        v = try_value
        if csp["G1"] == v or csp["G2"] == v or csp["G3"] == v or csp["H1"] == v or csp["H2"] == v or csp["H3"] == v or csp["I1"] == v or csp["I2"] == v or csp["I3"] == v:
            return False
        return True
    if box == 8:
        v = try_value
        if csp["G4"] == v or csp["G5"] == v or csp["G6"] == v or csp["H4"] == v or csp["H5"] == v or csp["H6"] == v or csp["I4"] == v or csp["I5"] == v or csp["I6"] == v:
            return False
        return True
    if box == 9:
        v = try_value
        if csp["G7"] == v or csp["G8"] == v or csp["G9"] == v or csp["H7"] == v or csp["H8"] == v or csp["H9"] == v or csp["I7"] == v or csp["I8"] == v or csp["I9"] == v:
            return False
        return True
        
    
def backtrack(assignment, csp):
   
    val = get_next(csp)

    if val == False: return True
    
    for try_value in range(1, 10):
        if legal(val, try_value, csp) == True: 
            csp[val] = try_value
            if (backtrack(assignment,csp)) == True:
                return True
            csp[val] = 0

    return False
 

def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    solved_board = backtrack([], board)
   
   # print(board_to_string(board))
    #print(print_board(board))
    return solved_board


if __name__ == '__main__':

    if len(sys.argv) > 1:

        #  Read individual board from command line arg.
        sudoku = sys.argv[1]

        if len(sudoku) != 81:
            print("Error reading the sudoku string %s" % sys.argv[1])
        else:
            board = { ROW[r] + COL[c]: int(sudoku[9*r+c])
                      for r in range(9) for c in range(9)}
            
            print_board(board)

           # start_time = time.time()
            solved_board = backtracking(board)
           # end_time = time.time()
            #print("TIME = ", end_time-start_time )

            #print(board_to_string(board))

            out_filename = 'output.txt'
            outfile = open(out_filename, "w")
            outfile.write(board_to_string(board))
            outfile.write('\n')

    else:

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                    for r in range(9) for c in range(9)}

            # Print starting board.
            #print_board(board)

            # Solve with backtracking
            #start_time = time.time()
            solved_board = backtracking(board)
           # end_time = time.time()
           # print("TIME = ", end_time-start_time )

            # Print solved board. 
            print("-------", board_to_string(board))

            # Write board to file
            outfile.write(board_to_string(board))
            outfile.write('\n')

        print("Finishing all boards in file.")
        outfile.close()
        import datetime
        print(datetime.datetime.now())
        
        
        