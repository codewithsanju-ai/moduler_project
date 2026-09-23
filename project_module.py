import  datetime,time
import math 
import random
import uuid
import string
from utilities.file_module import *

while True:
    print("WELCOME TO MULTI-UTILITY TULLKIT ")
    print("CHOOSE A OPTION ")
    print("1.DATETIME AND TIME OPEATION")
    print("2.MATHEMATICAL OPERATION")
    print("3.RANDOM DATA GENERATION")
    print("4.GENERATE UNIQUE IDENTIFIER (UUID)")
    print("5.FILE OPERATIONS (CUSTOM MODULE)")
    print("6.EXPLORE MODULE ATTRIBUTE (DIR())")
    print("7.EXIT")
    choice1=int(input("ENTER THE  CHOICE::"))
    match choice1:
        case 1:
            while True:
                print("CHOOSE A OPTION ")
                print("1.DISPLAY CURRENT TIME AND DATE")
                print("2.CALCULATE DIFFERENCE BETWEEN TWO TIME/DATE")
                print("3.FORMAT DATE INTO CUSTOM DATE")
                print("4.STOPWATCH")
                print("5.COUNDDOWN")
                print("6.BACK TO MAIN MENU")
                choice2=int(input("ENTER THE CHOICE::"))

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
                        formatted_date = custom_date.strftime("%d-%m-%Y %H:%M:%S")
                        print("custom date ::",custom_date)
                    case 4:
                       input("Press ENTER to start...")
                       start = datetime.datetime.now()
                       input("Press ENTER to stop...")
                       stop = datetime.datetime.now()
                       elapsed = stop - start
                       total = int(elapsed.total_seconds())
                       hours = total // 3600
                       minutes = (total % 3600) // 60
                       seconds = total % 60    
                       print(f"Time: {hours:02}:{minutes:02}:{seconds:02}")
                    case 5:
                        count_time=int(input("ENTER THE  COUNTDOWN TIME  ::"))
                        i=count_time
                        while True:
                         if i<=count_time:
                           print(f"remianig time:{i} seconds")
                           time.sleep(1)
                           i-=1
                           if i==0:
                            break
                        print("Time's UP!!")
                    case 6:
                        print("THANK YOU FOR USING DATE AND TIME MODULE")
                        break
                        

                
        case 2:
            while True:
                print("1.CALCULATE FACTORIAL")
                print("2.COMPOUND INTEREST")
                print("3.TRIGNOMETRIC CALCULATUIONS")
                print("4.AREA OF GEOGRAPHIC SHAPES")
                print("5.BACK TO MAIN MENU")
                choice3=int(input("ENTER THE CHOICE::"))
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
                            print("2.calculate circle")
                            print("3.calculate rectangle")
                            print("4.calculate triangle")
                            print("5.EXIT")
                            choice4=int(input("enter the choice"))
                            match choice4:
                                case 1:
                                    side=int(input("enter side for square calculation"))
                                    area=side * side
                                    print("area of square::",area)
                                case 2:
                                    r=int(input("enter r for circle calculation"))
                                    area=math.pi*math.pow(r,2)
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
                                    print("THANK YOU FOR USING")
                                    break
                    case 5:
                        print("THANK YOU FOR USING MATH MODULE")
                        break
        case 3:
            while True:
                print("1.Generatre Random Number")
                print("2.Generate Random List")
                print("3.Create Random Password")
                print("4.Generate Random OTP")
                print("5.BACK TO MAIN MENU")
                choice5=int(input("enter the choice::"))
                match choice5:
                    case 1:
                        start_num=int(input("enter the start number"))
                        last_num=int(input("enter the last number"))
                        print("random number between them :",random.randint(start_num,last_num))
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
                        password=''.join(random.choices(character,k=length))
                        print(password)
                    case 4:
                        length=int(input("enter the length of password: "))
                        otp=''.join(random.choices(string.digits,k=length))
                        print(otp)
                    case 5:
                        print("THANK YOU FOR USING DATE AND TIME MODULE")
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
                choice6=int(input("ENTER THE CHOICE::"))
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
                        print("THANK YOU FOR USING DATE AND TIME MODULE")
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
            
                