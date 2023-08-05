"""
Monitor in router and restart if no internet access deducted.
"""
import time

from Lib_Resource.LibCommFun import run_ping_test
from main.ISPMain import *
from Variables.GlobalVariables import *
from multiprocessing.pool import ThreadPool
from Lib_Resource.LibLog import Log
from Lib_Resource.GetCredential import *


class MonitorRouter:
    """
    Class to monitor Router and perform certain tasks.
    """

    stop_thread = False

    @classmethod
    def fun_stop_thread(cls):
        """
        Function to break the loop and end "fun_monitor_restart_router(cls):"
        """
        Log.log_info("Stopping Router Monitoring module")
        print("In fun_stop_thread for MonitorRouter class")
        MonitorRouter.stop_thread = True

    @classmethod
    def fun_monitor_restart_router(cls):
        """
        Function to monitor router and restart if required.
        """
        Log.log_info("Router Monitoring Started")
        print("In fun_monitor_restart_router")

        periodic_log_timer = time.time()
        ping_missed_count = 0
        thread_start_time = time.time()

        while True:
            # Verify data connection
            time.sleep(pingInterval)
            ping_test_pool = ThreadPool(processes=1)
            async_ping_result = ping_test_pool.apply_async(run_ping_test, ('google.com', ))
            return_output, return_err = async_ping_result.get()

            #Periodic logging of data availability
            if (time.time() - periodic_log_timer) >= routerMonitorPeriodicLogTime:
                Log.log_info("Periodic: " + str(return_output))
                periodic_log_timer = time.time()

            #Check if ping is missed
            if str(return_output).find("(100% loss)") != -1:
                Log.log_error(return_output)
                ping_missed_count += 1
            else:
                ping_missed_count = 0

            #Restart if pings are continuously missed
            if ping_missed_count >= numOfPingsMissedBeforeRestart:
                Log.log_error("Restarting Router")
                reboot_router()
                time.sleep(600)
                ping_missed_count = 0

            if MonitorRouter.stop_thread or find_credential('STOP_ALL_TASK'):
                Log.log_info("Monitor Router Stopped")
                break

            # Verify Thread active time and kill if more than "anyThreadLife"
            if (time.time() - thread_start_time) >= anyThreadLife:
                Log.log_error("Restarting Router")#
                reboot_router()#
                time.sleep(600)#
                break

