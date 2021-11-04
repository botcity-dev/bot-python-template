import re
import sys

bot_id = '{{ cookiecutter.bot_id }}'

pattern = re.compile("^[a-z|A-Z]+[a-z|A-Z|_]*[a-z|A-Z]$")

if not pattern.match(bot_id):
    print('ERROR: bot_id can only contain letters [a-z or A-Z], underscore (_) and must end with a letter [a-z or A-Z].')

    # exits with status 1 to indicate failure
    sys.exit(1)