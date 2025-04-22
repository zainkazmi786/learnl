# Learnl Command-Line Tool

`learnl` is an interactive command-line tool that allows you to run shell commands in a user-friendly way with suggestions and more. This README provides steps to set up and run the project.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)


## Requirements

Before you start, make sure you have the following installed:
- **Python 3.12+**: The latest version of Python is required.
- **pip**: Python's package installer.

Optionally, you can use **pipx** for a self-contained installation of the tool.

## Installation

1. **Clone the repository:**
   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/zainkazmi786/learnl.git
   cd learnl

2. **Set up a virtual environment (recommended):**  
   It's a good practice to create a virtual environment to isolate dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install Dependencies**

    ```
    pip install -r requirements.txt
4. **Alternative installation with pipx (recommended for CLI tools)**

   You can install the package globally with pipx:

    ```
    pipx install --editable .
5. **Optional pipx installation with dependencies:**

   For a complete isolated environment including all dependencies:

    

    ```
    pipx install --editable . --include-deps
    
This will install the tool globally and handle dependencies automatically.

## Usage

### Run the Tool

Once the project is installed, you can run the tool from the command line:

```
learnl
```
### Example Commands

- **Change Directory**: Navigate between directories:

  ```bash
  learnl make a folder test

