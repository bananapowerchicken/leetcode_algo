def fizzBuzz(n):
    # Write your code here
    
    for i in range(1, n+1):
        is_multiple = False
        if i % 3 == 0:
            print('Fizz')
            is_multiple = True
        if i % 5 == 0:
            print('Buzz')
            is_multiple = True
        if not is_multiple:
            print(i)
        
        
        

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)