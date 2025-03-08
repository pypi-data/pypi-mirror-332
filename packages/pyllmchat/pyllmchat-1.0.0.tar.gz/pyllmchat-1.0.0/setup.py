from setuptools import setup, find_packages

setup(
    name='pyllmchat',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/mdrehan4all/pyllmchat',
    license='MIT',
    author='Md Rehan',
    author_email='mdrehan4all@gmail.com',
    description='One library for all LLM related task',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='llmchat genai',
    python_requires='>=3.6',
    install_requires=[],
)