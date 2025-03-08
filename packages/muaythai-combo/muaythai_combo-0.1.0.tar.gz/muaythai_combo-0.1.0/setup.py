from setuptools import setup, find_packages

setup(
    name="muaythai_combo",
    version="0.1.0",
    description="Muay Thai Combo Generator with Tkinter",
    author="Sam Porter",
    author_email="sam.porter.18@ucl.ac.uk",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'muaythai_combo=muaythai_combo.app:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)