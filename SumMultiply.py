def sum():
    mylist = input('Enter your list: ')
    mylist = [int(x) for x in mylist.split(',')]
    total = 0    
    for number in mylist:    
        total += number    
    print ("The sum of the numbers is:", total)
            
sum()

def multiply():
    myList1 = input('Enter your numbers: ')
    myList1 = [int(y) for y in myList1.split(',')]
    product = 1
    for number in myList1:
        product= product*number
    print("The product of the numbers is: ", product)
multiply()
    
