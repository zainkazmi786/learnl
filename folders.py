import os

# Define folder and file structure
structure = {
    "learnl": [
        "__init__.py",
        "main.py",
        "shell.py",
        "llm.py",
        "utils.py"
    ],
    ".": [  # Root level files
        "setup.py",
        "requirements.txt",
        "README.md"
    ]
}

# Create directories and files
for folder, files in structure.items():
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder: {folder}")
    for file in files:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("")  # Empty file for now
            print(f"Created file: {file_path}")

print("\n✅ Project scaffold created successfully.")
