#https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
                break
        if letters[n-1]<= target:
            return letters[0]