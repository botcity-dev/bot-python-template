#!/bin/bash

zip -r "{{ cookiecutter.bot_id|replace(' ', '_') }}.zip" "{{ cookiecutter.bot_id|replace(' ', '_') }}"/*