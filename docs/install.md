
Installation
------------

`pyds9plugin` is governed by the CeCILL-B license under French law and
abides by the rules of free software distribution. The package has been
released on [https://pypi.org](https://pypi.org/project/pyds9plugin/)
and is being reviewed to become an [astropy affiliated
packages](https://www.astropy.org/affiliated/). The source code is
available on GitHub:

` git clone https://github.com/vpicouet/pyds9plugin.git `

You should create an environment with python 3.8:

` conda create --name py38 python=3.8  `

and then activate it

` conda activate py38 `

People can contribute to the code via GitHub and fill issues with
Github's issue tracker. `pyds9plugin` works with `DS9` with a version
equal to or higher than 8.2. The extension can be installed via the
terminal:

` pip install -v pyds9plugin `

or

` python3 setup.py install`

The package can also be installed inside a [virtual
environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
The package will be accessible via `DS9Utils` keyword in the terminal.
To load the analysis file in `DS9` run:

` DS9Utils LoadDS9QuickLookPlugin`

!!! warning
    If the file can not be added automatically, instructions will appear to add it manually. The given path returned by the previous command will just need to be added to DS9 preference analysis section

**Prerequisites and dependence:** `pyds9plugin` runs under Python
versions $>3.5$. Note that as a minimum, any user will need to have at
least installed [pyds9](https://GitHub.com/ericmandel/pyds9),
[`NumPy`](https://NumPy.org), [`scipy`](https://www.scipy.org),
[`astropy`](https://www.astropy.org),
[`argparse`](https://docs.Python.org/3/library/argparse.html),
[`pyvista`](https://docs.pyvista.org), [`tqdm`](https://tqdm.GitHub.io),
[`datetime`](https://docs.Python.org/fr/3/library/datetime.html),
[`pandas`](https://pandas.pydata.org),
[`PyQt5`](https://pypi.org/project/PyQt5/),
[`matplotlib`](https://matplotlib.org) and
[`dataphile`](https://GitHub.com/glentner/dataphile).

For full functionality the
[astromatic](https://astromatic.net/software/) suite (`Swarp`, `Stiff` and `PSFex`) is also needed.



!!! warning
    `Pyds9` package is not available on windows.
