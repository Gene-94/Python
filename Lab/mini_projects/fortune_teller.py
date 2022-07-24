import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"    
    elif answerNumber == 4:
        return "Reply hazy, try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtfull"

while True:
    r = random.randint(1, 9)
    fortune = getAnswer(r)  
    print("\nState your question !")
    qest = input(">")
    if qest == 'exit':
        break
    if qest == 'help':
        print("Just enter your question and the seer will provide you with an answer to your liking, if you ask times enough...")
        print("'exit' releases the seer and ends the question asking.")
        continue
    print("\n"+fortune)