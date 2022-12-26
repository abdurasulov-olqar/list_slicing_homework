def main(list1):
    """
    A list of several elements is given. Reverse this list.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    m = len(list1)
    i = 0
    list2 = []
    while i < m:
        list2.append(list1.pop())
        i += 1
    return list2