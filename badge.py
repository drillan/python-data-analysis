from pathlib import Path

import nbformat
from git import Repo


def get_repository_name(dir_path="."):
    repo = Repo(dir_path)
    origin_url = repo.remotes.origin.url
    return origin_url.split(":")[1].replace(".git", "")


def gen_badge_text(repository_name, file_path):
    return f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/{repository_name}/blob/main/{file_path})"


def add_badge(repository_name, file_path):
    nb = nbformat.read(file_path, as_version=4)
    first = nb["cells"][0]
    first_cell_type = first["cell_type"]
    first_source = first["source"]
    source = gen_badge_text(repository_name, file_path)
    new_cell = nbformat.v4.new_markdown_cell(source=source)
    if first_cell_type == "markdown" and first_source.startswith("[![Open In Colab]"):
        nb["cells"][0] = new_cell
    else:
        nb["cells"].insert(0, new_cell)
    new_nb = nbformat.v4.new_notebook()
    new_nb["cells"] = nb["cells"]
    nbformat.write(new_nb, file_path, version=4)


base_dir = "docs"
repository_name = get_repository_name()

p = Path(base_dir)
for file_path in p.glob("**/*.ipynb"):
    if ".ipynb_checkpoints" not in str(file_path):
        print(file_path)
        add_badge(repository_name, file_path)
