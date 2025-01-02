 #("Q1. Write a program to check leap Year ?")
 
year=int(input("Enter Year"))

if year % 4 ==0 and year % 100 != 0 or year % 400==0:
    print(f"{year}is a leap year")
    
else:
    print("not a leap year")

# Q2. Program to print all prime numbers in an interval of 1 to 10000 ? 

def prime_nums(num):
    if num<=1:
        return False
    for a in range(2,int(num**0.5)+1):
        if num % a == 0:
            return False
    return True

prime_list=[]
for num in range(2,10001):
    if prime_nums(num):
        prime_list.append(num)
        
    
print(prime_list)
        
        


# Q3. Program to find Armstrong numbers in an interval of 1 to 10000 ? 
    
    

# Q4. HCF 
def hcf(a,s):
    if s == 0:
        return a
    else:
        return hcf(s , a%s )
    
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

result = hcf(num1,num2)
print(f"HCF of {num1} and {num2} = ",result)


        


