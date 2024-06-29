class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.Keyboard = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if not digits:
            return []
        recombinations = []
        self.dfs(digits, 0, [], recombinations)
        return recombinations
    
    def dfs(self, digits, index, combination, combinations):
        if index == len(digits):
            combinations.append(''.join(combination))
            return
        for letter in self.Keyboard[digits[index]]:
            combination.append(letter)
            self.dfs(digits, index + 1, combination, combinations)
            combination.pop()