def mysum(*numbers):
    result = 0
    for number in numbers:
        #result = result + number
        result += number
    
    return result

print(mysum(1, 2, 3, 10))
