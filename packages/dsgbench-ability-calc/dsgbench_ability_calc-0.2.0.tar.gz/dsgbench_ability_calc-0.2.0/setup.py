from setuptools import setup, find_packages

setup(
    name='dsgbench_ability_calc',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    package_data={'dsgbench_ability_calc': ['pyarmor_runtime_000000/pyarmor_runtime.pyd']},
    include_package_data=True,
    author='WenjieTang',
    author_email='wenjietang2022@163.com',
    description='model ability calculation',
)