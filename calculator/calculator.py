def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def mod(x,y):
    return x%y

def pow(base,expo):
    return base**expo

def root(num,root):
    if num<0:
        return f"{(num**(1/root)):.2f}"
    return num**(1/root)





print("choose an operation:")
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
print("5:Modulus")
print("6:Power")
print("7.root")



l1=[]
while True:
    choice=input("choose between (1/2/3/4/5/6/7):")
    n=["1","2","3","4","5"]
    p=["6","7"]
    if choice in n:
        while True:
            try:
                n1=int(input("enter a number:"))
                n2=int(input("enter a number:"))
            except ValueError:
                print("Input is invalid . Please enter valid input")
                continue
            break
        if choice=="1":
            print(f"{n1} + {n2} = {add(n1,n2)}")
            l1.append(f"{n1} + {n2} = {add(n1,n2)}")
        if choice=="2":
            print(f"{n1} - {n2} = {sub(n1,n2)}")
            l1.append(f"{n1} - {n2} = {sub(n1,n2)}")
        if choice=="3":
            print(f"{n1} * {n2} = {mul(n1,n2)}")
            l1.append(f"{n1} * {n2} = {mul(n1,n2)}")
        if choice=="4":
            try:
                print(f"{n1} / {n2} = {div(n1,n2)}")
                l1.append(f"{n1} / {n2} = {div(n1,n2)}")
            except ZeroDivisionError:
                print("ZeroDivisionError")
                continue
        if choice=="5":
            try:
                print(f"{n1} % {n2} = {mod(n1,n2)}")
                l1.append(f"{n1} % {n2} = {mod(n1,n2)}")
            except ZeroDivisionError:
                print("ZeroDivisionError")
                continue
        
        while True:
            history=input("Want to see history(y/n)")
            n2=["y","n"]
            if history in n2:
                if history.lower()=="n".lower():
                    break
                else: 
                    print("Displaying HIstory:")
                    for i in l1:
                        print(i)
                    break
            else:
                print("Enter a valid response!")
        
        exit=False
        while True:
            execute=input("Want one more time (y/n)")
            n3=["y","n"]
            if execute in n3:
                if execute.lower()=="y".lower():
                    break
                else:
                    exit=True  
                break
            else:
                print("Enter a valid response!")
        if exit:
            break






    elif choice in p:
        if choice=="6":
            while True:
                try:
                    b=int(input("enter base value: "))
                    e=int(input("enter power:"))
                except ValueError:
                    print("Input is invalid . Please enter valid input")
                    continue
                break
            print(f"{b} ^ {e} = {pow(b,e)}")
            l1.append(f"{b} ^ {e} = {pow(b,e)}")
        if choice=="7":
            while True:
                try:
                    
                    x=int(input("enter a number: "))
                    n=int(input("enter root: "))
                except ValueError:
                    print("Input is invalid . Please enter valid input")
                    continue
                break
            try:
                print(f"{n} root of {x} = {root(x,n)}")
                l1.append(f"{n} root of  {x} = {root(x,n)}")
            except ZeroDivisionError:
                print("ZeroDivisionError")
                continue

        while True:
            history=input("Want to see history(y/n)")
            n2=["y","n"]
            if history in n2:
                if history.lower()=="n".lower():
                    break
                else: 
                    print("Displaying HIstory:")
                    for i in l1:
                        print(i)
                    break
            else:
                print("Enter a valid response!")
        
        exit=False
        while True:
            execute=input("Want one more time (y/n)")
            n3=["y","n"]
            if execute in n3:
                if execute.lower()=="y".lower():
                    break
                else:
                    exit=True  
                break
            else:
                print("Enter a valid response!")
        if exit:
            break


    
    else:
        print("Invalid Choice!")
print("Thank you for using the calculator.\nHave a nice day!")



