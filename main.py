import csv
import openpyxl

wb=openpyxl.load_workbook(filename="Q2.xlsx")
sheet= wb.active


print("WELCOME TO QUESTION PAPER GENERATOR: ")

if(__name__=="__main__"):
    course = input("ENTER THE COURSE NAME: ")
    sheet["B7"] = course

    cid = input("ENTER THE COURSE ID: ")
    sheet["B8"] = cid

    dt = input("ENTER THE DATE AND TIME OF EXAMINATION: ")
    sheet["B9"] = dt

    batch = input("ENTER YOUR BATCH: ")
    sheet["G6"] = batch

    maxmarks = int(input("ENTER THE MAXIMUM MARKS: "))
    sheet["G7"] = maxmarks


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

    csvfile.close()"""

print("PREPARING YOUR QUESTION PAPER: ")
with open("Question.Csv" ,"r") as csvfile:
    csvreader=csv.reader(csvfile)
    data_item=[]
    for data in csvreader:
        data_item.append(data)
csvfile.close()

print(data_item)
ques_col=15
for data in range(1,len(data_item)):
    sheet[f"A{ques_col}"]=data_item[data][0]
    sheet[f"B{ques_col}"] = data_item[data][1]
    sheet[f"D{ques_col}"] = data_item[data][2]
    ques_col+=1
wb.save(filename="Q#.xlsx")



 




