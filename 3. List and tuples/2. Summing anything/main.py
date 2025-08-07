def mysum(*args):
    if not args:
        return args
    
    output = args[0]
    
    for element in args[1:]:
        output += element
    
    return output

print(mysum())