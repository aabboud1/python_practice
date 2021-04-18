class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
         
        #  create empty list to store 
         li = []

        # loop to go through the list and check the number and write the correct thing
         for x in range(1, n + 1):
            if x % 3 == 0 and x % 5 == 0:
                li.append('FizzBuzz')
            elif x % 3 == 0:
                li.append('Fizz')
            elif x % 5 == 0:
                li.append('Buzz')
            else:
                li.append(str(x))
        
        return li