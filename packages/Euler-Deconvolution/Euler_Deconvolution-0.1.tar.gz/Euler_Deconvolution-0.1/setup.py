from setuptools import setup, find_packages

setup(
    name='Euler_Deconvolution',  # Unique package name
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy', 'scipy'],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python library for Euler Deconvolution in Geophysics',
    url='https://github.com/yourusername/Euler_Deconvolution',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
