class LargestOddAndEven:
    def largestEven(self, list):
        curr = -1        
        for num in list: 
            num = int(num)
            if(num % 2 == 0 and num > curr):
                curr = num
        print("Largest even number is ", curr)
    def largestOdd(self, list):      
        currO = -1
        for num in list:
          
            # converting number to integer
            # explicitly
            num = int(num)
            
            # even number is divisible by 2 and 
            # if larger than current largest
            if(num % 2 == 1 and num > currO):
                
                # replace current largest even
                currO = num

        print("Largest odd number is ", currO)

list_num = [1, 3, 5, 8, 6, 10]

# creating an object of class
obj = LargestOddAndEven()

# calling method for largest even number
obj.largestEven(list_num)

# calling method for largest odd number
obj.largestOdd(list_num)