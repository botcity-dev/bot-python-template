from botcity.base.utils import find_bot_class
from . import bot

klass = find_bot_class(bot)[0]
klass.main()
