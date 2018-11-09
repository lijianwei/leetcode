class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        P = 0
        max = 1
        while P < (len_s - 1):
            tmp = P
            ua = set()  # 利用set 无序 不重复数据结构
            while tmp < len_s:
                if s[tmp] in ua:
                    break
                else:
                    ua.add(s[tmp])
                tmp = tmp + 1
            # print("set:", ua)
            new_max = len(ua)
            if max >= new_max:
                pass
            else:
                max = new_max
            P = P + 1
        return max

if __name__ == '__main__':
    S = Solution()
    max = S.lengthOfLongestSubstring("helloworld")
    print(max)