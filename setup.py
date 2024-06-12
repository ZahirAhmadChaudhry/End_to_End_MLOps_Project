from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file: str) -> List[str]:
    '''
    Read requirements file and return list of requirements
    '''
    requirements = []
    with open(file) as f:
        requirements = f.readlines()
        requirements= [req.replace("\n", "")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name='End_to_End_ML_Project',
    version='0.0.1',
    author='ZahirAhmad',
    author_email= 'zahirahmadchaudhry@gmail.com',
    packages=find_packages(),
    license='MIT',
    description='End to End ML Project',
    long_description=open('README.md').read(),
    install_requires= get_requirements('requirements.txt')
)

