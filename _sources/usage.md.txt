# Usage

Furo is distributed on [PyPI]. To use the theme in your Sphinx project:

1. Install Furo in documentation's build environment.

   ```text
   pip install furo
   ```

2. Update the `html_theme` in `conf.py`.

   ```py
   html_theme = "furo"
   ```


Caution:
- DO NOT mix rst and md files together(except `license.rst`), because it might cause the table of contents miss some information. 