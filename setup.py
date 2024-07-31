
# to build entire application as package and publish as a library we use setup.py


from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:

    '''
    this function will return a list of requirements

    '''

    requirements = []

    with open(file_path) as file_obj :
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        print(requirements)

    return requirements


setup(
    name = "MLProject",
    version ='0.0.1',
    author="Anitt",
    author_email="an329828@dal.ca",
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
)