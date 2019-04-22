from setuptools import setup

setup(
    name="jut",
    version="0.4",
    py_modules=['jut'],
    install_requires = [
        'Click',
        'Colorama'
    ],
    entry_points = '''
    [console_scripts]
    jut=jut:cli
    ''',
)