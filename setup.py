from setuptools import find_packages, setup
from typing import List  # <-- CORRECTED LINE

hyphen = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements

setup(
    name='myproject',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)