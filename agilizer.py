import webbrowser
import json
import os
import pyfiglet  # Importing the pyfiglet library

# Path to the configuration file
CONFIG_FILE = "links_config.json"

# Load links from the JSON file
def load_links():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading the configuration file. Resetting to default links.")
            return {}
    return {}

# Save links to the JSON file
def save_links(links):
    try:
        with open(CONFIG_FILE, "w") as file:
            json.dump(links, file)
    except IOError:
        print("Error saving the links. Changes might not be preserved.")

# Add or edit a link
def add_link(links):
    new_link = input("Enter the new link URL: ").strip()
    if not new_link.startswith("http"):
        print("Invalid link. It must start with 'http'.")
        return

    # Determine the next available number
    next_number = str(max(map(int, links.keys())) + 1 if links else 1)
    links[next_number] = new_link
    save_links(links)
    print(f"Link added with number {next_number}.")

# Open a link
def open_link(links):
    number = input("Enter the link number to open: ").strip()
    if number in links:
        webbrowser.open(links[number])
        print(f"Opened: {links[number]}")
    else:
        print("No link associated with this number.")

# Delete a link
def delete_link(links):
    number = input("Enter the number of the link you want to delete: ").strip()
    if number in links:
        del links[number]
        save_links(links)
        print(f"Link associated with number {number} has been deleted.")
    else:
        print("No link associated with this number.")

# Show all links
def show_all_links(links):
    if links:
        print("\nSaved Links:")
        for number, url in links.items():
            print(f"{number}: {url}")
    else:
        print("No links available.")

# Show help
def show_help():
    print("\n=== Agilizer Help ===")
    print("1. Add/Edit link: Assigns a number to a link or updates an existing one.")
    print("2. Open link: Opens the link associated with a number in the browser.")
    print("3. Show all links: Lists all numbers and their associated links.")
    print("4. Delete link: Removes the association of a number with a link.")
    print("5. Help: Displays this help message.")
    print("6. Exit: Closes the program.")

# Main menu
def main():
    links = load_links()

    # Display "AGILIZER" in ASCII Art (uppercase)
    ascii_art_agilizer = pyfiglet.figlet_format("AGILIZER")
    print(ascii_art_agilizer)  # Large text for "AGILIZER"

    # Display "version 1.0" and "created by https://github.com/Juliano1086"
    print("version 1.0")
    print("created by https://github.com/Juliano1086\n")

    print("\n=== Agilizer: Link Manager ===")  # Title displayed only once

    # Display menu options only once at the start
    menu_options = """
1. Add/Edit link
2. Open link
3. Show all links
4. Delete link
5. Help
6. Exit
"""
    print(menu_options)  # Menu displayed here only once

    while True:
        choice = input("Choose an option: ")

        if choice == "1":
            add_link(links)
        elif choice == "2":
            open_link(links)
        elif choice == "3":
            show_all_links(links)
        elif choice == "4":
            delete_link(links)
        elif choice == "5":
            show_help()
        elif choice == "6":
            print("Exiting Agilizer...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
