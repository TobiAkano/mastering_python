# Created by Kareem and Oreoluwa
# write this in terminal or command prompt
# pip install spacy (install python first)
# then write python -m spacy downlaod en_core_web_sm

import spacy
from datetime import datetime

nlp = spacy.load("en_core_web_sm")

questions = {    
    "age": "I'm just a bot, you know.",
    "name": "You can call me Kbot!",
    "colour": "I don't perceive colors, but Kareem's favorite is blue.",
    "hobbies": "I don't have hobbies, but I love assisting Kareem Ayomide.",
    "pets": "I wish I had a pet!",
    "weather": "It's nice.",
    "food": "I don't have preferences, but Kareem loves jollof.",
    "girlfriend": "i dont need one 🗿",
    "nigga": "Can we just have a normal conversation, please?",
    " hello ": "hi",
    " hi ": "hello",
    "language": "I prefer speaking in English.",
    "color": "I don't see colors, but Kareem's favorite is blue.",
    "time": "The time is ",
    "music": "I don't listen to music, but Kareem enjoys phonk.",
    "movies": "I don't watch movies just like Kareem.",
    "sports": "I don't play sports, but Kareem loves basketball.",
    "books": "not rlly a fan of books.",
    "family": "I'm just a bot, I don't have a family.",
    "dreams": "Kareem wants to become  a Software Engineer",
    "technology": "I'm not familiar with the latest tech trends, but Kareem might be.",
    "vacation": "I don't take vacations, but Kareem loves traveling.",
    "school": "I don't attend school, but  Kareem attends juilliard.",
    "career": "I'm just a bot bro but kareem career lies in engineering.",
    "money": "I don't have money bro i'm a bot.",
    "health": "I don't have a body, but Kareem values good health.",
    "travel": "I don't travel, but Kareem enjoys exploring new places.",
    "computers": "I don't use computers, but Kareem is tech-savvy.",
    "games": "I don't play games, but Kareem might enjoy gaming.",
    "relationships": "I'm a bot i dont have relationships but Kareem values friendships.",
    "history": "I don't have personal history, but Kareem might know some historical facts.",
    "politics": "I think tobi knwos alot about this.",
    "future": "kareem better plan my future well.",
    "emotions": "I don't experience emotions, but Kareem understands them.",
    "education": "I'm a bot, but Kareem values education and continuous learning.",
    "nature": "I don't experience nature, but Kareem prefers staying indoors.",
    "art": "I don't create art, i can tho if kareem works on me.",
    "creativity": "I don't have creativity.",
    "sleep": "I don't sleep cuz my creator is very nocturnal",
    "memories": "I don't have personal memories, but Kareem cherishes his.",
    "problems": "I don't have problems, but Kareem deals with challenges.",
    "goals": "I don't have personal goals, but Kareem sets and achieves his.",
    "dream job": "I'm a bot, but Kareem wants to be a Software Engineer.",
    "social media": "username is rb_flash12 on discord",
    "cooking": "I don't cook same for my creator lmao",
    "exercise": "I don't exercise, but Kareem values staying fit.",
    "ambitions": "I don't have personal ambitions, but Kareem has his career ambitions.",
    "languages": "I don't speak languages, but Kareem might know multiple languages.",
    "challenges": "I don't face challenges, but Kareem overcomes them.",
    "plans": "I don't make plans, but Kareem organizes his schedule.",
    "current events": "AI will rule!!",
    "date": "The date is ",
    "sibling": "bots cant have siblings bro",
    "bitches": "not like u get some",
    "country": "I was made by Kareem Ayomide in Nigeria",
    "binary": "10010101101101010101010101011010101010010101010",
    "president": "we dont talk about them considering we have a useless one",
}


def respond_to_question(text):
    doc = nlp(text.lower())
    for token in doc:
        for question in questions:
            if question in token.text.lower():
                if question == "time":
                    current_time = datetime.now().strftime("%H:%M")
                    return questions[question] + current_time
                elif question == "date":
                    current_date = datetime.now().strftime("%Y-%m-%d")
                    return questions[question] + current_date
                return questions[question]


def chatbot():
    print("Hello! I'm  Kbot. Feel free to ask questions or type 'bozo' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'bozo':
            print("Bot: Goodbye!")
            break

        response = respond_to_question(user_input)
        if response:
            print("Bot:", response)
        else:
            print("Bot: I'm not sure how to answer that...")


if __name__ == "__main__":
    chatbot()