import datetime

print("Chatbot: Welcome!")

while True:
        user = input("You: ").lower()

        if user =="hello" or user == "hi":
            print("Chatbot: Hello! I am glad to chat with you.")

        elif "how are you" in user:
            print("Chatbot: I'm doing well. Thank you!")
        
        elif "your name" in user:
            print("Chatbot: I am just a rule-based chatbot.")
        
        elif "help" in user:
            print("Chatbot: I am here to assist you , please ask.")

        elif "time" in user:
            currenttime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Chatbot: Current time is", currenttime)

        elif "date" in user:
            currentdate = datetime.datetime.now().strftime("%d-%m-%Y")
            print("Chatbot: Today's date is", currentdate)

        elif "day" in user:
            now = datetime.datetime.now().strftime("%A")
            print("Chatbot: Today is", now)

        elif "do you like me" in user:
            print("Chatbot: yes! I love to chat with you")

        elif "how was you created" in user:
            print("Chatbot: I was created using Python and rule-based logic.")

        elif "how was your day" in user:
            print("Chatbot: My day was fine.")

        elif "motivate me" in user:
           print(" Chatbot: Believe in yourself. Consistency is the key to success.")

        elif "what do you think about me" in user:
            print("Chatbot: I think you are a great person to talk to.")

        elif "bye" in user:
            print("Chatbot: Goodbye! Have a wonderful day.")
            break

        else:
            print("Chatbot: Sorry, I do not understand ")