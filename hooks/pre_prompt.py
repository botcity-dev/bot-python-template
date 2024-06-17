import sys

print("*"*80)
print("*" + "WARNING".center(78) + "*")
print("*"*80)
print("")
print("You are using an outdated version of the template which is no longer recommended.")
print("While this template works and is valid, it is strongly recommended to create a new project with the latest template version.")
print("")
print("Please refer to our documentation: https://documentation.botcity.dev/tutorials/python-automations/desktop/")
print("")

try:
    input(f"Press any key to continue or use Ctrl+C to cancel.")
except KeyboardInterrupt:
    sys.exit("Interrupted by the user")
    pass