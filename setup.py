from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Hareesh Madasi',
    author_email='harischandra1995@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","pypdf2"],
    packages=find_packages()
)