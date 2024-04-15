import random
import smtplib
import nltk
from nltk.chat.util import Chat, reflections

class UserLogin:
    def __init__(self):
        self.users = {"john_doe": {"email": "john@example.com", "password": "password123"},
                      "jane_smith": {"email": "jane@example.com", "password": "password456"}}
        self.logged_in_user = None
    
    def send_otp(self, email):
        otp = random.randint(1000, 9999)
        print(f"OTP sent to {email}: {otp}")
        return otp
    
    def login(self, username, password):
        if username in self.users and password == self.users[username]["password"]:
            self.logged_in_user = username
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False

    def register(self, username, password):
        if len(username) <= 10 and len(password) <= 10:
            self.users[username] = {"email": f"{username}@example.com", "password": password}
            print("Registered!")
            return True
        else:
            print("Username and password must be 10 characters or less.")
            return False

class HistoryChatbot:
    def __init__(self):
        self.topics = [
            "Ancient civilizations",
            "World Wars",
            "Renaissance",
            "Real time chat with history people",
            "Historical events",
        ]
        self.responses = {
            "shivaji": [
                (r'(.*)your vision(.*)', [
                    "My vision for the Maratha Empire is to establish a kingdom that upholds righteousness and protects the people."
                ]),
                (r'(.*)strateg(y|ies)(.*)', [
                    "Through strategic warfare and alliances, we will ensure the prosperity and security of our kingdom."
                ]),
                (r'(.*)alliance(.*)', [
                    "Alliances are crucial in our mission to establish a strong and prosperous Maratha Empire."
                ]),
                (r'(.*)', [
                    "I, Shivaji Maharaj, believe in the valor and strength of the Maratha warriors. Together, we shall strive for independence and justice."
                ])
            ]
        }
    
    def introduce(self):
        print("Welcome to HIS-STORY, your history chatbot!")
        print("I can provide information on various historical topics.")
        print("Feel free to ask me anything about history!\n")
    
    def show_contents(self):
        print("Here are the topics available in HIS-STORY:")
        for index, topic in enumerate(self.topics, start=1):
            print(f"{index}. {topic}")
    
    def start_chat(self):
        self.introduce()
        self.show_contents()
        
        while True:
            user_input = input("\nWhat would you like to learn about? (Enter the topic number or type 'exit' to end): ")
            
            if user_input.lower() == "exit":
                print("Thank you for using HIS-STORY. Goodbye!")
                break
            elif user_input.isdigit():
                index = int(user_input) - 1
                if 0 <= index < len(self.topics):
                    print(f"\nYou chose to learn about: {self.topics[index]}")
                    if self.topics[index] == "Real time chat with history people":
                        self.real_time_chat()
                    else:
                        self.provide_information(self.topics[index])
                else:
                    print("Invalid topic number. Please try again.")
            else:
                print("Invalid input. Please enter the topic number or 'exit'.")

    def provide_information(self, topic):
        print("\nHere's some information about", topic)
        print("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        print("Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        print("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
        print("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        print("Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    def real_time_chat(self):
        print("Welcome to Real Time Chat with History People!")
        print("Who would you like to chat with?")
        print("1. Shivaji")
        print("Enter 'exit' to end the chat.")
        
        while True:
            user_input = input("\nChoose a person to chat with: ").strip().lower()

            if user_input == "exit":
                print("Exiting Real Time Chat with History People.")
                break
            elif user_input == "shivaji":
                self.chat_with_shivaji()
            else:
                print("Invalid choice. Please select a valid option.")

    def chat_with_shivaji(self):
        chatbot = Chat(self.responses["shivaji"], reflections)
        print("You are now chatting with Chatrapathi Shivaji. Ask anything about his vision, strategies, or empire!")
        print("Enter 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ").strip().lower()

            if user_input == "exit":
                print("Exiting chat with Shivaji.")
                break
            else:
                response = chatbot.respond(user_input)
                print("Shivaji:", response)

if __name__ == "__main__":
    print("Welcome to HIS-STORY!")

    login_system = UserLogin()

    while True:
        new_or_existing = input("Are you a new user (N) or an existing user (E)? ").strip()

        if new_or_existing == "N":
            while True:
                username = input("Enter your username: ").strip().lower()
                password = input("Enter your password: ").strip()
                if login_system.register(username, password):
                    break
            chatbot = HistoryChatbot()
            chatbot.start_chat()
            break
        elif new_or_existing == "E":
            while True:
                existing_username = input("Enter your username: ").strip().lower()
                existing_password = input("Enter your password: ").strip()
                if login_system.login(existing_username, existing_password):
                    break
            chatbot = HistoryChatbot()
            chatbot.start_chat()
            break
        else:
            print("Invalid input. Please enter 'N' for new user or 'E' for existing user.")
            continue

