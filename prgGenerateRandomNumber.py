import random
def funGenrateRandomNum(frm,to):
    res=random.randint(frm,to)
    print(res)

def main():
    frm=1
    to=100
    funGenrateRandomNum(frm,to)

main()