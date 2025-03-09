from setuptools import setup, find_packages

setup(
    name="Final-CPP-Project",
    version="0.4.1", 
    author="x24142816-JiyoungKim",
    author_email="x24142816@student.ncirl.ie",
    description="This is Remote_WorkTime_Tracker for CPP's project",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jiyoung0716/Final_CPP_Project",
    packages=find_packages(),
    install_requires=[
        'boto3==1.37.8',
        'botocore==1.37.8',
        'Django==4.2.19',
        'setuptools==59.6.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
