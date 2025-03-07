from setuptools import setup, find_packages

setup(
    name='dsgbench_ability_calc',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    package_data={'dsgbench_ability_calc': ['weights/game_weights.json','weights/metrics_range.json',
                                            'weights/metrics_weights.json','weights/model_abilities.json',
                                            'weights/scene_ability.json','pyarmor_runtime_000000/pyarmor_runtime.pyd']},
    include_package_data=True,
    author='WenjieTang',
    author_email='wenjietang2022@163.com',
    description='model ability calculation',
)