from setuptools import setup,find_packages
setup(
    name='JarvisPackage',
    version='0.1',
    author='Aman',
    author_email='amanmishra3496@gmail.com',
    description='this is first project in python created by aman mishra'
)
packages=find_packages(),
install_requirements=[
    'selenium',
    'webdriver_manager'
]

