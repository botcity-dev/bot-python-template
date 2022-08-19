powershell Compress-Archive -LiteralPath "{{ cookiecutter.bot_id|replace(' ', '_') }}" -DestinationPath "{{ cookiecutter.bot_id|replace(' ', '_') }}.zip"
