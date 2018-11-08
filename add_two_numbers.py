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
            tmp_b = tmp_b.next
            tmp_c = tmp_c.next = ListNode(0)
            while tmp_b.next != None:
                sum = tmp_b.val + pos
                pos = sum // 10
                tmp_c.val = sum % 10
                tmp_b = tmp_b.next
                tmp_c = tmp_c.next = ListNode(0)

        # l2的遍历已到最后1个节点，而l1还剩多于1个
        if tmp_b.next == None:
            sum = tmp_a.val + tmp_b.val + pos
            tmp_c.val = sum % 10
            pos = sum // 10
            tmp_b.val = 0
            tmp_a = tmp_a.next
            tmp_c = tmp_c.next = ListNode(0)
            while tmp_a.next != None:
                sum = tmp_a.val + pos
                pos = sum // 10
                tmp_c.val = sum % 10
                tmp_a = tmp_a.next
                tmp_c = tmp_c.next = ListNode(0)

        # 在l1和l2节点数还一样多的情况下
        val_a = tmp_a.val
        val_b = tmp_b.val
        sum = val_a + val_b + pos
        tmp_c.val = sum % 10
        # 为下一循环修改的变量值
        pos = sum // 10
        tmp_a = tmp_a.next
        tmp_b = tmp_b.next
        tmp_c = tmp_c.next = ListNode(0)

    sum = tmp_a.val + tmp_b.val + pos
    tmp_c.val = sum % 10
    if (sum // 10) == 0:
        tmp_c.next = None
    else:
        tmp_c.next = ListNode(1)

    return l3


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


def print_node(node):
    tmp = node
    while tmp.next != None:
        print(tmp.val)
        tmp = tmp.next
    print(tmp.val)
    print("------------------------------------")



if __name__ == '__main__':
    print("hello world")
    a1 = ListNode(1)
    a2 = a1.next = ListNode(3)
    a3 = a2.next = ListNode(5)
    a3.next = ListNode(7)

    b1 = ListNode(2)
    b2 = b1.next = ListNode(4)
    b3 = b2.next = ListNode(6)
    b3.next = ListNode(8)

    a_num = node_2_num(a1)
    print("a:", a_num)
    print_node(a1)

    b_num = node_2_num(b1)
    print("b:", b_num)
    print_node(b1)

    c1 = add_two_numbers(a1, b1)
    c_num = node_2_num(c1)
    print("c:", c_num)
    print_node(c1)