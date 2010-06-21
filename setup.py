from setuptools import setup, find_packages
VERSION="0.0.1"
setup(
    name="dotfilemanager",
    version=VERSION,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    license='GPL',
    test_suite="nose.collector",
    tests_require="nose",
    entry_points={
        'console_scripts': [
            'dotfilemanager = dotfilemanager.dotfilemanager:main',
            ],
        #'hestia.ui' : ['hestia.ui=hestia.ui']
        }
)
