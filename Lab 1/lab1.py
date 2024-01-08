class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node  = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """
    A class to represent a Queue.

    ...

    Attributes
    ----------
    __head : int or float
        Represents the top of the queue or the first item inputted
    __tail : object of class Node
        Represents the end of the queue or the last item inputted

    Methods
    -------
    enqueue(newData):
        Creates a new node and appends it to the tail of the queue
    dequeue():
        Dequeues the head of the queue and updates the next node to be the new head of the queue
    isEmpty():
        Returns a boolean representing whether the queue is empty (True) or not empty (False)
    """
    def __init__(self):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        __head : object of class Node
            The first enqueued node in the queue
        __tail : object of class Node
            The last or most recent enqueued node in the queue
        """
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.
        Padded to provide the formatting of an array'''
        current = self.__head
        string = "["
        while current != None:
            string += str(current.getData())
            if current == self.__tail:
                break
            current = current.getNext()
            string += ", "
        string += "]"
        return string
            

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.
        Parameters:
            newData: string
                used to create a newNode and set its data as newData
        '''
        # Hint: Think about what's different for the first node added to the Queue
        newNode = Node()
        newNode.setData(newData)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.setNext(newNode)
            self.__tail = newNode

    def dequeue(self):
        '''Return the head of the Queue
        Update head.
        Paremeters:
            None
        Raises:
            Exepction: If queue is empty, nothing can be dequeued'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.__tail == None:
            print("Queue is empty!")
            raise Exception
        else:
            data = self.__head.getData()
            temp = self.__head.getNext()
            self.__head = temp
            return data
            
        

    def isEmpty(self):
        '''Check if the Queue is empty.'''
        if self.__head == None:
            return True
        else:
            return False


class Stack(object):
    """
    A class to represent a Stack.

    ...

    Attributes
    ----------
    size : int or float
        Represents the top of the queue or the first item inputted
    top : object of class Node
        Represents the end of the queue or the last item inputted

    Methods
    -------
    enqueue(newData):
        Creates a new node and appends it to the tail of the queue
    dequeue():
        Dequeues the head of the queue and updates the next node to be the new head of the queue
    isEmpty():
        Returns a boolean representing whether the queue is empty (True) or not empty (False)
    """
    def __init__(self):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        top : object of class Node
            The most recent node pushed to the stack
        size : int
            A number representing the number of nodes in the stack
        """
        self.top = None
        self.size = 0

    def __str__(self):
        '''Loop through your stack and print each Node's data.
        Should return [] is the stack is empty'''
        current = self.top
        string = "["
        count = 0
        while current != None:
            count += 1
            string += str(current.getData())
            if count == self.size:
                break
            string += ", "
            current = current.getNext()
        string += "]"
        return string
        

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top and increment size.
        Parameters:
            newData : string
            Creates a new node whose data is newData and sets it as the new top of the stack'''
        newNode = Node()
        newNode.setData(newData)
        temp = self.top
        newNode.setNext(temp)
        self.top = newNode
        self.size+=1
        

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top. If the top is null, raise an exception as you can't pop from an empty stack.
        Parameters:
            None
        Raises:
            Exception : If top is none, nothing can be popped
            '''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.top == None:
            raise Exception
        data = self.top.getData()
        newTop = self.top.getNext()
        self.top = newTop
        self.size -= 1
        return data

    def isEmpty(self):
        '''Check if the Stack is empty by seeing if top is null.'''
        if self.top == None:
            return True
        else:
            return False
        
class TwoStackQueue(object):
    """
    A class to represent a Two Stack Queue.

    ...

    Attributes
    ----------
    stack1 : object of class Stack
        Represents the stack that all values will initially be put into
    stack2 : object of class Stack
        Represents the stack that will contain the reverse order so .pop() return
        top value

    Methods
    -------
    enqueue(newData):
        Creates a new node and pushes it to stack1
    dequeue():
        Pops the top of the stack2 and updates the next node to be the new top of the stack
    isEmpty():
        Returns a boolean representing whether both stacks are empty (True) or not empty (False)
    """
    def __init__(self):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        stack1 : object of class Stack
            Represents the stack that all values will initially be put into
        stack2 : object of class Stack
            Represents the stack that will contain the reverse order so .pop() return
        top value
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        '''Loop through your active stack and print each Node's data.'''
        temp = Stack()
        stack2_str = str(self.stack2)[:-1]
        while not self.stack1.isEmpty():
            temp.push(self.stack1.pop())
        temp_str = str(temp)[1:]
        if len(temp_str) > 1 and len(stack2_str) > 1:
            temp_str = ", " + temp_str
        while not temp.isEmpty():
            self.stack1.push(temp.pop())
        return stack2_str + temp_str
            

    def enqueue(self, newData):
        '''First pick which stack is the active one. Next create a new node whose data is newData and push
        this Node to the active stack
        Parameters:
            newData: string
                a string containing newData that will be used to create a Node and added to stack1'''
        # Hint: Think about what's different for the first node added to the Queue
        self.stack1.push(newData)

    def dequeue(self):
        '''Pick which stack is the active stack, move all elements from that stack to the other stack.
        Pop the top element of the new stack to get the last element of the previous stack.
        Return that node's data.
        Parameters:
            None
        Raises:
            Exception : If the queue is empty, raise an error as nothing can be dequeued from it.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.isEmpty():
            print("Can't dequeue from an empty Two Stack Queue!")
            raise Exception
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                data = self.stack1.pop()
                self.stack2.push(data)
        return self.stack2.pop()
            

    def isEmpty(self):
        '''Check if the Stacks are empty.'''
        return self.stack2.isEmpty() and self.stack1.isEmpty()

def padString(s):
    '''Pads the string to get rid of spaces and makes all letters in the string lowercase.'''
    s = s.replace(" ", "")
    newstring = ""
    for char in s:
        if type(s) == str:
            newstring+=char.lower()
        else:
            newstring+= char
    return newstring

def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()
    s = padString(s)
    for char in s:
        myStack.push(char)
        myQueue.enqueue(char)
    length = len(s)
    for i in range(length):
        popped = myStack.pop()
        dequeued = myQueue.dequeue()
        if popped!=dequeued:
            return False
    return True
    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # Return appropriate value

def isPalindromeEC(s):
    '''This uses a stack and a two stack queue instead of a regular queue to determine if the string is a palindrome.
    The result should always be the same as the original.'''

    # Return appropriate value
    myStack = Stack()
    myQueue = TwoStackQueue()
    s = padString(s)
    for char in s:
        myStack.push(char)
        myQueue.enqueue(char)
    length = len(s)
    for i in range(length):
        popped = myStack.pop()
        dequeued = myQueue.dequeue()
        if popped!=dequeued:
            return False
    return True
