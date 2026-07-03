import json
import os

import random
import string

FILE_NAME = "passwords.json"

def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

passwords = load_passwords()
MASTER_PIN = "1234"

#1
def show_passwords(passwords, reveal=False):
    if not passwords:
        print("No passwords found!\n")
    else:
        if reveal:
            for website in passwords:
                email = passwords[website]["email"]
                password = passwords[website]["password"]
                print(f"{website} -\n   email id: {email}\n   password: {password}\n")
        else:
            print("Saved Passwords:\n")
            for i, website in enumerate(passwords, start = 1):
                email = passwords[website]["email"]
                print(f"{i}. {website}\n   email id: {email}\n   password: ********\n")

#2
def add_password(passwords, website, email, password):
    passwords[website] = {
        "email": email,
        "password": password
    }
    print("\nPassword added successfully!\n")

#3
def save_passwords(passwords):
    sort_passwords(passwords)
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)

#4
def delete_password(passwords, website):
    del passwords[website]
    print("\nPassword deleted successfully!\n")

#5
def edit_password(passwords, website, email, password):
    passwords[website] = {
        "email": email,
        "password": password
    }
    print("\nPassword edited successfully!\n")

#6
def search_website(passwords, keyword):
    search_results = {}
    for entry in passwords:
        if keyword.lower() in entry.lower():
            search_results[entry] = passwords[entry]
    return search_results

#7
def reveal_password(passwords, website):
    get_pin()
    result = {}
    result[website] = passwords[website]
    return result

#8
def generate_random_password(length):
    character_groups = [string.ascii_lowercase , string.ascii_uppercase , string.digits , string.punctuation]
    while True:
        random_password = ""
        for i in range(4):
            random_password += random.choice(character_groups[i])
        characters = (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
        for i in range(length - 4):
            random_password += random.choice(characters)
        password = list(random_password)
        random.shuffle(password)
        random_password = "".join(password)
        print("\n",random_password,"\n")
        while True:
            response = input("Do you want to use this password?(y/n): ")
            if response == "y":
                return random_password
            elif response == "n":
                break
            else:
                print("Invalid response!")
        if response == "n":
            print("Generating new password ...")
            print("New password: ")
            continue

def get_valid_length():
    while True:
        length = input("Enter length of password (>=6): ")
        if length.isdigit():
            length = int(length)
            if length >= 6:
                return length
            else:
                print("Length should be atleast 6")
                continue
        else:
            print("Invalid input!")

def get_pin():
    while True:
        pin = input("Enter pin: ")
        if pin != MASTER_PIN:
            print("\nIncorrect Pin!\n")
            continue
        break

def get_valid_website(passwords, edit=False):
    while True:
        website = input("Enter website name: ")
        website = website.title()
        if not website:
            print("\nWebsite name cannot be empty!\n")
            continue
        if not edit:
            duplicate=False
            for entry in passwords:
                if website == entry:
                    print("\nWebsite already exists!\n")
                    duplicate=True
                    break
            if duplicate:
                continue
        if edit:
            for entry in passwords:
                if website == entry:
                    return entry
            print("\nWebsite does not exist!\n")
            continue
        return website
        
def get_valid_email():
    while True:
        email = input("Enter email id: ")
        if not email:
            print("\nEmail id cannot be empty!\n")
        else:
            return email
        
def get_valid_password():
    while True:
        password = input("Enter password: ")
        if not password:
            print("\nPassword name cannot be empty!\n")
        else:
            return password

def get_valid_keyword():
    while True:
        keyword = input("Enter keyword: ")
        if not keyword:
            print("\nKeyword cannot be empty!\n")
            continue
        return keyword
    
def sort_passwords(passwords):
    temp = dict(sorted(passwords.items(), key=lambda item: item[0].lower()))
    passwords.clear()
    passwords.update(temp)

def menu_system():
    menu = "1. Show Passwords\n" "2. Add Password\n" "3. Save Password\n" "4. Delete Password\n" "5. Edit Password\n" "6. Search Website\n" "7. Reveal Password\n" "8. Generate random password\n" "0. Exit\n"
    while True:
        print(menu)
        choice = input("Enter choice: ")
        if choice == "0":
            save_passwords(passwords)
            break
        elif choice == "1":
            show_passwords(passwords)
        elif choice == "2":
            website = get_valid_website(passwords)
            email = get_valid_email()
            password = get_valid_password()
            add_password(passwords, website, email, password)
            save_passwords(passwords)
        elif choice == "3":
            save_passwords(passwords)
            print("\nPasswords saved successfully!\n")
        elif choice == "4":
            website = get_valid_website(passwords, edit=True)
            delete_password(passwords, website)
            save_passwords(passwords)
        elif choice == "5":
            website = get_valid_website(passwords, edit=True)
            email = get_valid_email()
            password = get_valid_password()
            edit_password(passwords, website, email, password)
            save_passwords(passwords)
        elif choice == "6":
            keyword = get_valid_keyword()
            result = search_website(passwords, keyword)
            if not result:
                print("\nNo matches found!\n")
            else:
                show_passwords(result)
        elif choice =="7":
            website = get_valid_website(passwords, edit=True)
            result = reveal_password(passwords, website)
            show_passwords(result, reveal=True)
        elif choice == "8":
            length = get_valid_length()
            result = generate_random_password(length)
            print(f"\npassword: {result}\n")
        else:
            print("\nInvalid choice!\n")

menu_system()