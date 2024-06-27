class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        Keyboard = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    def dfs(self, digits, index, path, res):
        if index == len(digits):
            res.append(path)
            return
        for letter in self.dict[digits[index]]:
            path.append(letter)
            self.dfs(digits, index + 1, path , res)
            path.pop()