#!/bin/bash

zip -r "{{ cookiecutter.bot_id|replace(' ', '_') }}.zip" * -x "{{ cookiecutter.bot_id|replace(' ', '_') }}.zip"