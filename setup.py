import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Analyze",                     # This is the name of the package
    version="1.0.0",                        # The initial release version
    author="Henry Uwakwe",
    author_email="Henry.uwakxy@gmail.com",                     # Full name of the author
    description="Analyze is a python library that provides comprehensive statistical analysis of a dataframe in 5 lines of code. It creates significant insight for data scientists, analysts and machine learning engineers, enabling quick understanding of a dataset.",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],  
    url = 'https://github.com/Chaboddunamis/analyze',  
    keywords = ['data-science', 'machine-learning', 'python', 'statistics'],                              # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["Analyze"],             # Name of the python package
    package_dir={'':'Analyze/src'},     # Directory of the source code of the package
    install_requires=[
        'pandas',
        'pandas_profiling',
        'numpy',
        'scipy',
    ]                     # Install other dependencies if any
)