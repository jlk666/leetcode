class TwoSum_listbased():
    def __init__(self) :
        self.num_list = []
    
    def add(self, number):
        self.num_list.append(number)
        index_num = len(self.num_list) -1
        while index_num > 0 and self.num_list[index_num -1] > self.num_list[index_num -1]:
            self.num_list[index_num -1], self.num_list[index_num] = self.num_list[index_num], self.num_list[index_num -1]
            index_num -= 1
            
    def find(self, target): #using two num pointers
        left = 0
        right = len(self.num_list)-1
        while left < right:
            if self.num_list[left] + self.num_list[right] == target:
                return True
            if self.num_list[left] + self.num_list[right] < target:
                left+=1
            if self.num_list[left] + self.num_list[right] > target:
                right-=1
        return False

class TwoSum_hashMapbased():
    def __init__(self) :
        self.num_hash = {}
        
    def add(self, number):
        self.num_hash[number] = self.num_hash.get(number, 0) + 1 # the 2nd parameter here, if there is no number in the hash, set the value to 0
    
    def find(self, target):
        for num1 in self.num_hash:
            num2 = target - num1
            num2_numberNeeded = 2 if num2 == num1 else 1
            if self.num_hash.get(num2, 0) >= num2_numberNeeded:
                return True
            
        return False
            
