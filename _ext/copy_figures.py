"""Copy ./figures into the built HTML site.

Some notebooks embed images with raw HTML, e.g. <img src="figures/diagram.png">.
Sphinx does not treat raw HTML as an image reference, so those files would be
missing from the published book. This tiny extension copies the whole `figures/`
folder next to the pages so those <img> tags keep working. Nothing to configure:
just keep your images in `figures/` (as the notebooks already expect).
"""
import shutil
from pathlib import Path

FOLDERS = ["figures"]          # add more folder names here if you need them


def _copy(app, exception):
    if exception is not None or app.builder.format != "html":
        return
    for name in FOLDERS:
        src = Path(app.srcdir) / name
        if src.is_dir():
            shutil.copytree(src, Path(app.outdir) / name, dirs_exist_ok=True)


def setup(app):
    app.connect("build-finished", _copy)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
