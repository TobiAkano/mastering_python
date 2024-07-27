Name = input("What is your name? ")
print("Welcome, " + Name + ", the API calculating machine")

api = float(input("Enter your API: ")) 
no_of_subjects = int(input("How many subjects do you have? "))  

total_score = 0

for _ in range(no_of_subjects):
    subject = input("Enter subject name: ")
    score_of_subject = float(input("Enter your score for " + subject + ": "))
    total_score += score_of_subject  

total_API = (api + total_score) / (no_of_subjects + 1)
print("Total API for " + Name + " is: " + str(total_API))
