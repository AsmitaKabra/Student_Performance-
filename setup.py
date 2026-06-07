##build machine learning project as a package and use it as a package in other projects too
#also deploy it

from typing import List
from setuptools import find_packages,setup

HYPHEN_E_DOT = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
name='ml_project',
version='0.0.1',
author = 'Asmita',
author_email='asmita.kabra49@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)