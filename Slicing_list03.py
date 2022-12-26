def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    m = len(list1)
    i = 0
    list2 = []
    while i < m:
        list2.append(list1[(i+1)*(-1)])
        i += 1
    return list1+list2

print(main([1,2,3]))