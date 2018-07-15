import math

class Map:
    def __init__(self,n,p): #建立instance object時，自動執行。
        self.map_list = [['*' for i in range(n)] for j in range(n)]
        self.map_size = n 

        if (self.map_size%2) == 1 and p==1:        
            center = math.floor(self.map_size/2) 
            self.map_list[center][center-1] = 0
            self.map_list[center-1][center-1] = 0
            self.map_list[center-1][center] = 0
            self.map_list[center-1][center+1] = 0
            self.map_list[center+1][center] = 0

    def display(self):
        for i in range(self.map_size):
            for j in range(self.map_size):
                print(self.map_list[i][j], end = ' ')
            print()

n= int(input("Please enter number："))
p = int(input("Please enter number 1 to set pattern：")) 
map = Map(n,p)

map.display()



