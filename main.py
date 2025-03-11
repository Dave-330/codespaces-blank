import time
print("Welcome to the Elite 101 Chatbox!")
name = input("What is your name?: ")
age = input("Hello " + name + ", how old are you? ")
print("Welcome " + name + "! Oh wow, I wish I was " + age +".")
time.sleep(2)
print("How can I help you?: ")
def display_menu():
    print("1. Know if you can Vote")
    print("2. Know if you can Drive")
    print("3. Know if you can run for president")
    print("4. Exit\n")
    if choice == "1":

        print("1, let’s find out if you can vote ")

    elif choice == "2":

        print(1"Great, you have to be 18 yers old to vote")

    elif choice == "3":

        print(1" oh ok!, thank you so much")

        
display_menu()
choice = int(input("Enter the number of your choice: "))
if choice == 4:
    print("Thanks for chatting with me. Goodbye!!")
