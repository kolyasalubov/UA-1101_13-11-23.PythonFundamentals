def solution(number):
    num_list = []
    if number > 0:
        for x in range(1, number):
            if x % 3 == 0 and x % 5 == 0:
                num_list.append(x)
            elif x % 3 == 0:
                num_list.append(x)
            elif x % 5 == 0:
                num_list.append(x)
        return sum(num_list)
    return 0
