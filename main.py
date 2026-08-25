def show_menu():
    with open("notes.txt","r") as f:
        data = f.read()
        print(data)


def add_data(work):
    with open("notes.txt","a") as f:
        f.write("\n" + work)


def refresh_data():
    with open("notes.txt","w") as f:
        pass


def update_specific_notes():
    try:
        with open("notes.txt","r") as f:
            data = f.read()
            user_edit_old = input("Enter which word do you want to change : ").strip().lower()
            user_edit_new = input(f"Instead of {user_edit_old} what do you want to write : ").strip().lower()
            updated_data = data.replace(user_edit_old, user_edit_new)

        with open("notes.txt","w") as f:
            f.write(updated_data)
        
        print("Note updated successfully...")
    
    except FileNotFoundError:
        print("File does not exist.")



print("<-: Welcome to notes app :-> ".center(300))

print("""Please select your choice from the given features : 
      
      1. Show Menu
      2. Add Data
      3. Refresh Data
      4. update specific notes
      5. Exit

    """)



while True:
    
    user_choice = input("Enter your choice (1,2,3,4,5) : ")

    if user_choice == "1":
        show_menu()
    
    elif user_choice == "2":
        work = input("Enter what you want to write : ").strip().lower()
        add_data(work)
        print("Data added successfully...")
    
    elif user_choice == "3":
        refresh_data()
        print("Data refreshed successfully...")


    elif user_choice == "4":
        update_specific_notes()
    
    elif user_choice == "5":
        print("Exiting...\nGood Bye!!")
        break

    else:
        print("Please enter a valid choice(1,2,3,4,5)..")