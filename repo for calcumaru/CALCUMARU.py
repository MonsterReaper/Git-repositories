# dont copy shibe sama
# © 2022 shivesh.s 
import math
import time


def calculator():
     print("Welcome to Bifrost-Calculator")
     s = input("""press:
     c to Calculate
     help for for tutorial
     credits for credits
     i to find numbers inbetween two numbers 
     sqrt to find square root
     CI to find compund interest """)

     s = s.lower()
     time.sleep(1)


     try:
     
      if s == 'i':
        l = int(input('from: '))
        e = int(input('to: '))
        
        while l < e:
          l += 1
          print(l-1)
          print(l)


      elif s == 'help':
         print('''Hi this is a quick tutorial
    type a number
    then a given symbol
    then a number again
    example:
    5
    +
    9
    it will give 9 as output!, thats how this work''')
     
     
      elif s == 'c':
          calc = 0
          Number1 = int(input("Enter the first number: "))
          symbol = input("- , + , / , * , raise, remainder: ")
          symbol = symbol.lower()
          number2 = int(input("Enter the second number: "))
          if symbol == "+":
            calc = Number1 + number2
          elif symbol == "-":
            calc = Number1 - number2
          elif symbol == "/":
            calc = int(Number1/number2)
          elif symbol == "*":
            calc = Number1 * number2
          elif symbol == "raise":
            calc = Number1 ** number2
          elif symbol == "remainder":
            calc == Number1 % number2
            print("Loading..")    
          time.sleep(1)
          print("calculating..")
          time.sleep(1)
          print("displaying")
          time.sleep(1)
          print(calc)    
      elif s == "sqrt":
        no = int(input("Enter a number to find its square root: "))
        sqrt = math.sqrt(no)
        print(sqrt)
      
      elif s == "ci":
          print("cant process half yearly")
          amount = int(input("Amount:"))
          interest = int(input("Rate: "))
          n = int(input("Time: "))
          calculations = amount*(1+interest/100)**n
          calcu = calculations-amount
          calci = str(calcu) + " is the interest"
          print("Amount: ")
          print(calculations)
          print(calci)
      
    


     except ZeroDivisionError as msg:
          print("cant divide by 0")
          print(msg)
def restart():
     ask = input("Calculate anything?: (Y/N)")
     ask = ask.upper()
     if ask == 'Y':
          return True
     else:
          return False
    
while restart():
     calculator()
print("Bye")