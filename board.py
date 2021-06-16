class Board():
    # Gener board    

    def __init__(self,column=3,row=3):
        self.row = row
        self.column = column
        self.pole = []
        for iter_1 in range(row+1):
            self.pole.append([iter_1])
            for iter_2 in range(self.column):
                a = len(self.pole)-1
                b = self.pole[a]
                if a == 0:
                    self.pole[a].append('' + str(iter_2+1) + '')
                else:
                    self.pole[iter_1].append('-')
            # print(self.pole[iter_1])
    def pole_print(self):
        for iter in self.pole:
            print(iter)



        
# ob = Board()
# ob.pole_print()
