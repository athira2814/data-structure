class Stack:
    def __init__(self,n):
        self.maxsize = n
        self.top = 0
        self.stack = []
    
    def push(self,data):
        if (self.top >= self.maxsize):
            print("Stack Overflow")
        else :
            self.top+=1
            self.stack.append(data)
            print( self.stack)

    def pop(self):
        if (self.stack == []):
            print("Stack Underflow")
        else:
            self.stack.pop()
            self.top-=1
            print (self.stack)

    def peek(self):
        return self.stack[-1]

    def display(self):
        return self.stack

if __name__ == "__main__" :
    s= Stack(5)
    while (True):

        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Quit")
        c = input("Enter your choice :")
        if(c == "1"):
            data = int (input("Enter an element :"))
            s.push(data)
        elif (c == "2"):
            s.pop()
        elif (c == "3"):
            print(s.peek())
        elif (c == "4"):
            print(s.display())
        elif (c == "5"):
            print("Thank You!!")
            break
        else:
            print("wrong choice")
