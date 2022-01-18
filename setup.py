import setuptools

setuptools.setup(
    name='lxslt',
    version="0.1.0",
    author="Oleg Parashchenko",
    author_email="olpa@uucode.com",
    description="XSLT-like transformations over python lists",
    url="https://github.com/olpa/python-lxslt",
    classifiers=[
        "Topic :: Text Processing :: Markup :: XML",
    ],
    package_dir={'lxslt': './src/lxslt'},
    packages=['lxslt'],
    python_requires=">=3.6",
)
