from setuptools import setup, find_packages

setup(
    name='com_micheg.md2site',
    version='0.1',
    packages=find_packages(),
    namespace_packages=['com_micheg'],
    install_requires=[
        'setuptools',
        'Jinja2',
        'markdown2',
        'MarkupSafe',
        'docopt',
        'zc.lockfile'
    ],
    entry_points={
        'console_scripts': [
            'md2site=com_micheg.md2site.cmd:main',
            ],
    }
)
