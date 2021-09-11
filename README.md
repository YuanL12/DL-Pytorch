# DL-Pytorch

<!-- start DL-Pytorch -->

This is a repository used to store personal learning process of Pytorch, published at https://yuanl12.github.io/DL-Pytorch/. I mainly follow the contents in https://d2l.ai/.

<!-- end DL-Pytorch -->

## Installation
```
conda create -n d2l-zh python=3.8
conda activate d2l-zh
pip install jupyter d2l torch torchvision
conda install nb_conda_kernels ipykernel // for selecting different packages easily in the kernel list
```

## Make documentation and Github pages
In order to make pages, I highly recommend using a separate conda environment,
```terminal
cd docs
conda create -n docu python=3
conda activate docu
pip install -r requriements.txt
make html
```
, then you can see it in `docs/build/html/index.html`

In order to publish on Github (make sure you are still in `docs` folder), 
```terminal
make gh-pages
```

## Sphinx Resoruces
- themes
https://sphinx-themes.org/sample-sites/sphinx-book-theme/#navigation

- sphinx command
**On parent directory of docs, **
```
sphinx-quickstart docs
sphinx-build -b html docs/source/ docs/build/html

pip install furo
```

- Online blogs
https://jamwheeler.com/college-productivity/how-to-write-beautiful-code-documentation/
https://rantzen.net/2020/02/tutorial--using-sphinx-clever-with-github-pages/