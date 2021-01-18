def swapByThreeVar(list):
    # t a b t 
    t=list[0]
    list[0]=list[1] 
    list[1]=t 
#end of function 


def main():
    a=10
    b=20
    list=[a,b ]
    print("Before function call")
    print(list[0])
    print(list[1])
    swapByThreeVar(list)
    print("after swap")
    print(list[0])
    print(list[1])
#end of main() function 


#entry point
main()

