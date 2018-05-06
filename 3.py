# 这道题的关键要点在于开始位置start的确定
# 判断起始字符串位置的更改需要满足两个条件：之前出现过，在start位置之后出现的


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sstring = {}
        result = start = 0
        for i in range(len(s)):
            if s[i] in sstring and start <= sstring[s[i]]:
                start = sstring[s[i]] + 1
            else:
                result = max(result, i-start+1)

            sstring[s[i]] = i

        return result
