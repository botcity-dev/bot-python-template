Get-ChildItem -Path . -Recurse -Exclude "{{ cookiecutter.bot_id|replace(' ', '_') }}.zip" |
  Compress-Archive -DestinationPath "{{ cookiecutter.bot_id|replace(' ', '_') }}.zip" -Force