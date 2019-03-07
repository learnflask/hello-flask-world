import setuptools
from os.path import splitext,basename
from glob import glob

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hello-flask-world",
    version="0.0.1",
    author="Terrel Shumway",
    author_email="ghdev@learnflask.dev",
    description="Boilerplate project for a simple Flask app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/learnflask/hello-flask-world",
    packages=setuptools.find_packages("src"),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts':[
            "helloflask=helloflask.cli:main"
        ]
    }
)