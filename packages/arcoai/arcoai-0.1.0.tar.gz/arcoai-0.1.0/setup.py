from setuptools import setup, find_packages

setup(
    name="arcoai",
    version="0.1.0",
    author="Arcoson",
    author_email="hylendust@gmail.com",
    description="A library for easy creation of ANN and CNN models with integrated visualization tools",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Arcoson/arcoai",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.6',
    install_requires=[
        'tensorflow>=2.0',
        'torch>=1.7',
        'numpy>=1.18',
        'matplotlib>=3.0',
        'scipy>=1.5',
        'pandas>=1.0',
        'scikit-learn>=0.24',
        'Pillow>=8.0',
        'pytest>=6.0',
    ],
    include_package_data=True,
    package_data={
        '': ['*.md', '*.txt', '*.csv', '*.json'],
    },
    entry_points={
        'console_scripts': [
            'arcoai=arcoai.cli:main',
        ],
    },
)
