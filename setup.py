import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyrosenv',
    version='0.0.1',
    author='Omri Rozenzaft',
    author_email='omrirz@gmail.com',
    url='https://github.com/omrirz/pyrosenv.git',
    description='Set an environment for easy work with ROS in python without setting things up',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix"
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyros_setup',
        'rospkg',
        'defusedxml'
    ],
)
