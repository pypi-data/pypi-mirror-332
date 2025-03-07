from setuptools import setup, find_packages

setup(
    name='board2048',
    version='1.0.0',
    description='2048 game logic in Python',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List any dependencies here (if you have any)
    ],
    zip_safe=True,  # Makes the package non-easily accessible
)
