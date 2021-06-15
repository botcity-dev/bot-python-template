# Building the Package

Since the bot is a python package, it is recommended to generate a source distribution.

For that we provide build scripts (`build.bat` and `build.bat`) which just do the following:

```shell
python setup.py sdist
```

This process will generate a `dist` folder with the compressed project source code.


# Installing

After that is done you can install the package generated with:

```shell
pip install dist/botPython-1.0.tar.gz   # or .zip if running on Windows
```

Or simply using the following command:

```shell
pip install .
```

!!! tip
    If you are using the BotCity Maestro server, the BotRunner will take care of installing
    your package into a virtual environment for execution in your automation machine.
    All you need to do is use the BotCLI command line interface to deploy and release your
    package.

    ```shell
    # For deploy:
    botCLI bot deploy -botId "botPython" -version 1.0 -file "./dist/botPython-1.0.tar.gz" -python

    # For update of an existing version file:
    botCLI bot update -botId "botPython" -version 1.0 -file "./dist/botPython-1.0.tar.gz"

    # For release:
    botCLI bot release -botId "botPython" -version 1.0
    ```
