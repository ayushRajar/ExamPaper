import csv
print("WELCOME TO QUESTION PAPER GENERATOR: ")
if(__name__=="__main__"):
    n=int(input("ENTER THE NUMBER OF QUESTION: "))

    for i in range(1,n+1):
        print("ENTER THE NUMBER OF SUBDIVISION OF QUESTION : ",end=" ")
        s = int(input())
        for j in range(s):
            print("QUESTION 1 ",chr(97+j) ,end=" ")
            q=input()


