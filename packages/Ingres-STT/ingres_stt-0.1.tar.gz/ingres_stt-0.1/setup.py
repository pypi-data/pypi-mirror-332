from setuptools import setup,find_packages

setup(
    name='Ingres-STT',
    version='0.1',
    author='yousuf kasmani',
    author_email='yousuf.kasmani007@gmail.com',
    description='this is speech to text package created by yousuf kasmani'
)
packages = find_packages(),
install_requirements = [
    'selenium',
    'webdriver_manager'
]