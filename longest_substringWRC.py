class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        P = 0
        max = 0
        while P < len_s :
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


def hash_func(s):
    Hp = 0  # 头指针
    Tp = 0  # 尾指针
    max = 0
    D = dict()

    while Tp < len(s) :
        if s[Tp] in D :
            TmpIndex = D[s[Tp]]
            if TmpIndex >= Hp :
                Hp = TmpIndex + 1
            else :
                D[s[Tp]] = Tp
                tmp_max = Tp - Hp + 1
                max = bigger(max, tmp_max)
                Tp = Tp + 1
        else:
            D[s[Tp]] = Tp   # 把新字母加入字典中
            tmp_max = Tp - Hp + 1
            max = bigger(max, tmp_max)
            Tp = Tp + 1
    return max


def bigger(a,b) :
    if a >= b :
        return a
    else :
        return b


if __name__ == '__main__':
    max = hash_func("abcdefghisdflkajoesdfa")
    print(max)