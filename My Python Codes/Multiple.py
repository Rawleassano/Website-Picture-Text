def solution(number):
    multiple = []

    for number in range(1, number):
        if number % 3 == 0:
            multiple.append(number)
        if number % 5 == 0:
            multiple.append(number)
    sum1 = sum(multiple)
    return sum1










    
