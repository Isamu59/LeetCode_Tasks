class Solution:
    def plusOne(self, digits):
        s = ''
        dig2 = []
        for i in range(len(digits)):
            s += str(digits[i])
        temp = str(int(s) + 1)
        
        for j in range(len(temp)):
            dig2.append(int(temp[j]))
        return dig2
        