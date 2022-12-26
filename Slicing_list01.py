def main(numbers):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    num1 = []
    i = 0
    while len(numbers) > i:
        if i%2 == 0:
            num1.append(numbers[i])
        i+=1

    return num1
