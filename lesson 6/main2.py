stack=[]
open=['(','[','{']
close=[')',']','}']
print(close.index('}'))

inputEq=input("Insert the equation: ")

def check(inputEq):
    stack=[]

    for character in inputEq:
        print(character)
        if character in open:
            stack.append(character)
        elif character in close:
            pos=close.index(character)
            if len(stack)>0:
                if open[pos]==stack[-1]:
                    stack.pop()
                else:
                    return "unbalanced"
                
    if len(stack)==0:
        return "balanced"
    
    else:
        return "unbalanced"
    

print(check(inputEq))
