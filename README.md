# Data Science Portfolio

Lab reports on neural networks and deep learning with PyTorch, published as a
[Jupyter Book](https://jupyterbook.org).

**Read it online:** https://tagalogclark123-cmyk.github.io/ds-portfolio-tagalog/

## Contents

| Lab | Topic |
| --- | --- |
| 2 | Forward pass and error computation |
| 3 | Forward and backward propagation |
| 4 | PyTorch linear regression |
| 5 | PyTorch tensor fundamentals |

## Build locally

```bash
pip install -r requirements.txt
jupyter-book build .          # output in _build/html
```

## Deploy to GitHub Pages

```bash
ghp-import -n -p -f _build/html
```

## Project layout

- `_config.yml`: book settings (title, theme options, buttons)
- `_toc.yml`: sidebar structure and page titles
- `_static/`: custom CSS, logo, favicon, link-preview image
- `intro.md`: home page
- `Lab_Task_*.ipynb`: the lab notebooks (outputs are shown as saved)
