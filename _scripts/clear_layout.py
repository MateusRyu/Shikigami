import sys
import os
import time

def show_help():
    print(f"Usage: {sys.argv[0]} <path_to_directory>")
    print("Removes the 'layout:' line from all Markdown files in the specified directory.")
    sys.exit(0)

def validate_arg():
    if len(sys.argv) != 2:
        print(f"Path is required. Check '{sys.argv[0]} --help' for help.")
        sys.exit(1)

    if len(sys.argv) == 2 and sys.argv[1] == '--help':
            show_help()

def check_directory(base_dir):
    if not os.path.isdir(base_dir):
        print(f"The path '{base_dir}' is not a valid directory.")
        sys.exit(1)

def request_confirmation(attempts):
    print(f"layout property in all files in '{base_dir}' will be erased. This action cannot be undo...\n")
    confirm = input("(Y)es or (N)o\nConfirm: ")

    if confirm.lower() in ["no", "n"]:
        print(f"Action cancelled")
        sys.exit(0)
    elif confirm.lower() in ["yes", "y"]:
        print(f"Action confirmed")
    else:
        if attempts < 3:
            print("\nInvalid request...\n")
            time.sleep(1)
            request_confirmation(attempts+1)
        else:
            print("Too many invalid answers. Action cancelled!")
            sys.exit(1)

def remove_layout_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        lines = [line for line in lines if not line.strip().startswith('layout: ')]

        with open(file_path, 'w') as file:
            file.writelines(lines)
    except IOError as e:
        print(f"Error processing file {file_path}: {e}")

def process_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                remove_layout_line(file_path)

validate_arg()
base_dir = sys.argv[1]
check_directory(base_dir)
request_confirmation(0)
process_files(base_dir)