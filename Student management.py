import csv
def csv_write(a):
    csvf=open("stu_detail.csv","a",newline="")
    stuwriter=csv.writer(csvf)
    if csvf.tell()==0:
        stuwriter.writerow(["Name","Age","Contact","Email_ID"])
    stuwriter.writerow(a)
    csvf.close()

if __name__ == '__main__':
    count=0
    con=True
    while con == True:
        print("Enter information in format 'Name Age Contact No Email_ID'")
        str_input=input("Enter details of student: ")
        input_list=str_input.split(" ")
        print(input_list)
        print("Enter Information is:\nName: {}\nAge: {}\nContact No: {}\nEmail_ID: {}". 
              format(input_list[0], input_list[1],input_list[2],input_list[3]))
        ans_check=input("Is information correct, ANSWER in Y or N: ")
        if ans_check in "Yy":
            count+=1
            csv_write(input_list)
            ans_con=input("Do you want to enter information of more students: ")
            if ans_con in 'Yy':
                con=True
            elif ans_con in 'Nn':
                con=False
                print("No of students whose information stored is: ",count)
        elif ans_check in "Nn":
            print("Please enter correct information again!")
