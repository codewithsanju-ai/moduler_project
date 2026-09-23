def create_file():
    try:
        file_name=input("enter the file name::")
        with open(file_name+".txt",'x') as file:
            file.write('file created !!!!!!'+"\n")
    except FileExistsError:
        print("file already exists")

def write_file():
    try:
        file_name=input("enter the file name::")
        data=input("enter the txt you want to write in the file::")
        with open(file_name+".txt",'a') as file:
            file.write(data+"\n")
            
            
    except FileNotFoundError:
        print("file not found ")
def read_file():
    try:
        file_name=input("enter the file name::")
        with open(file_name+".txt",'r') as file:
            res=file.read()
            print(res)
        
    except FileNotFoundError:
        print("file not found")
def apppend_file():
    try:
        file_name=input("enter the file name;:")
        data=input("enter the txt you want to append in the file::")
        with open(file_name+".txt","a") as file:
            file.write(data+"\n")
    except FileNotFoundError:
        print("file not found")
    
if __name__=="__main__":
    create_file()
    write_file()
    apppend_file()
    read_file()
    print("This script is running directly.")
    
