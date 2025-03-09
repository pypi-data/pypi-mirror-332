from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='tubiu',
    version='1.0.0',
    description='tubiu',
    long_description=long_description,
    author='huang yi yi',
    author_email='363766687@qq.com',
    packages=find_packages(),
    package_data={
        "tubiu": ['*.pyd'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tubiu=tubiu.tubiu:main', 
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        "watchdog",
        "paramiko",
        "pycryptodome",
        "pywin32",
        "rich",
        "plyer",
        "mpmath",
    ],
)