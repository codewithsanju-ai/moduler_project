import  datetime
import math 
import random
import uuid
import string
from file_module import *

while True:
    print("welcome to multi-utility tullkit ")
    print("choose a open ")
    print("1.datetime and time operation")
    print("2.Mathematical operation")
    print("3.random data generation")
    print("4.Generate Unique Identifier (uuid)")
    print("5.file operations (custom module)")
    print("6.explore module Attribute (dir())")
    print("7.Exit")
    choice1=int(input("enter the first input"))
    match choice1:
        case 1:
            while True:
                print("Display current date and time")
                print("calculate diffrence betwwen two dates/times")
                print("format date into custom format")
                print("stopwatch")
                print("countdown Timer")
                print("back to main menu")
                choice2=int(input("enter the choice"))

                match choice2:
                    case 1:
                        print("TODAY DATE AND TIME IS ::",datetime.datetime.now())
                    case 2:
                        date1=input("enter first date1 in dd-mm-yyy:")
                        date2=input("enter second date2 in dd-mm-yyy:")
                        converted_date1=datetime.datetime.strptime(date1,"%d-%m-%Y")
                        converted_date2=datetime.datetime.strptime(date2,"%d-%m-%Y")
                        difference=abs((converted_date2-converted_date1).days)
                        print("day diffrence betwwen two date::",difference)
                    case 3:
                        
                        year = int(input("Enter year: "))
                        month = int(input("Enter month: "))
                        day = int(input("Enter day: "))
                        hour = int(input("Enter hour: "))
                        minute = int(input("Enter minute: "))
                        second = int(input("Enter second: "))
                        custom_date=datetime.datetime(year,month,day,hour,minute,second)
                        print("custom date ::",custom_date)
                    case 4:
                        print("")
                    case 5:
                        print("")
                    case 6:
                        break
                        

                
        case 2:
            while True:
                print("1.calculate factorial")
                print("2.solve compound interest")
                print("3.trigonometric calculations")
                print("4.area of geometric shapes")
                print("5.back to main menu")
                choice3=int(input("enter the choice"))
                match choice3:
                    case 1:
                        number=int(input("input the number for calculate the factorial:"))
                        result=math.factorial(number)
                        print("faactorial of number is:",result)
                    case 2:
                        p = float(input("Enter principal amount: "))
                        r = float(input("Enter rate of interest: "))
                        t = float(input("Enter time in years: "))
                        amount=p*math.pow((1+r/100),t)
                        a=math.trunc(amount)
                        ci=a-p
                        print("compound interest:",ci)
                        print("toral amount:",a)
                    case 3:
                        angle=int(input("enter the angle in degree"))
                        radians=math.radians(angle)                        
                        print("sin value::",math.sin(radians))
                        print("cos value::",math.cos(radians))
                        print("tan value::",math.tan(radians))
                        print("asin value::",math.asin(radians))
                        print("acos value::",math.acos(radians))
                        print("atan value::",math.atan(radians))
                    case 4:
                        while True:
                            print("1.calculate square")
                            print("1.calculate circle")
                            print("1.calculate rectangle")
                            print("1.calculate triangle")
                            choice4=int(input("enter the choice"))
                            match choice4:
                                case 1:
                                    side=int(input("enter side for square calculation"))
                                    area=side * side
                                    print("area of square::",area)
                                case 2:
                                    r=int(input("enter r for circle calculation"))
                                    area=math.pi*math.pow(r)
                                    print("area of square::",area)
                                case 3:
                                    length=int(input("enter length for rectangle calculation"))
                                    width=int(input("enter width for rectangle calculation"))
                                    area=length*width
                                    print("area of rectangle::",area)
                                case 4:
                                    base=int(input("enter base for triangle calculation"))
                                    height=int(input("enter height for triangle calculation"))
                                    area=0.5*base*height
                                    print("area of tringle::",area)
                    case 5:
                        break
        case 3:
            while True:
                print("1.Generatre Random Number")
                print("2.Generate Random List")
                print("3.Create Random Password")
                print("4.Generate Random OTP")
                print("5.BACK TO MAIN MENU")
                choice5=int(input("enter the choice"))
                match choice5:
                    case 1:
                        start_num=int(input("enter the start number"))
                        last_num=int(input("enter the last number"))
                        print("random number :",random.randint(start_num,last_num))
                    case 2:
                        list1=[]
                        end_num=int(input("enter the end number"))
                        count = int(input("How many random numbers? "))

                        for i in range(count):
                            a=random.randint(1,end_num)
                            list1.append(a)
                        print(list1)
                    case 3:
                        length=int(input("enter the length of password: "))
                        character=string.ascii_letters+string.digits
                        password=(random.choices(character,k=length))
                        print(password)
                    case 4:
                        length=int(input("enter the length of password: "))
                        otp=''.join(random.choices(string.digits,k=length))
                        print(otp)
                    case 5:
                        break
                        
        case 4:
            print("using uuid1:",uuid.uuid4())
            print("using uuid2:",uuid.uuid1())
        case 5:
            while True:
                print("File Opeartions")
                print("1.Create a new file")
                print("2.Write to a file")
                print("3.Read  from a file")
                print("4.Append to a file ")
                print("5.Back to main menu")
                choice6=int(input("enter the choice"))
                match choice6:
                    case 1:
                        create_file()
                    case 2:
                        write_file()
                    case 3:
                        read_file()
                    case 4:
                        apppend_file()
                    case 5:
                        break
                

        case 6:
            print("Explore Module Attribute:")
            module_name=input("enter the module name ::")
            print(f"avalaible Attribute name in {module_name} module")
            print(dir(module_name))
        case 7:
            print("thank you to use this multi-utility Tullkit")
            break
        case _:
            print("invalid input")
            
                