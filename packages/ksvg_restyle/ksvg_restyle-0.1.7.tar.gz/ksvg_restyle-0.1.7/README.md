# KSVGRestyle

KSVGRestyle is a command-line interface (CLI) tool designed to apply a color scheme to a specified SVG file of a Plasma desktop widget. This tool is ported from the [apply-stylesheet.sh](https://invent.kde.org/plasma/libplasma/-/blob/master/src/tools/apply-stylesheet.sh) script by the KDE Development Team.

## Features

- **Apply Color Schemes:** Modify the color palette of SVG files to match your desired Plasma desktop theme.
- **CLI Interface:** Easily integrate into scripts or use directly from the terminal.


<!-- Pytest Coverage Comment:Begin -->
<!-- Pytest Coverage Comment:End -->

## Installation

KSVGRestyle can be installed through several means. The most simple one (and recommended) would be installing it via [pipx](https://github.com/pypa/pipx)
```bash
# to install it from the PyPI registry
pipx install ksvg_restyle 
# or
# to install directly from git
pipx install git+https://github.com/squalorware/KSVGRestyle.git 
```
It will install the application to an isolated Python environment, and expose the entrypoint locally on one of the possible directories that are included to local `PATH` - usually `$HOME/.local/bin` or `$HOME/.bin` etc. Nevertheless, `pipx` provides an opportunity to install packages system-wide as well.

Users that do not utilize `pipx`, can install it like any other regular Python package using pip -
```bash
pip install --user ksvg_restyle
```

And of course, it is possible to build the installable Python package directly from the source code - in this case a user must ensure they have [Poetry](https://python-poetry.org/) installed (version 2 and higher) and run Python 3.12 or higher. To build the package, one should

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/squalorware/KSVGRestyle.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd KSVGRestyle
   ```

3. **Install Runtime Dependencies:**

   (Don't forget about [Poetry](https://python-poetry.org/)!)

   ```bash
   poetry install --only main 
   ```
4. **And finally**:

   ```bash
   poetry build 
   ```
If the build is successful, a directory named `dist` will appear in the root of the source code directory, which will contain Python package in both formats - wheel and sdist (a tar.gz archive)

## Usage
```bash
 $ ksvgrestyle [OPTIONS] SVG

Options:
  -c, --color-scheme PATH  Path to the Plasma Color Theme file  [required]
  -o, --output PATH        Output destination path (recolored SVG image)
  -r, --replace            Replace existing SVG. Effective only when no output
                           path provided.
  --help                   Show this message and exit.
```
Since it is a Python package, it can also be called as a module 
```bash
$ python -m ksvg_restyle [OPTIONS] SVG
```

## TODOs

- [ ] Add a possibility to pass a path to a directory containing the svg images to restyle them in-bulk
- [ ] Add an optional parameter for the user to decide whether to compress a resulting SVG image or not (right now the compression applies only if the input file was compressed as well).

## Contributing

Contributions are welcome! If you'd like to contribute to KSVGRestyle, please follow these steps:

1. **Fork the Repository:** Click on the "Fork" button at the top right corner of this page.
2. **Create a New Branch:** In your forked repository, create a new branch for your feature or bugfix.
3. **Make Your Changes:** Implement your feature or fix the bug.
4. **Submit a Pull Request:** Once your changes are ready, submit a pull request to the main repository.

## License

This project is licensed under the LGPL-2.1-or-later License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

Special thanks to the KDE Development Team for the original [apply-stylesheet.sh](https://invent.kde.org/plasma/libplasma/-/blob/master/src/tools/apply-stylesheet.sh) script, which served as the foundation for this tool.
