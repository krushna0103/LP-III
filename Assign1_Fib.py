


def fibWithRecursion(n):
    if n < 0:
        print("Incorrect Num")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibWithRecursion(n-1) + fibWithRecursion(n-2)
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))


        
print("Fibonacii number till n are : \n")
n = int(input("\nEnter Number : "))
for i in range(n):
    print(fibWithRecursion(i))
#    print(f"\nFibonacci Number of " + str(n) + " is " + str(fibWithRecursion(n+1)))
#

# n1, n2 = 0, 1
# count = 0

# if n <= 0:
#     print("Enter Positive Num")
# elif n == 1:
#     print("Fibonacci of ",n,":")
#     print(n1)
# else:
#     print("\nFibonacci sequence: ")
# while count < n:
#     print(n1, end=" ")
#     nth = n1 + n2

#     n1 = n2
#     n2 = nth
#     count += 1   
