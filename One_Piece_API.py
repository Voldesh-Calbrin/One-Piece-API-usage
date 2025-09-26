import requests as rq
import os
import sys
import json
    
def fruit_print(fruit):
    print('-' * 50)
    print(f"ID:          {fruit['id']}")
    print(f"Name:        {fruit['name']}")
    print(f"Type:        {fruit['type']}")
    print(f"Full Name:   {fruit.get('roman_name', "N/A")}")
    print(f"Description: {fruit['description']}")
    


def fruit_info():
    furit_url = os.getenv ("fruit_url", "https://api.api-onepiece.com/v2/fruits/en")
    fruit_rsp = rq.get(furit_url)

    if fruit_rsp.status_code == 200:
        data = fruit_rsp.json()

        for fruit in data:
            print(f"ID: {fruit['id']} Name: {fruit['name']}")

        inputted_id = int(input("Which fruit would you like to know more about? (1-206) "))

        for fruit in data:
            if fruit['id'] == inputted_id:
                fruit_print(fruit)

    else:
        print("wrong")
    

# ---------- Characters ----------
def character_print(character):
    print('-' * 50)
    print(f"ID:         {character['id']}")
    print(f"Name:       {character.get('name', "N/A")}")
    print(f"Hight:      {character['size']}")
    print(f"Age:        {character['age']}")
    print(f"Bounty:     {character.get('bounty', "N/A")}")
    print(f"Job:        {character['job']}")

def character_info():
    char_url = os.getenv("char_url", "https://api.api-onepiece.com/v2/characters/en")
    char_rsp = rq.get(char_url)

    if char_rsp.status_code == 200:
        data = char_rsp.json()

        for char in data:
            print(f"ID: {char['id']} Name: {char['name']}")

        inputted_id = int(input("Which character would you like to know more about? "))

        for char in data:
            if char['id'] == inputted_id:
                character_print(char)
                break
    else:
        print("Error fetching characters")


# ---------- Crews ----------
def crew_print(crew):
    print('-' * 50)
    print(f"ID:                 {crew['id']}")
    print(f"Name:               {crew['name']}")
    print(f"Total Bounty:       {crew['total_prime']}")
    print(f"Number of Members:  {crew['number']}")

def crew_info():
    crew_url = os.getenv("crew_url", "https://api.api-onepiece.com/v2/crews/en")
    crew_rsp = rq.get(crew_url)

    if crew_rsp.status_code == 200:
        data = crew_rsp.json()

        for crew in data:
            print(f"ID: {crew['id']} Name: {crew['name']}")

        inputted_id = int(input("Which crew would you like to know more about? "))

        for crew in data:
            if crew['id'] == inputted_id:
                crew_print(crew)
                break
    else:
        print("Error fetching crews")




def menu():
    while True:
        print("\n--- One Piece Info Menu ---")
        print("1. Devil Fruits")
        print("2. Characters")
        print("3. Crews")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            fruit_info()
        elif choice == "2":
            character_info()
        elif choice == "3":
            crew_info()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
