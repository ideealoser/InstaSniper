import requests
import re
import time
import os

def get_id_from_username(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Instagram 155.0.0.37.107 Android",
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            match = re.search(r'"profilePage_([0-9]+)"', response.text)
            if match:
                return match.group(1)
    except Exception:
        pass
    return None

def get_username_from_id(user_id):
    url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
    headers = {
        "User-Agent": "Instagram 155.0.0.37.107 Android",
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['user']['username']
    except Exception:
        pass
    return None

def save_id(username, user_id):
    with open("id.txt", "a", encoding="utf-8") as file:
        file.write(f"{username} - {user_id}\n")

def open_file():
    try:
        with open("id.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("No saved IDs found.")

def falling_effect(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def falling_menu(lines, delay=0.07):
    for line in lines:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.002)
        print()
        time.sleep(delay)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt):
    user_input = input(prompt).strip()
    return user_input

def menu():
    while True:
        clear_screen()
        falling_menu([
            "[ 1 ] Search by username",
            "[ 2 ] Search by ID",
            "[ 3 ] View saved IDs",
            "[ 4 ] Exit"
        ])
        
        print()
        choice = get_user_input(": ")

        if choice == '1':
            username = get_user_input("Enter username: ")
            if username:
                user_id = get_id_from_username(username)
                if user_id:
                    clear_screen()
                    falling_effect(f"ID of @{username}: {user_id}\n")
                    save_id(username, user_id)
                else:
                    clear_screen()
                    falling_effect(f"Could not find ID for @{username}.\n")
                time.sleep(10)
                clear_screen()

        elif choice == '2':
            user_id = get_user_input("Enter user ID: ")
            if user_id:
                username = get_username_from_id(user_id)
                clear_screen()
                if username:
                    falling_effect(f"Username for ID {user_id}: @{username}\n")
                    save_id(username, user_id)
                else:
                    falling_effect(f"Could not find username for ID {user_id}.\n")
                time.sleep(10)
                clear_screen()

        elif choice == '3':
            open_file()
            time.sleep(10)
            clear_screen()

        elif choice == '4':
            falling_effect("Exiting...")
            break

        else:
            clear_screen()
            menu()  

if __name__ == "__main__":
    menu()
