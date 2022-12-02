
a=str(input())
print(ord(a))
b=ord(a)+2
print(b)
def factorial_1(n):        
        fact = 1                 
        for i in range(1,n+1,1): 
            fact = fact*i            
        return fact #print(fact)
factorial_1(7)
# factorial_1(1)
# factorial_1(0)
# factorial_1(8)
# factorial_1(10)
# factorial_1(100)
