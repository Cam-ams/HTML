#!/usr/bin/env python3

import os
import time
import random
import platform

def random_boolean(prob):
    return random.random() <= prob

def to_string(game_of_life):
    s = "┌" + ("─" * (game_of_life.width * 2)) + "┐\n"
    for y in range(game_of_life.height):
        s += "│"
        for x in range(game_of_life.width):
            if game_of_life.grid[y][x]:
                s += "▓▓"
            else:
                s += "  "
        s += "│\n"
    s += "└" + ("─" * (game_of_life.width * 2)) + "┘\n"
    return s

def play(obj):
    is_windows = platform.system() == "Windows"
    print(to_string(obj))
    input("Press Enter to start")
    while True:
        if is_windows:
            os.system("cls")
        else:
            os.system("clear")

        print(to_string(obj))
        obj.update()
        time.sleep(0.05)




## TP - DJENID CAMELIA






class GameOfLine():
    def __init__(self, width, height):
        self.width= width
        self.height= height
        
        self.grid = []
        
        prob_alive = 0.45

        for i in range(height):
            ligne=[]
            for j in range(width):
                ligne.append(random_boolean(prob_alive))
            self.grid.append(ligne)

         
        

    def is_alive(self,x,y):  ## ici je voulais retourner la valeur TRUE ou FALSE ici le prbl est que l'index on le depasse cz qui retourne une erreur
        self.y = y # le but etait de prendre les coordones d'une cellule
        self.x = x # si elle est vivante on retournev TRUE si non elle est mort ou horrs du champs donc on retourne FALSE
        if y > self.height and x> self.width:
            self.grid[self.y][self.x] = False

        if  self.grid[y][x] == True : ## il n'aime pas le [x] 
            self.grid[self.y][self.x] = True
        
        else : self.grid[self.y][self.x]= False

        return self.grid[self.y][self.x]        



    
    def set_cell(self,x,y):
        if self.grid[y][x]== False:
            self.grid[y][x]= True
        return self.grid[y][x]
            
    
    
    def update(self): 
        new_gridn = []
        for i in range(len(self.grid)):
            ligne=[]
            for j in range(len(self.grid[i])):
        
                vivantes= 0               
                if self.is_alive(j-1, i-1) == True :
                    vivantes = vivantes + 1

                if self.is_alive(j,i-1) == True : 
                    vivantes = vivantes + 1

                if self.is_alive(j+1,i-1) == True  :
                    vivantes = vivantes + 1

                if self.is_alive(j-1,i) == True :
                        vivantes = vivantes + 1

                if self.is_alive(j+1,i) == True  :
                    vivantes = vivantes + 1

                if self.is_alive(j-1,i+1) == True :
                    vivantes = vivantes + 1

                if self.is_alive(j,i+1) == True :
                    vivantes = vivantes + 1

                if self.is_alive(j+1,i+1) == True  :
                    if self.grid[i+1][j+1] == True:
                        vivantes = vivantes + 1

                if vivantes >= 2:
                   if vivantes == 2 or vivantes == 3 :
                       val_cellule = True
                   if vivantes > 3:
                       val_cellule = True
                   if val_cellule == 3:
                       val_cellule=0
                else : 
                   val_cellule=False
    
            ligne.append(val_cellule)
        new_gridn.append(ligne)
        self.grid =new_gridn
        

    def  block (self,x,y):
        self.set_cell(x,y)
        self.set_cell(x+1,y)
        self.set_cell(x,y+1)
        self.set_cell(x+1,y+1)

    def blinker(self,x,y):
        self.set_cell(x,y)
        self.set_cell(x+1,y)
        self.set_cell(x,y+1)
        self.set_cell(x+1,y+1)

    
    def glider(self,x,y):
        self.set_cell(x+1,y)
        self.set_cell(x+1,y+2)
        self.set_cell(x,y+2)
        self.set_cell(x+2,y+2)
        self.set_cell(x+2,y+1)
    
    def beacon(self,x,y):
        self.set_cell(x,y)
        self.set_cell(x+2,y+2)

            
tes= GameOfLine(5,5)
tes.set_cell(2,3)
play(tes)