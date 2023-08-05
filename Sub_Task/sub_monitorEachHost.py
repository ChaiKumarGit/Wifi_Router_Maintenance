"""
Monitor each host (PC) and restart Router if any one of the host is not reachable.
"""
import time

from Lib_Resource.LibCommFun import run_ping_test
from main.ISPMain import *
from Variables.GlobalVariables import *
from multiprocessing.pool import ThreadPool
from Lib_Resource.LibLog import Log
from Lib_Resource.GetCredential import *


class MonitorHost:
    """
    Class to monitor each Host and perform certain tasks.
    """

    stop_thread = False

    @classmethod
    def fun_monitor_each_host(cls):
        """
        Function to monitor router and restart if required.
        """
        Log.log_info("Host Monitoring Started")
        print("In fun_monitor_each_host")

        periodic_log_timer = time.time()
        ping_missed_count = 0
        while True:

            Read Host monitor file and check of time

            if host time is not updated for more than 5 min:
                Initiate restart
                break
