def solution(number):
    i = 0
    y = 0
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            y = y + i
            i += 1
        else:
            i+=1
    return y
    
