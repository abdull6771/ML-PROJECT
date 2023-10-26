from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT ="-e ."

def get_requirements(path: str) -> List[str]:
    ''''
    This fuction will return list of requirements and remove /n from each line
     '''
    requirements = []
    with open(path) as f:
        requirements =  f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
        

setup(
    name="mlproject",
    author="Abdullahi",
    author_email="abdull6771@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)