import os
time = input("Enter the interval between easch reboot (in minutes): ")

def reboot():
    os.system(f"shutdown -r {time}")

reboot()