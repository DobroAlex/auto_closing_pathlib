import setuptools

with open('README.md', 'r') as readme:
    long_description: str = readme.read()

setuptools.setup(
    name='auto_closing_path',
    version='0.0.1',
    author='Alex Konsmanov',
    author_email='alexkoshernosiegov@gmail.com',
    description='The alternative implementation of pathlib.Path\'s context manager',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DobroAlex/auto_closing_pathlib',
    packages=setuptools.find_packages(),
    classifires=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Natural Language :: Russian',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Programming Language :: Python :: 3 :: Only',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 ],
    python_requires='>=3.7',
)
