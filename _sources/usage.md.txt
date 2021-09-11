# Usage

To build this documentation locally :

1. Install Furo and other necessary packages for Sphinx in documentation's build environment.

   ```text
   pip install furo
   pip install -r requirements.txt
   conda install -c conda-forge pandoc
   conda install -c conda-forge ipython
   conda install -c conda-forge ipykernel
   conda install ipython notebook
   ```

2. Update the `html_theme` in `conf.py`.

   ```py
   html_theme = "furo"
   ```


Caution:
- DO NOT mix rst and md files together(except `license.rst`), because it might cause the table of contents miss some information. 