from setuptools import setup, find_packages

setup(
    name="central-error-codes",
    version="0.0.2",
    packages=find_packages(where='py_modules/src'),  # This will search for packages inside 'py_modules/src'
    package_dir={
        '': 'py_modules/src',  # Tell setuptools to look for packages under 'py_modules/src'
    },
    package_data={
        'central_error_codes': ['../../errors/*', '../../errors/**/*'],  # Include files from 'errors/'
    },
    include_package_data=True,
    install_requires=[
        # List your dependencies here
    ],
)
