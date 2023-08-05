"""
Main module to handle master activity.
MainModule will start "main_thread_loop" and exits. However, "main_thread_loop" runs continuously until user prefer to stop.

"""

from Variables.GlobalVariables import *
from Sub_Task.sub_monitorRestartRouter import *
from threading import Thread
import threading
from Lib_Resource.LibLog import Log


class StartStopTask:
    """
    Class to start and stop a sub task through "main_thread_loop".
    """

    @classmethod
    def nothing_to_start(self):
        pass

    # @classmethod
    # def nothing_to_stop(self):
    #     pass

    @classmethod
    def start_task(self, task_name=nothing_to_start):
        # Starting Sub-thread to run Ping Test
        Thread(target=task_name, args=(), daemon=True).start()
        # ping_thread.start()


def main_thread_loop():
    """
    Main thread to start  the process and coordinate between sub-threads.
    """
    Log.set_logging(log_directory, log_file_name, 'Info')
    Log.log_info("Logging started")

    while True:
        try:
            active_threads_list = threading.enumerate()
            print(time.strftime("\n%H:%M:%S", time.localtime()) + ": Main Thread Loop")
            # Log.log_info("Active Threads: {0}".format(str(active_threads_list)))
            for clas, fun in [list for list in monitor_threads]:
                matches = [match for match in active_threads_list if fun in str(match)]
                if len(matches) <= 0:
                    # print("Starting ", fun)
                    StartStopTask.start_task(getattr(eval(clas), fun))
                # else:
                #     print(fun, " is running.")
                #     pass

            #Start anothr loop to check if any unneccessary threads are running and stop them using below code
                #eval(clas).fun_stop()

        except Exception as e:
            print(f"Exception : ", e)

        # global task_to_start
        # StartStopTask.start_task(task_to_start)
        # task_to_start = StartStopTask.nothing_to_start

        time.sleep(mainThreadWaitTime)

        global stop_main_thread
        if stop_main_thread or find_credential("STOP_ALL_TASK"):
            Log.log_info("Main Thread Stopped")
            print("\n************Main Thread Stopped************")
            break


if __name__ == "__main__":
    stop_main_thread = False
    mainThread = Thread(target=main_thread_loop)
    mainThread.start()
    # time.sleep(5)
    # stop_main_thread = True
    # mainThread.join()

    print("\n************END Of Main Module************")
