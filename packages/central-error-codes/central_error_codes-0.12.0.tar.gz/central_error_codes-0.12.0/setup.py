from setuptools import setup, find_packages

setup(
    name='central_error_codes',  # Name of the package
    version='0.12.0',             # Version of the package
    packages=find_packages(),    # This automatically includes all sub-packages
    include_package_data=True,   # Include additional files specified in MANIFEST.in
    install_requires=[           # List of dependencies (if any)
        # 'some_package',
    ],
    author='Your Name',          # Your name
    author_email='your.email@example.com',  # Your email
    description='A Python package to manage error codes for multiple microservices',  # Short description
    long_description=open('README.md').read(),  # Detailed description (from README file)
    long_description_content_type='text/markdown',  # Format of the long description
    url='https://github.com/yourusername/central-error-codes',  # URL to the project
    classifiers=[  # Classifiers help users find your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
