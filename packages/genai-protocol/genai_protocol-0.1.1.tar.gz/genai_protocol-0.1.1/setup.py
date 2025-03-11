from setuptools import setup, find_packages

setup(
    name='genai-protocol',
    version='0.1.1',
    packages=find_packages(),
    author='genai-protocol',
    author_email='',
    description='Network connector for AI tools',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[
        "wcwidth==0.2.13",
	    "websockets~=15.0",
	    "colorlog==6.9.0",
        "azure-messaging-webpubsubservice==1.2.1",
    ],
)
