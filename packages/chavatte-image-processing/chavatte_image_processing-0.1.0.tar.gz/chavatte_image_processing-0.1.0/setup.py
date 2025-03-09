from setuptools import setup, find_packages

setup(
    name='chavatte_image_processing',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='João Carlos Chavatte',
    author_email='chavatte@duck.com',
    description='Biblioteca para processamento de imagens',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chavatte/LAB-SUZANO-PYTHON-DEVELOPER/blob/main/projects/LAB-04/README.md',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Image Processing',
    ],
)