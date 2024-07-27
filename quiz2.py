
score = 0

def question_system(question, answer):
    global score  
    print(question)
    user_input = input("Type your answer here: ").strip().lower() 
    if user_input == answer.lower():  
        print("Hurray! You got it right!")
        score += 1  
        print(f"You have {score} point(s)")
    else:
        print("Sorry, that's not correct. Try again!")

def main():
    global score
    
    print("Welcome to the Advanced Biology Quiz Game!")
    status = input("Do you want to play the game? (Y or N): ").strip().lower() 
    
    if status == "y":
        # Advanced Biology questions and answers
        questions_and_answers = [
            ("What is the process by which DNA is copied before cell division?", "dna replication"),
            ("What is the term for the loss of water from plant leaves?", "transpiration"),
            ("Which part of the cell is responsible for protein synthesis?", "ribosome"),
            ("What is the name of the process that converts glucose into ATP in the presence of oxygen?", "cellular respiration"),
            ("What is the role of the enzyme 'catalase' in cells?", "decomposition of hydrogen peroxide"),
            ("Which phase of mitosis involves the alignment of chromosomes along the equatorial plane?", "metaphase"),
            ("What type of bond is formed between amino acids in proteins?", "peptide bond"),
            ("Which structure in the cell membrane is responsible for regulating the passage of substances in and out of the cell?", "cell membrane"),
            ("What is the name of the organelle that contains enzymes for digesting cellular waste?", "lysosome"),
            ("What is the term for the genetic variation that occurs during meiosis due to the exchange of genetic material between homologous chromosomes?", "crossing over")
        ]
        
      
        for question, answer in questions_and_answers:
            question_system(question, answer)
        
        
        print(f"At the end of the quiz, you scored {score} point(s).")
        
    elif status == "n":
        print("The game has ended. Have a great day!")

if __name__ == "__main__":
    main()
