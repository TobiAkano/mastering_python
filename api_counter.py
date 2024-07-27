Name=str(input(" what is your Name: "))
print("welocome " + Name + " the API calculating machine ")
API=int(input("Enter your API: "))
print ("do you want to calculate you api with a subject or with out a subject")
no_of_subjects = (input("how many subject do you do (write the number): "))
if no_of_subjects == int or float:
    print("what subject would you like to add: ")
    Subject=str(input("Subject: "))
    print("so " + Name +" we would add your score for " + Subject + "to your API")
    Score_of_subject=int(input("Type your score here: "))
    Total_API = (API*no_of_subjects+Score_of_subject)/(no_of_subjects+1)
    print(Total_API)
else:
    print("the number of subject you do must be in numbers")
