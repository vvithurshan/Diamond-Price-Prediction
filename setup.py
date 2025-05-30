# Import necessary functions from setuptools and typing
from setuptools import find_packages, setup
from typing import List

# Define a constant for the editable install line often found in requirements.txt
HYPHEN_E_DOT = '-e .'

# Function to read requirements from a file
def get_requirements(file_path: str) -> List[str]: # Renamed from get_requirments for correct spelling
    """
    This function reads a requirements file, processes the lines,
    and returns a list of dependency strings.
    It also removes the '-e .' line if present.
    """
    requirements = []
    # Open the specified file
    with open(file_path) as file_obj:
        # Read all lines from the file
        requirements = file_obj.readlines()
        # Remove newline characters from each requirement
        requirements = [req.replace("\n", "") for req in requirements]

        # If '-e .' is in the list (used for editable installs), remove it
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

# Main setup configuration for the package
setup(
    name='DiamondPricePrediction',  # Name of the package
    version='0.0.1',  # Version of the package
    author='Vithurshan',  # Author's name
    author_email='vvithurshan@gmail.com',  # Author's email
    # install_requires=get_requirements('requirements.txt'), # Option 1: Read dependencies from requirements.txt
    install_requires=get_requirements('requirements.txt'), # Option 2: Manually specify dependencies)
    packages=find_packages()  # Automatically find all packages in the project
)