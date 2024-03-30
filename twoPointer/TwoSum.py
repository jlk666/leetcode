class TwoSum():
    def __init__(self) :
        self.num_list = []
    
    def add(self, number):
        self.num_list.append(number)
        index_num = len(self.num_list) -1
        while index_num > 0 and self.num_list[index_num -1] > self.num_list[index_num -1]:
            self.num_list[index_num -1], self.num_list[index_num] = self.num_list[index_num], self.num_list[index_num -1]
            index_num -= 1
            
             