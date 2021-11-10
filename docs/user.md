Tutorials
---------

The plugin incorporates four tutorials to help the user understand how
it works and guide him step by step throughout all the functions via
specific test cases. They are accessible via `DS9` menus.

` Analysis -> Quick look plugin -> Give it a go`.

The help is also available directly from the

` Analysis -> Quick look plugin -> Help`

<!-- Some training videos are available on the
[website](https://people.lam.fr/picouet.vincent/pyds9plugin/) and on
[youtube](https://www.youtube.com/watch?v=XcDm2JQDMLY). -->

<!-- Performance and maintainability
-------------------------------

Each function has been profiled and optimized in order to increase its
speed performance. For instance, all the dependencies of each function
are imported within the function so that running DS9Utils only loads
needed modules. The code follows PEP 8 guide style. -->



<!--
### Known issues

No Next window in tutorials:

:   This means that there was an error at the install of PyQt5. On
    Linux, refer to that
    [page](https://www.programmersought.com/article/30566120835/) to
    solve the issue. On mac you can uninstall pyds9plugin, re-install
    the required packages using
    [mamba](https://GitHub.com/mamba-org/mamba):\
    ` mamba install NumPy matplotlib astropy tqdm pyvista  PyQt `\
    and then re-install pyds9plugin:\
    ` pip install -v pyds9plugin `\ -->
