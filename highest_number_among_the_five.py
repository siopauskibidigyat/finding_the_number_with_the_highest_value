#define the 5 variables
    #identify the numbers as the input
def find_highest(num1, num2, num3, num4, num5):
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))
    num4 = int(input("Enter another number: "))
    num5 = int(input("Enter another number: "))

    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    num5 = int(num5)
#compare var1 and var2
#if var1 is greater than var2
    #compare var1 to var3
    #if var1 is greater than var3
    #compare var1 to var4
    #if var1 is greater than var4
    #compare var1 to var 5
    #if var1 is greater than var 5
    #print var1
    #if not print var5 
    if num1 > num2:
        if num1 > num3:
            if num1 > num4:
                if num1 > num5:
                    print(f"The highest number is {num1}")
                else:
                    print(f"The highest number is {num5}")
        elif num1 < num3:
            if num3 > num4:
                if num3 > num5:
                    print(f"The highest number is {num3}")
                else:
                    print(f"The highest number is {num5}")
            elif num3 < num4:
                if num4 > num5:
                    print(f"The highest number is {num4}")
                else:
                    print(f"The highest number is {num5}")
#else if var1 is less than var2
    #compare var2 to var3
    #if var2 is greater than var3
    #compare var2 to var4
    #if var2 is greater than var4
    #compare var2 to var5
    #if var2 is greater than var5
    #print var2
    #if not print var 5
    elif num1 < num2:
        if num2 > num3:
            if num2 > num4:
                if num2 > num5:
                    print(f"The highest number is {num2}")
                else:
                    print(f"The highest number is {num5}")
        elif num2 < num3:
            if num3 > num4:
                if num3 > num5:
                    print(f"The highest number is {num3}")
                else:
                    print(f"The highest number is {num5}")
            elif num3 < num4:
                if num4 > num5:
                    print(f"The highest number is {num4}")
                else:
                    print(f"The highest number is {num5}")
res = find_highest(num1=0, num2=0, num3=0, num4=0, num5=0)
