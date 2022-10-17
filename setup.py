from setuptools import find_packages, setup

setup(
    name='cluscompy',
    packages=find_packages(include=['cluspy']),
    version='0.1.0',
    description='Library for simulating cluster generation and computation for Measurement-Based Quantum Computation (MBQC).',
    author='Emil Ostergaard',
    license='MIT',
)
