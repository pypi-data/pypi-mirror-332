from setuptools import setup, find_packages

setup(
    name="Final-CPP-Project",
    version="0.2.7", #업로드할꺼면 여기서 수정 후 라이브러리 업로드 가능 > 버전 규칙 0.1.0 → 0.1.1 (작은 버그 수정) /0.1.0 → 0.2.0 (새로운 기능 추가) /0.1.0 → 1.0.0 (대규모 변경)
    author="x24142816-JiyoungKim",
    author_email="x24142816@student.ncirl.ie",
    description="This is Remote_WorkTime_Tracker for CPP's project",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jiyoung0716/Final_CPP_Project",
    packages=find_packages(),
    install_requires=[
        'asgiref==3.8.1',
        'attrs==20.3.0',
        'aws-cfn-bootstrap==1.4.post31',
        'awscli==1.25.3',
        'awscrt==0.19.19',
        'Babel==2.9.1',
        'boto3==1.37.3',
        'botocore==1.37.3',
        'cffi==1.14.5',
        'chardet==4.0.0',
        'chevron==0.13.1',
        #'cloud-init>=22.2.2', > PyPI 제공하지 않는 부분
        'colorama==0.4.4',
        'configobj==5.0.6',
        'cryptography==36.0.1',
        'dbus-python==1.2.18',
        'distro==1.5.0',
        'Django==4.2.19',
        'docutils==0.16',
        'ec2-hibinit-agent==1.0.8',
        'git-remote-codecommit==1.17',
        'gpg==1.15.1',
        'idna==2.10',
        'ikp3db==1.4.2',
        'Jinja2==2.11.3',
        'jmespath==0.10.0',
        'jsonpatch==1.21',
        'jsonpointer==2.0',
        'jsonschema==3.2.0',
        'libcomps==0.1.20',
        'lockfile==0.12.2',
        'MarkupSafe==1.1.1',
        'mercurial==5.7.1',
        'netifaces==0.10.6',
        'oauthlib==3.0.2',
        'packaging==21.3',
        'pillow==11.1.0',
        'ply==3.11',
        'prettytable==0.7.2',
        'prompt-toolkit==3.0.24',
        'pycparser==2.20',
        'pyparsing==2.4.7',
        'pyrsistent==0.17.3',
        'pyserial==3.4',
        'PySocks==1.7.1',
        'python-daemon==2.3.0',
        'python-dateutil==2.8.1',
        'pytz==2022.7.1',
        'PyYAML==5.4.1',
        'release-notification==1.2',
        'requests==2.25.1',
        'rpm==4.16.1.3',
        'ruamel.yaml==0.16.6',
        'ruamel.yaml.clib==0.1.2',
        's3transfer==0.11.3',
        'selinux==3.4',
        'sepolicy==3.4',
        'setools==4.4.1',
        'six==1.15.0',
        'sqlparse==0.5.3',
        'support-info==1.0',
        'systemd-python==235',
        'typing_extensions==4.12.2',
        'urllib3==1.25.10',
        'wcwidth==0.2.5'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
