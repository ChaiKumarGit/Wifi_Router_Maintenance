"""
Module containing common function used across the project.

"""

import subprocess
import time


def run_ping_test(host="8.8.8.8"):
    """
    Run ping test
    """
    ping_command = "ping {0} -n 1".format(host)
    p = subprocess.Popen(ping_command.split(),
                         shell=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    output, error = p.communicate()

    return output, error

