class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    Attributes
    ----------
    size : int object
        Max size of max_heap 'heap' object, default is 20
    data : list object
        List containing the desired heap contents, default is None

    Methods
    -------
    get_heap():
        Returns the heap object
    insert(data):
        Inserts an element into the list, self.heap
    peek():
        Returns the maximum value in the heap
    extract_max():
        Remove and return the maximum value in the heap
    sort_in_place():
        Performs a heatsort in-place on a heap object
    build_heap():
        Builds max_heap from a list
    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations -- using __swap method.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        return self.heap


    def insert(self, data):
        """Insert an element into the heap.

        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root
        
        if self.length >= self.max_size:
            raise IndexError("Heap is full")
    
        # Add the new element to the end of the heap.
        self.heap[self.length] = data
        
        # Get the index of the newly added element.
        current_index = self.length

        # Swap the new element with its parent until it's in the correct position.
        while current_index > 0:
            parent = self.__get_parent(current_index)
            
            if self.heap[current_index] > self.heap[parent]:
                self.__swap(current_index, parent)
                current_index = parent
            else:
                break

        self.length += 1
            
    def peek(self):
        """Return the maximum value in the heap."""
        if self.length == 0:
            return None
        else:
            return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""
        if self.length == 0:
            raise KeyError("Heap is empty")

        max_value = self.heap[0]
        self.length -= 1
        self.__swap(0, self.length)
        self.heap[self.length] = None  # Set the last element to None
        self.__heapify(0)  # Call the heapify function to reorganize the heap
        return max_value


    def sort_in_place(self):
        """Perform heatsort in-place (e.g., reorder elements in ascending order for self.heap)
        Note that the heap is no longer "valid" once this method is called.
        Tip 1. Use the list_length parameter for __heapify method to limit the scope of self.heap
        Tip 2. Only use build_heap once, and then call __heapify for index where max-heap property is violated
        """
        self.build_heap()
        for i in range(self.x - 1, 0, -1):
            self.__swap(0, i)
            self.__heapify(0, i)


    def __heapify(self, curr_index, list_length = None):
        """Recursively adjust the max-heap structure starting from the given index.

        This function compares the element at the current index with its left and right
        children (if they exist) and moves the largest element up to the current index.
        If the max-heap property is violated, it swaps elements and continues recursively
        to ensure the max-heap property is maintained.

        Arguments
        ---------
            curr_index (int): The current index of the element to be adjusted.
            list_length (int, optional): The length of the list or sub-list to operate on.
            If not provided, it defaults to the length of the heap.
        """
        if list_length is None:
            list_length = self.length
        left_child = self.__get_left(curr_index)
        right_child = self.__get_right(curr_index)
        largest = curr_index

        if left_child < list_length and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < list_length and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest, list_length)


    def build_heap(self):
        """Build a max-heap from the current list of elements.

        This function transforms the current list into a valid max-heap by applying
        the `__heapify` function to each element, starting in the middle of
        the list and moving towards the beginning, ensuring that the max-heap
        property is satisfied for each sub-tree

        Arguments:
            None

        """
        for i in range(self.length // 2, -1, -1):
            self.__heapify(i)
            print(self.get_heap())


    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2
        

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
    

def heap_sort(l):
    """The public heap_sort should do the following.
    1. Create a max_heap object using the provided list l
    2. Call sort_in_place method to sort the list "in-place"
    """
    max_heap_obj = max_heap(data=l)
    max_heap_obj.sort_in_place()
    return max_heap_obj.get_heap()