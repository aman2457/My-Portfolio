class StackNode:
    def __init__(self,data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
            return True if self.top == None else False
    
    def push(self,data):
        newNode = StackNode(data)
        newNode.next = self.top
        self.top = newNode
        #print("{} is pushed".format(data))
        
    def pop(self):
        if (self.isEmpty()):
            return float('-inf')
        
        temp = self.top
        self.top = self.top.next
        
        return temp.data
    
    def peek(self):
        if (self.isEmpty()):
            return float('-inf')
        
        else:
            return self.top.data

def infixToPostFix(infixexp):
        precedence = {'*':3, '/':3, '+':2, '-':2, '(':1}
        opStack = Stack()
        varList = infixexp.split()
        postfixExp = []
        
        for var in varList:
            if var in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or var in "0123456789":
                postfixExp.append(var)
            
            elif var == '(':
                opStack.push(var)
                
            elif var == ')':
                topVar = opStack.pop()
                while topVar != '(':
                    postfixExp.append(topVar)
                    topVar = opStack.pop()
            
            else:
                while (not opStack.isEmpty()) and (precedence[opStack.peek()] >= precedence[var]):
                    postfixExp.append(opStack.pop())
                opStack.push(var)
           
        while not opStack.isEmpty():
            postfixExp.append(opStack.pop())
        
        return ' '.join(postfixExp)


def baseConverter(digit,base):
    values = '0123456789ABCDEF'
    stack = []
    while digit > 0:
        rem = digit % base
        stack.append(rem)
        digit = digit // base
    
    output = 'The converted value for the given decimal is  '
    while (len(stack) != 0):
        output = output + str(values[stack.pop()])
    return output    

# class Queue
class Queue:
    
    def __init__(self):
        self.items = []
        
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    
    def dequeue(self):
        return self.items.pop()
    
    def getSize(self):
        return len(self.items)
    
    
    def getFront(self):
        pos = len(self.items)
        return self.items[pos-1]
    
    def getRear(self):
        return self.items[0]


#TOH solver using disk number
op_list = []
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        op_list.append(moveDisk(fromPole,toPole))
        moveTower(height-1,withPole,toPole,fromPole)
    

def moveDisk(fp,tp):
    opEx = ''
    opEx = "Moving disk from "+str(fp)+" to "+str(tp)
    return opEx



def simulator(height,fromPole, toPole, withPole):
    moveTower(height,fromPole, toPole, withPole)
    return op_list















#class Deque
class Deque(object):
    
    #intializing a deque
    def __init__(self):
        self.items = []
        
    #checking for empty deque
    def isEmpty(self):
        return self.items == []
        
        
    def getSize(self):
        return len(self.items)
        
    #inserting at front 
    def addFront(self,item):
        return self.items.append(item)
    
    #inserting at the rear    
    def addRear(self,item):                
        return self.items.insert(0,item)
        
    
    #deleting the element from front
    def removeFront(self):
        return self.items.pop()
    
    #deleting the element from Rear
    def removeRear(self):
        return self.items.pop(0)
    
    #peeking the front element
    def getFront(self):
        pos = len(self.items)
        return self.items[pos-1]
    
    #peeking the rear element
    def getRear(self):
        return self.items[0]
        

def isPalindrome(exp):
    d1 = Deque()
    exp = exp.lower()
    for char in exp:
        d1.addRear(char)

    isPal = True

    while d1.getSize() > 1 and isPal:
        first = d1.removeRear()
        last = d1.removeFront()
        if first != last:
            isPal = False
        
    return isPal

    

