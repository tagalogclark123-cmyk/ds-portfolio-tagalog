"""Make images written as raw HTML show up in the built site.

Notebooks/markdown often embed pictures like  <img src="diagram.jpg">  or
<img src="figures/diagram.png">.  Jupyter and VS Code find those files next to
the notebook, but Sphinx does not treat raw HTML as an image reference, so
`jupyter-book build` never copies them and the image is broken on the website.

This helper fixes that automatically after every HTML build:
  1. it scans every page listed in _toc.yml for  <img src="...">  with a
     relative path and copies each existing file into the site, keeping its path;
  2. it also copies the whole `figures/` folder (add names to FOLDERS below).
Nothing to configure: keep the image next to the notebook (or in figures/).
"""
import re
import shutil
from pathlib import Path

FOLDERS = ["figures"]
SRC_RE = re.compile(r"""<img[^>]*?\bsrc=\\?["']([^"'\\>]+)""", re.I)


def _copy_file(src_root: Path, out_root: Path, rel: str):
    rel = rel.split("#")[0].split("?")[0]
    if not rel or re.match(r"^(?:[a-z][a-z0-9+.-]*:|//|/)", rel, re.I):
        return                                   # http(s):, data:, absolute paths
    src = (src_root / rel).resolve()
    try:
        src.relative_to(src_root.resolve())      # stay inside the project
    except ValueError:
        return
    if src.is_file():
        dest = out_root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)


def _copy(app, exception):
    if exception is not None or app.builder.format != "html":
        return
    src_root, out_root = Path(app.srcdir), Path(app.outdir)
    for docname in app.env.found_docs:
        try:
            path = Path(app.env.doc2path(docname))
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for rel in SRC_RE.findall(text):
            _copy_file(src_root, out_root, rel)
    for name in FOLDERS:
        folder = src_root / name
        if folder.is_dir():
            shutil.copytree(folder, out_root / name, dirs_exist_ok=True)


def setup(app):
    app.connect("build-finished", _copy)
    return {"version": "1.1", "parallel_read_safe": True, "parallel_write_safe": True}
