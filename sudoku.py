import time
from tkinter import *
class Sudoku:

    def __init__(self):
        self.matrix = [[0 for x in range(9)] for x in range(9)]
        self.zero_list=[]

    def read_game_file(self, filename):
        #line = input()
        game_file = open("D:/Sudoku/"+filename)
        
        for i in range(9):
            line = game_file.readline()
            line = line.split()
            for j in range(9):
                self.matrix[i][j]=int(line[j])
                
        print (self.matrix)
        self.get_zero_list()
        return self.matrix

    def read_game_from_board(self, mat):
        self.matrix=mat
        print (self.matrix)
        self.get_zero_list()
        return self.matrix
    
    def detect_clash(self, i, j, val):
        for crawl_i in range(9):
            if self.matrix[i][crawl_i]==val:
                return -1

        for crawl_j in range(9):
            if self.matrix[crawl_j][j]==val:
                return -1

        for crawl_i in range(9):
            if self.matrix[i][crawl_i]==val:
                return -1

        block_i = int((i/3))*3
        block_j = int((j/3))*3

        for k in range(3):
            for l in range(3):
                if self.matrix[block_i+k][block_j+l]==val:
                    return -1
        
        return 1
    
            
    def get_zero_list(self):
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j]==0:
            
                    pair=[i,j]
                    self.zero_list.append(pair)
        print (self.zero_list)
                
    def solve_sudoku(self,index):
        
        if index >= len(self.zero_list):
            return 1
        
        for check_num in range(9):
            result = self.detect_clash(self.zero_list[index][0], self.zero_list[index][1], check_num+1)
            if result == 1:
                self.matrix[self.zero_list[index][0]][self.zero_list[index][1]]=check_num+1
                if self.solve_sudoku(index+1)==1:
                    return 1
                self.matrix[self.zero_list[index][0]][self.zero_list[index][1]]=0
        
        return -1

    def print_matrix(self):
        for i in range(9):
            print (self.matrix[i])

    def get_solved_matrix(self):
        return self.matrix


class Sudoku_GUI:

    def __init__(self, master):

        self.game = Sudoku()
        sudoku_box = Frame(master)
        sudoku_box.pack()

        frame = Frame(master)
        frame.pack()
        
        self.box=[[0 for x in range(9)] for x in range(9)]
        for i in range(9):
            for j in range(9):
                bgc ="white"
                if (int(i/3)+int(j/3))%2==0:
                    bgc="green"
                    fgc="red"
                self.box[i][j] = Text(sudoku_box, height=1, width=2, bg=bgc, fg=fgc)
                self.box[i][j].grid(row=i, column=j)
                
                
        
        
        self.button = Button(
            frame, text="Solve", fg="red", command=self.call_solve
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Press Me", command=self.say_hi)
        self.hi_there.pack(side=RIGHT)


    def call_solve(self):
        mat = [[0 for x in range(9)] for x in range(9)]
        for i in range(9):
            for j in range(9):
                val = self.box[i][j].get('1.0',END).replace("\n","")
                if val.isdigit():
                    if int(val)>=1&int(val)<=9:
                        mat[i][j]=int(val)

        self.game.read_game_from_board(mat)
        self.game.solve_sudoku(0)
        self.game.print_matrix()
        matri = self.game.get_solved_matrix()
        self.display_res(matri)
        
    def display_res(self, mat):
        
        for i in range(9):
            for j in range(9):
                val = self.box[i][j].get('1.0',END).replace("\n","")
                if val=='':
                    self.box[i][j]['foreground']="black"       
                    self.box[i][j].delete('0.0',END)
                    self.box[i][j].insert('0.0',str(mat[i][j]) )   
                
    def say_hi(self):
        print ("Fuck you motherfucker!")

root = Tk()


sudoku_obj = Sudoku()
'''
sudoku_obj.read_game_file("game2.sudoku")
'''
start = time.time()
'''
sudoku_obj.get_zero_list()
sudoku_obj.solve_sudoku(0)
'''
elapsed = (time.time() - start)
print (elapsed)
#sudoku_obj.print_matrix()

gui = Sudoku_GUI(root)

root.mainloop()
root.destroy()
