class clsSampleException:
    def __init__(self):
        print("constructor called ")
    def funAccept(self):
        name=input("Enter your name")
        self.name=name;
        try:
            age=int(input("Enter your age"))
            if(age<18):
                raise ValueError
            else:
                self.age=age
        except ValueError:
            print("age must be equal or greter that 18")
    def funDisplay(self):
        print("Entered Name is ",self.name)
        print("Entered age is ",self.age)
    def __del__(self):
        print("destructor call ,object which is created by constructor is deleted by destuctor")
    def funDivByZero(self):
        try:
            a=int(input("Enter first number"))
            b=int(input("Enter second number "))
            c=a/b
        except Exception as e:
            print("Genereated exception is ")
            print(e)
        else:
            print("Division result is ",c)
        finally:
            print("you have tryied division ")
        
       
def main():
    obj=clsSampleException()
    obj.funAccept();
    obj.funDisplay();
    obj.funDivByZero();
main()