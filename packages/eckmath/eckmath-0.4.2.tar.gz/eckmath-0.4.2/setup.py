from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='eckmath',
    version='0.4.2',
    license='MIT License',
    author='Guilherme Eckhardt',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='eckhardt.gui@gmail.com',
    keywords='multmat,seglen,segintersect,point2D, point3D',
    description=u'Um repositorio para fins academicos',
    packages=['eckmath'],)