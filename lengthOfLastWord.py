# LeetCode class method
#class Solution:
#    def lengthOfLastWord(self, s: str) -> int:
#        return len(s.strip().split(' ')[-1])

# Normal function definition
def lengthOfLastWord(s):
    return len(s.strip().split(' ')[-1])

print(lengthOfLastWord('the length here should be four'))
