def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list2 = list1[n:]
    m = len(list2)
    i = 0
    list3 = []
    while i < m:
        list3.append(list2.pop())
        i += 1
    return list3
print(main(['a', 'b', 'c', 'd', 'e', 'f'],3))