import math
class mathOps:
    """
    Simple math operations on a given pair of integers, u and v.

    This includes the lcm (least common multiple) and 
    gcd (greatest common divisor) functions, each of returns an integer.
    """

    def __init__(self, u, v):
        '''Set the values of u and v to be used in the math operations.'''
        self.u = u
        self.v = v
        
    
    def __repr__(self):
        return "mathOps({}, {})".format(self.u, self.v)
    
    def valid(self):
        '''True if both u and v are integers.'''
        return isinstance(abs(math.ceil(self.u)), int) and isinstance(abs(math.ceil(self.v)), int)
    
    def gcd(self):
        '''Compute the greatest common divisor of member variables u and v.'''
        # Find the greatest common divisor of a and b
        # Hint: Use Euclid's Algorithm
        # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
        # Taking absolute value and ceiling of each to account for negative numbers and floating points
        tempU = abs(math.ceil(self.u))
        tempV = abs(math.ceil(self.v))
        try:
            # Asserting both numbers are ints
            if not self.valid():
                raise TypeError
        except TypeError:
            print("one or both the values of ", tempU, " and ", tempV, " are not integers")
            raise TypeError
        try:
            # Asserting neither number is infinity
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise ValueError
        except ValueError:
            print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise ValueError
        
        # Checking if either is 0 and returning 0 if so    
        if tempU==0:
            return tempV
        if tempV==0:
            return tempU
        
        # Setting up tempU > tempV
        if tempU>tempV:
            a = tempU
            b = tempV
        else:
            a = tempV
            b = tempU
        # Standard Euclidean algorithm procedure
        left = a
        p_rem = b
        q = left//p_rem
        rem = q*p_rem-a
        # Infinite loop until broken by GCD found
        while 1:
            if rem==0:
                return abs(p_rem)
            left = p_rem
            p_rem = rem
            q = left//p_rem
            rem = q*p_rem-left

      # ENTER YOUR CODE HERE
      # Feel free to modify the exceptions, delete the try block etc or the entire funtion
      # Just keep the fucntion name as gcd
    
        
          
             

        
    def lcm(self):
      '''Compute the least common multiple of member variables u and v.'''
      # Hint: Use the gcd of a and b
      # Taking absolute value and ceiling of each to account for negative numbers and floating points

      tempU = abs(math.ceil(self.u))
      tempV = abs(math.ceil(self.v))
      try:
          # Making sure neither value is infinity
        if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
            raise OverflowError
      except OverflowError:
          print("one or both the values of ", tempU, " and ", tempV, " are equal to infinity")
          raise OverflowError
      try:
          # Making sure neither value is zero
        if tempU == 0 or tempV == 0:
            raise ZeroDivisionError
      except ZeroDivisionError:
          print("one or both the values of ", tempU, " and ", tempV, " are equal to 0")
          raise ZeroDivisionError
        
        # ENTER YOUR CODE HERE
        # Feel free to modify the exceptions, delete the try block etc or the entire funtion
        # Just keep the fucntion name as lcm
        # Standard LCM computation algorithm
      return (tempU*tempV)/self.gcd()
      
      
      


