"""
    This Module is to store the IP address of the machine to a file periodically.
"""

import subprocess
import time
import os


def get_hostname():
    """
    To get hostname
    """
    p = subprocess.Popen('hostname'.split(),
                         shell=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    hostname, stderr = p.communicate()
    hostname = str(hostname.decode('ascii')).strip()

    return hostname


def store_ipconfig():
    """
    This function is to store the IP address of the machine to a file periodically.
    """

    if os.path.exists(r'..\CloudProjectWrokSpace\IPAddress'):
        ip_log_path_with_file = r'"..\CloudProjectWrokSpace\IPAddress\{0}_IP.txt"'.format(
            get_hostname())
    elif os.path.exists(r'..\Pycharm'):
        ip_log_path_with_file = r'"..\Pycharm\{0}_IP.txt"'.format(get_hostname())
    else:
        ip_log_path_with_file = "no_path"

    ipconfig_cmd = r"ipconfig > {0}".format(ip_log_path_with_file)

    p = subprocess.Popen(ipconfig_cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


print("IP Configure Monitor..")

while True:
    store_ipconfig()
    time.sleep(300)
