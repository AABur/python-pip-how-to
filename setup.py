from setuptools import find_packages, setup

setup(
    long_description='just learning pip packaging',
    name='pip_how_to',
    version='0.0.1',
    description='',
    python_requires='==3.*,>=3.8.0',
    url='https://github.com/AABur/python-pip-how-to',
    author='AABur',
    author_email='aabur@mail.ru',
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Topic :: Education',
    ],
    entry_points={
        'console_scripts': [
            'brain-games = brain_games.scripts.brain_games:main',
            'brain-even = brain_games.scripts.brain_even:main',
            'brain-calc = brain_games.scripts.brain_calc:main',
            'brain-gcd = brain_games.scripts.brain_gcd:main',
            'brain-progression = brain_games.scripts.brain_progression:main',
            'brain-prime = brain_games.scripts.brain_prime:main',
        ]
    },
    packages=find_packages(),
    install_requires=['prompt==0.*,>=0.4.1', 'pyprimer==0.*,>=0.1.0'],
    extras_require={'dev': ['flake8==3.*,>=3.8.3', 'isort==5.*,>=5.5.0']},
)
