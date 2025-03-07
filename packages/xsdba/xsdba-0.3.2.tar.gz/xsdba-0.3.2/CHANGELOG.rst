=========
Changelog
=========

..
    `Unreleased <https://github.com/Ouranosinc/xsdba>`_ (latest)
    ------------------------------------------------------------

    Contributors:

    Changes
    ^^^^^^^
    * No change.

    Fixes
    ^^^^^
    * No change.

.. _changes_0.3.2:

`v0.3.2 <https://github.com/Ouranosinc/xsdba/tree/0.3.2>`_ (2025-03-06)
-----------------------------------------------------------------------

Contributors: Trevor James Smith (:user:`Zeitsperre`).

Fixes
^^^^^
* Packaging and security adjustments. (:pull:`106`):
    * Added `deptry`, `codespell`, `vulture`, and `yamllint` to the dev dependencies.
    * Added a few transitive dependencies (`packaging`, `pandas`) to the core dependencies.
    * Added `fastnanquantile` to the `dev` dependencies (to be placed in an `extras` recipe for `xsdba` v0.4.0+).
    * Configured `deptry` to handle optional imports.
    * A new Makefile command `lint/security` has been added (called when running `$ make lint`).
    * Updated `tox.ini` with new linting dependencies.

.. _changes_0.3.1:

`v0.3.1 <https://github.com/Ouranosinc/xsdba/tree/0.3.1>`_ (2025-03-04)
-----------------------------------------------------------------------

Contributors: Trevor James Smith (:user:`Zeitsperre`).

Changes
^^^^^^^
* Added `POT` to the development dependencies. (:pull:`96`).

Fixes
^^^^^
* Adjusted the documentation dependencies and the `sphinx` configuration to fix the ReadTheDocs build. (:pull:`96`).

.. _changes_0.3.0:

`v0.3.0 <https://github.com/Ouranosinc/xsdba/tree/0.3.0>`_ (2025-03-04)
-----------------------------------------------------------------------

Contributors: Pascal Bourgault (:user:`aulemahal`), Éric Dupuis (:user:`coxipi`), Trevor James Smith (:user:`Zeitsperre`).

Announcements
^^^^^^^^^^^^^
* `xsdba` is now available as a package on the Anaconda `conda-forge` channel. (:pull:`82`).

Changes
^^^^^^^
* Remove the units registry declaration and instead use whatever is set as pint's application registry.
  Code still assumes it is a registry based upon the one in cf-xarray (which exports the `cf` formatter). (:issue:`44`, :pull:`57`).
* Updated the cookiecutter template to use the latest version of `cookiecutter-pypackage`. (:pull:`71`):
    * Python and GitHub Actions versions have been updated.
    * Now using advanced CodeQL configuration.
    * New pre-commit hooks for `vulture` (find dead code), `codespell` (grammatical errors), `zizmor` (workflow security), and `gitleaks` (token commit prevention).
    * Corrected some minor spelling and security issues.
* Added `upstream` testing to the CI pipeline for both daily and push events. (:pull:`61`).
* Import last changes in xclim before the embargo (:pull:`80`).
* `xsdba` has begun the process of adoption of the OpenSSF Best Practices checklist. (:pull:`82`).
* `xclim` migration guide added. (:issue:`62`, :pull:`86`).
* Add a missing `dOTC` example to documentation. (:pull:`86`).
* Add a new grouping method specific for `MBCn` which called by passing `group=Grouper("5D", window=n)` where `n` is an odd positive integer. (:pull:`79`).

Fixes
^^^^^
* Gave credits to the package to all previous contributors of ``xclim.sdba``. (:issue:`58`, :pull:`59`).
* Pin `sphinx-codeautolink` to fix ReadTheDocs and correct some docs errors. (:pull:`40`).
* Removed reliance on the `netcdf4` package for testing purposes. The `h5netcdf` engine is now used for file IO operations. (:pull:`71`).
* Changes to reflect the change of library name `xsdba`. (:pull:`72`).
* Revert changes to allow using `group="time.dayofyear"` and `interp="linear"` in adjustment methods. (:pull:`86`).

.. _changes_0.2.0:

`v0.2.0 <https://github.com/Ouranosinc/xsdba/tree/0.2.0>`_ (2025-01-09)
-----------------------------------------------------------------------

Contributors: Éric Dupuis (:user:`coxipi`), Trevor James Smith (:user:`Zeitsperre`).

Changes
^^^^^^^
* Split `sdba` from `xclim` into its own standalone package. Where needed, some common functionalities were duplicated: (:pull:`8`)
    * ``xsdba.units`` is an adaptation of the ``xclim.core.units`` modules.
    * Many functions and definitions found in ``xclim.core.calendar`` have been adapted to ``xsdba.base``.
* Dependencies have been updated to reflect the new package structure. (:pull:`45`).
* Updated documentation configuration: (:pull:`46`)
    * Significant improvements to the documentation content and layout.
    * Now using the `furo` theme for `sphinx`.
    * Notebooks are now linted and formatted with `nbstripout` and `nbqa-black`.
    * CSS configurations have been added for better rendering of the documentation and logos.
* Added the `vulture` linter (for identifying dead code) to the pre-commit configuration. (:pull:`46`).

.. _changes_0.1.0:

`v0.1.0 <https://github.com/Ouranosinc/xsdba/tree/0.1.0>`_
----------------------------------------------------------

Contributors: Trevor James Smith (:user:`Zeitsperre`)

Changes
^^^^^^^
* First release on PyPI.
