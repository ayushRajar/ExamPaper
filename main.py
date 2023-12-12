import csv
print("WELCOME TO QUESTION PAPER GENERATOR: ")
if(__name__=="__main__"):
    n=int(input("ENTER THE NUMBER OF QUESTION: "))
    field=["Number","Question","Marks"]
    with open ("Question.Csv" , "w") as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(field)

        for i in range(1,n+1):
            print("ENTER THE NUMBER OF SUBDIVISION OF QUESTION : ",end=" ")
            s = int(input())
            for j in range(s):
                print("QUESTION 1 ",chr(97+j) ,end=" ")
                q=input()
                m=int(input("ENTER THE MARKS: "))
                print()

                l=[f"{i}{chr(97+j)}",q,m]
                csvwriter.writerow(l)

    csvfile.close()




