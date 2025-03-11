from setuptools import setup

setup(  name= 'transaction_analyze', 
        version='1.0.3', 
        description='Transaction Analyze.', 
        packages=['transaction_analyze'],
		author='Jordan',
		license="Python Script",
        install_requires = ["blessings ~= 1.7"],
        extras_require={
            "dev": [
                "pytest>=3.2",
            ],
        },
    )

