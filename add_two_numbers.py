# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    tmp_a = l1
    tmp_b = l2
    tmp_c = l3 = ListNode(0)
    pos = 0  # 默认进位标志为0
    while tmp_a.next != None or tmp_b.next != None:

        # l1的遍历已到最后1个节点，而l2还剩多于1个
        if tmp_a.next == None:
            sum = tmp_a.val + tmp_b.val + pos
            tmp_c.val = sum % 10
            pos = sum // 10
            tmp_a.val = 0
            # tmp_a = ListNode(0)
            tmp_b = tmp_b.next
            # tmp_c = tmp_c.next = ListNode(0)
            tmp_c.next = ListNode(0)
            tmp_c = tmp_c.next
            while tmp_b.next != None:
                sum = tmp_b.val + pos
                pos = sum // 10
                tmp_c.val = sum % 10
                tmp_b = tmp_b.next
                # tmp_c = tmp_c.next = ListNode(0)
                tmp_c.next = ListNode(0)
                tmp_c = tmp_c.next

        # l2的遍历已到最后1个节点，而l1还剩多于1个
        elif tmp_b.next == None:
            sum = tmp_a.val + tmp_b.val + pos
            tmp_c.val = sum % 10
            pos = sum // 10
            tmp_b.val = 0
            # tmp_b = ListNode(0)
            tmp_a = tmp_a.next
            # tmp_c = tmp_c.next = ListNode(0)
            tmp_c.next = ListNode(0)
            tmp_c = tmp_c.next
            while tmp_a.next != None:
                sum = tmp_a.val + pos
                pos = sum // 10
                tmp_c.val = sum % 10
                tmp_a = tmp_a.next
                tmp_c.next = ListNode(0)
                tmp_c = tmp_c.next

        # 在l1和l2节点数还一样多的情况下
        else:
            val_a = tmp_a.val
            val_b = tmp_b.val
            sum = val_a + val_b + pos
            tmp_c.val = sum % 10
            # 为下一循环修改的变量值
            pos = sum // 10
            tmp_a = tmp_a.next
            tmp_b = tmp_b.next
            tmp_c.next = ListNode(0)
            tmp_c = tmp_c.next

    sum = tmp_a.val + tmp_b.val + pos
    tmp_c.val = sum % 10
    if (sum // 10) == 0:
        tmp_c.next = None
    else:
        tmp_c.next = ListNode(1)

    return l3

# 节点到整数
# return::int
def node_2_num(node):
    tmp = node
    sum = 0
    pos = 1
    while tmp.next != None:
        sum = sum + tmp.val * pos
        pos = pos * 10
        tmp = tmp.next
    sum = sum + tmp.val * pos
    return sum

# 整数到节点
# return::ListNode()
def num_2_node(num):
    tmp = num
    tmpN = N = ListNode(0)
    while tmp // 10 != 0 :
        val = tmp % 10
        tmp = tmp // 10
        tmpN.val = val
        tmpN.next = ListNode(0)
        tmpN = tmpN.next
    tmpN.val = tmp
    return N

# 打印节点
def print_node(node):
    tmp = node
    while tmp.next != None:
        print(tmp.val)
        tmp = tmp.next
    print(tmp.val)
    print("----------------  over  -----------------")


if __name__ == '__main__':
    d = num_2_node(34567)
    e = num_2_node(4)
    de = add_two_numbers(d,e)
    print(node_2_num(de))
    print_node(de)
