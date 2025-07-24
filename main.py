import os
from prompts.storage import load_data, save_data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_next_id(prompts):
    """Returns the next available ID for a new prompt."""
    if not prompts:
        return 1
    return max(p['id'] for p in prompts) + 1

def add_prompt(prompts):
    """Adds a new prompt to the list."""
    clear_screen()
    print("Add new prompt")
    title = input("enter prompt title:")
    text = input("enter prompt text:")
    
    new_prompt = {
        "id": get_next_id(prompts),
        "title": title,
        "text": text
    }
    
    prompts.append(new_prompt)
    save_data(prompts)
    print("\n prompt added successfully!")
    input("\n Press Enter to return to the main menu...")
    
def list_prompts(prompts):
    """Lists all saved prompts."""
    clear_screen()
    print("List of saved prompts:")
    if not prompts:
        print("No prompts saved yet.")
    else:
        for prompt in sorted(prompts, key=lambda p: p['id']):
            print(f" [{prompt['id']}] {prompt['title']}")
            
    print("\n---------------------------------")
    input("\n Press Enter to return to the main menu...")
    
def view_prompt(prompts):
    """Views a specific prompt by its ID."""
    clear_screen()
    print("View Prompt")
    try:
        prompt_id = int(input("Enter prompt ID: "))
        prompt = next((p for p in prompts if p['id'] == prompt_id), None)
        
        if prompt:
            print("---------------------------------")
            print(f"ID: {prompt['id']}")
            print(f"Title: {prompt['title']}")
            print(f"Text: {prompt['text']}")
            print("---------------------------------")
        else:
            print("Prompt not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")
    input("\n Press Enter to return to the main menu...")
    
def delete_prompt(prompts):
    """Deletes a specific prompt by its ID."""
    clear_screen()
    print("Delete Prompt")
    try:
        prompt_id = int(input("Enter prompt ID to delete: "))
        
        # create a new list excluding the prompt to be deleted
        new_prompts = [p for p in prompts if p['id'] != prompt_id]
        
        if len(new_prompts) < len(prompts):
            save_data(new_prompts)
            print("Prompt deleted successfully.")
            return new_prompts
        else:
            print("Prompt not found.")
            return prompts
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return prompts
    finally:
        input("\n Press Enter to return to the main menu...")
        
def main_menu():
    """Displays the main menu and handles user input."""
    prompts = load_data()
    
    while True:
        clear_screen()
        print("Prompt Saver v1.0")
        print("What would you like to do?")
        print("\n [1] Add a new prompt")
        print(" [2] List all prompts")
        print(" [3] View a prompt")
        print(" [4] Delete a prompt")
        print(" [0] Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            add_prompt(prompts)
        elif choice == '2':
            list_prompts(prompts)
        elif choice == '3':
            view_prompt(prompts)
        elif choice == '4':
            delete_prompt(prompts)
        elif choice == '0':
            print("\nThank you for using Prompt Saver! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            print("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
