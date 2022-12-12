<p align="center">
  <h1 align="center">Template Bot Project - Python</h1>
  <p align="center">
    <br>
    <br>
    <a href="https://github.com/botcity-dev/bot-python-template/issues/new?template=bug-report.md">Report bug</a>
    ·
    <a href="https://github.com/botcity-dev/bot-python-template/issues/new?template=feature-request.md&labels=request">Request feature</a>
    ·
    <a href="https://github.com/botcity-dev/bot-python-template/blob/main/.github/CONTRIBUTING.md">How to Contribute</a>
    ·
    <a href="https://github.com/botcity-dev/bot-python-template/blob/main/.github/SUPPORT.md">Support</a>
  </p>
</p>
<br>

# Prerequisites
* Python 3.7+
* cookiecutter

# Getting Started

This repository contains a cookiecutter template for generating a Bot using
BotCity's Python Framework.

To create a templated project all you need to do is:
```
cookiecutter https://github.com/botcity-dev/bot-python-template
```

# Building the Documentation Locally
In order to build the documentation you will need to install some dependencies
that are not part of the runtime dependencies.

Assuming that you have cloned this repository do:

```bash
pip install -r docs-requirements.txt

mkdocs build
```

This will generate the HTML documentation in the `<>/site`
folder. Look for the `index.html` file and open it with your browser.
