class Board():
    # Gener board    

    def pole_games(self,column,row):
        self.row = row
        self.column = column
        self.pole = []
        for iter_1 in range(row):
            self.pole.append([])
            for iter_2 in range(self.column):
                self.pole[iter_1].append('-')
            print(self.pole[iter_1])
        # for i in self.pole:
        #     print(i)

        # for item_1 in range(1,self.summa_column_row+1,self.column):
        #     print(self.summa_column_row)
        #     self.pole.append([item_1])
            
        #     for item_2 in range(1,self.column+1):
        #         print(item_2)
        # print(self.pole)
