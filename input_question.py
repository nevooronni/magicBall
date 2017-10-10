import random
import time
answers = [
"It is certain",
"As I see it, yes",
"Reply hazy try again",
"Don't count on it",
"It is decideldly",
"Most likely",
"Ask again later",
"My reply is no",
"Without a doubt",
"Outlook good",
"Better not tell you now",
"My sources say no",
"Yes definetely",
"Yes",
"Cannot predict now",
"Outlook not so good",
"You may rely on it",
"Signs point to yes",
"Concentrate and ask again",
"Very doubtful"
]

while True:
    input("Ask me the all knowing 8 Ball a closed-ended question?")
    for i in range(0,3):
        print("Searching......")
        time.sleep(1)
    print(random.choice(answers))
