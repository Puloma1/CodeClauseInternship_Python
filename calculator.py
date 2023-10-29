def add(x,y):
     return x+y

def subtract(x,y):
     return x-y

def mult(x,y):
     return x*y

def div(x,y):
     return x/y

def modulo(x,y):
     return x%y

def options():
     while True:
          print("\nSelect Operation : \n")
          print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulo\n")
          choice = int(input("Choice : "))
          num1 = int(input("Enter First Number = "))
          num2 = int(input("Enter Second Number = "))
          if choice ==1 :
               print(num1,"+",num2,"=",add(num1,num2))
          elif choice ==2 :
               print(num1,"-",num2,"=",subtract(num1,num2))
          elif choice ==3 :
               print(num1,"*",num2,"=",mult(num1,num2))
          elif choice ==4 :
               print(num1,"/",num2,"=",div(num1,num2))
          elif choice ==5 :
               print(num1,"%",num2,"=",modulo(num1,num2))
          continued =input("Press any key to continue (No to exit) : ")
          if continued == 'No':
               break
          elif continued == 'no':
               break
          else :
               print("Continuing...")


options()
