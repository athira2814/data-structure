class Stack:
    def __init__(self,n):
        self.maxsize = n
        self.top = 0
        self.stack = []
    
    def push(self,data):
        if (self.top >= self.maxsize):
            print("stack overflow")
        else :
            self.top+=1
            self.stack.append(data)
            print( self.stack)

    def pop(self):
        if (self.top == 0):
            print("stack is empty")
        else:
            self.stack.pop()
            self.top-+1
            return self.stack

    def peek(self):
        return self.stack[-1]

    def display(self):
        return self.stack

if __name__ == "__main__" :
    s= Stack(5)
    while (True):

        print("1.push")
        print("2.pop")
        print("3.peek")
        print("4.display")
        print("5.quit")
        c = input("enter your choice")
        if(c == "1"):
            data = int (input("enter the ele"))
            s.push(data)
        elif (c == "2"):
            print(s.pop())
        elif (c == "3"):
            print(s.peek())
        elif (c == "4"):
            print(s.display())
        else:
            print("wrong choice")
