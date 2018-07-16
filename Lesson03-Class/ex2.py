import math

class Map:
    def set_map(self,n):
        self.map_list = [['*' for i in range(n)] for j in range(n)]
        self.map_size = n 

    def set_pattern(self,p):
        if (self.map_size%2) == 1 and p==1:
            center = math.floor(self.map_size/2)  #無條件捨取法
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
map = Map()
map.set_map(n)
map.display()
print()
map.set_pattern(p)
map.display()

