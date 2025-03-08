from setuptools import setup, find_packages

setup(
    name='board2048',
    version='1.0.1',
    description='2048 game logic in Python',
    author='Mark Kwong',
    author_email='mark_kwong@fuhsd.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List any dependencies here (if you have any)
    ],
    zip_safe=True,  # Makes the package non-easily accessible
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
