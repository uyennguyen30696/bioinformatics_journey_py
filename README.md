This is a documentation of my beginning practice in learning Python for bioinformatics. Each file contains solutions for bioinformatics problems on [Rosalind](http://rosalind.info)

I run my code on [IDLE](https://docs.python.org/2/library/idle.html), or [VS CODE](https://code.visualstudio.com/) with Code Runner Extension (compatible with multiple programming languages).

Smaller steps count toward bigger goal!

## Set up Python virtual environment & install libraries for macOS

### Python virtual environment

Python virtual environment is a self-contained directory that maintains its own version of Python and libray dependencies, which does not interfere with other projects.

In the root directory, run `python -m venv venv`. If a newer Python version needed, for example Python 3, run `python3 -m venv venv`

To activate the virtual environment, run `venv/bin/activate`. At the command-line prompt, `(venv)` should appear.

To deactivate, run `deactivate`

### Install biopython

`pip install biopython`
