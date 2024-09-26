# LeetCode class method
#class Solution:
#    def reverseString(self, s: List[str]) -> None:
#        for i in range(len(s)//2):
#            firstValue = s[i]
#            s[i] = s[-1-i]
#            s[-1-i] = firstValue

# Normal function definition
def reverseString(s):
    for i in range(len(s)//2):
        firstValue = s[i]
        s[i] = s[-1-i]
        s[-1-i] = firstValue

# Test
test = ['t', 'e', 's', 't']
reverseString(test)
print(test)
