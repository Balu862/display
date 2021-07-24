odd=[]
even=[]
def check(n):
    if n%2==0:
        even.append(n)
        print("evenlist: ",even)
    else:
        odd.append(n)
        print("oddlist: ",odd)
n=int(input("Enter a number: "))
check(n)