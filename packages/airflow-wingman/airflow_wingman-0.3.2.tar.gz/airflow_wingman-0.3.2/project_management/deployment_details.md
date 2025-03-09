`env` is the python. Creted by `uv`.
direct `pip` won't work but `uv pip` does.

`astro` folder is in gitignore. So only shell commands work.
plugin is built and deployed in astro project in astro folder:
```bash
uv build && 
cp -f dist/*.whl astro/wheels/ &&
cd astro && astro dev restart && cd ..
```
See we cd into astro folder so it is a differetn folder as compared to source code.

once the project starts, we can see the docker images with `docker ps` and exec and test things.
