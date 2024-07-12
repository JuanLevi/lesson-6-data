

class Stack():
    def __init__(self,length):
        self.max=length
        self.stack=[]
        self.size=len(self.stack)
    
    def push(self,value):
        if len(self.stack)<self.max:
            self.stack.append(value)
        else:
            print('The stack is already full')

    def pop(self):
        if len(self.stack)>0:
            self.stack.pop(self.size-1)
        else:
            print('The stack is empty')

    def peek(self):
        if len(self.stack)>0:
            print(self.stack[self.size-1])
        else:
            print('The stack is empty')        

    def IsEmpty(self):
        if len(self.stack)==0:
            print('The stack is empty')
        else:
            print('The stack is not empty')

    def IsFull(self):
        if len(self.stack)==self.max:
            print('The stack is full')
        else:
            print('The stack is not full')

s=Stack(5)

s.push(3)
s.push(4)
s.push(7)
print(s.stack)


s.pop()
print(s.stack)


s.peek()


s.push(8)
s.push(9)
s.push(10)
print(s.stack)

s.IsFull()


s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print(s.stack)
s.IsEmpty()