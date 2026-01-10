import os 
from pathlib import Path 
import logging 


logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s" 

) 

while True:
    project_name = input("Enter your project name:") 

    if project_name != "":
        break 
    else:
        logging.info("Project name cannot be empty. Please try again.") 

logging.info(f"Creating project by name: {project_name}") 


# list of files: 

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
    ""


]