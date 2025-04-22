import os
import subprocess

current_dir = os.getcwd()

def run_shell_command(command):
    global current_dir
    if command.startswith("cd "):
        # Change the directory and update the current_dir variable
        new_dir = command.split(" ", 1)[1]
        if os.path.isdir(new_dir):
            os.chdir(new_dir)
            current_dir = os.getcwd()
        else:
            print(f"Error: Directory {new_dir} does not exist.")
    else:
        subprocess.run(command, shell=True)

# Example usage
run_shell_command("cd projects")
print("Current Directory:", os.getcwd())  # Verifying directory change
