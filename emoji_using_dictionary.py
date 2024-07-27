message = (input("how you doing:")).lower()

def emoji_converter(message):
    words = message.split(" ")
    #the dictionary for the emoji 
    emojis = { 
        "sad":"😢",
        "happy":"😀",
        "great": "😤",
        "crying":"😭",
        "i":"you are "}
    
    for word in words:
        output = emojis.get(word, word) + ""
    return output



result = emoji_converter(message)
print(result)
