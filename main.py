import os
from datetime import datetime

# Determine the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# File to update (in the same directory as the script)
file_to_update = os.path.join(script_dir, "daily_update.txt")

def update_file():
    # Append the current date and time to the file
    with open(file_to_update, "a") as f:
        f.write(f"Streak maintained on: {datetime.now()}\n")

def git_commit_and_push():
    # Change to the script's directory (repository path)
    os.chdir(script_dir)
    
    # Run Git commands to add, commit, and push
    os.system("git add .")
    os.system(f'git commit -m "Daily streak update: {datetime.now().strftime("%Y-%m-%d")}"')
    os.system("git push origin master")  # Replace 'main' with your branch name if necessary

if __name__ == "__main__":
    # Ensure the text file exists before updating
    if not os.path.exists(file_to_update):
        with open(file_to_update, "w") as f:
            f.write("Daily update log:\n")  # Initial content for the file
    
    # Perform the update and push
    update_file()
    git_commit_and_push()
