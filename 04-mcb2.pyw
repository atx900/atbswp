'''
Practice Project 04: MultiClipBoard
- Manages multiple pieces of text that are copied and pasted to the clipboard.

Objective(s):
- Extend the existing program to include the following features:
    delete <save_name>      - Deletes a specific save name and its associated content
    delete                  - Deletes all save names and their associated content

Implemented additional minor change(s):
- Display program usage and requirements information
- Feedback on chosen keyword (save <save_name> | list | delete | delete <save_name>)
- Python 3.6x f-string
- Rename keyword 'delete' to 'purge' to refer deletion of all existing save names & associated content
- User confirmation for keywords 'delete' and 'purge'
'''
#! python3

import shelve, pyperclip, sys

appVersion = "0.2"

usageText = """
Usage:  python3 pwb.pyw list                        - Copies a list of existing saved names to clipboard
        python3 pwb.pyw save <save_name>            - Saves clipboard content to the chosen 'save name'
        python3 pwb.pyw delete <save_name>          - Deletes an existing 'save name' and its associated content
        python3 pwb.pyw purge                       - Deletes all stored saved name and associated content
        python3 pwb.pyw                             - Displays how to use the program's keywords (delete|list|purge|save)

Note:   Requires Python 3.6x and pyperclip module to run properly.
"""

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(f"Save Name '{sys.argv[2]}' stored.\n")

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    targetSaveName = sys.argv[2]
    deletionResponse = input(f"Warning: Unrecoverable deletion of save name '{targetSaveName}'. Continue [y/n]? ").lower()
    if deletionResponse == 'y':
        try:
            del mcbShelf[str(targetSaveName)]
            print(f"Successfully deleted save name '{targetSaveName} and its content'.\n")
        except KeyError:
            print(f"Warning: save name '{targetSaveName}' does not exist.\n")
    else:
        print(f"Deletion of save name '{targetSaveName}' aborted.\n")

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print("List of existing save names copied on clipboard.\n")

    elif sys.argv[1].lower() == 'purge':
        purgeResponse = input("Warning: Unrecoverable deletion of all save names. Continue [y/n]? ").lower()
        if purgeResponse == 'y':
            purgeSavedNames = list(mcbShelf.keys())
            for deleteItem in range(len(purgeSavedNames)):
                del mcbShelf[str(purgeSavedNames[deleteItem])]
            print("Successfully purged all existing save name and content.\n")

        else:
            print("Purge of save names aborted.\n")

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print("Clipboard content has been updated.\n")
else:
    print(f"\nMultiClipBoard (MCB) Utility v.{appVersion}")
    print(f"{usageText}")

mcbShelf.close()
