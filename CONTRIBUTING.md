#  Introduction

Thank you for considering contribution to Navitia Client !

You will find in the following few ground rules to help to provide a good tool to the open-source community.

## Ground rules

By contributing to this project:

* Be respectful with others and remember that this project is maintained by volunteers which are doing so on their free time.
* If you want to make a change, please create an issue first so we might be able to track your changes.
* Ensure that your code is following the [Style Guide for Python Code](https://peps.python.org/pep-0008/).
* Make sure that any changes you provide is covered tested properly.
* Create clear commit messages and keep the history of your branch as clean as possible.

##  How to contribute

To contribute to this repository, you will need to install the dependancies located in [dev-requirements.txt](dev-requirements.txt).

```bash
pip install dev-requirements.txt
```

We are relying on a few tools (mypy, ruff) to ensure code quality, which are run at commit time. Make sure that [pre-commit](https://pre-commit.com/) has been installed properly

```bash
pre-commit init
```

Ensure that these tools ran successfully on your machine before creating a pull-request. In any case, they have been added to the CI, so your pull request will not be mergeable until all error are fixed.

##  Testing

Ensure that any changes you provide is covered by tests. We are using [pytest](https://docs.pytest.org/en/8.0.x/).

After installation of the dev dependancies, you can run all tests using

```bash
python -m pytest tests/
```

##   Issues and feature requests

Feel free to open a Github issue when reporting an issue or asking for a feature request.
