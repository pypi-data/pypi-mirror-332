from setuptools import setup, find_packages

setup(
    name='wsa-toetsing-tool',
    version='4.0.0',
    author='Emiel Verstegen',
    author_email='emiel.verstegen@rhdhv.com',
    description='Postprocessing tool voor WSA toetsing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://hhdelfland.visualstudio.com/Waterhuishouding/_git/WSA_toetsing_tool',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='GPL-3.0',
)