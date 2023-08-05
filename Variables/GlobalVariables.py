"""
Globally configured Variables.
"""

from Lib_Resource.GetCredential import *

#Router Maintenance -

#Router Maintenance - Extra
pingInterval                            =   10                                              # seconds
routerMonitorPeriodicLogTime            =   300                                             # seconds
numOfPingsMissedBeforeRestart           =   9
routerPeriodicRestart                   =   900                                            # 0 for no periodic restart. Any value more than 0 in 'seconds' for periodic restart.

#Router Maintenance - LOGGING
log_directory                           =   find_credential('logDir')
log_file_name                           =   '_WIFIROUTER_LOG'

#Router Maintenance - Webpage
host                                    =   find_credential('host')
userName                                =   find_credential('user')
userPassword                            =   find_credential('password')
waitTimeToLoad                          =   15                                               # Wait time for webDrive (implicit) to wait until element found

#Router Maintenance - xPath
xpathUsername                           =   '//input[@name="ui_user"]'
xpathPassword                           =   '//input[@name="ui_pws"]'
xpathLoginBtn                           =   '//div[@id="btn_"]'
xpathRebootBtn_iframe                   =   '//iframe[@id="frm_main2"]'
xpathRebootBtn                          =   '//div[@id="btn_apply"]'

#Configuration Variables
mainThreadWaitTime                      =   300                                              # seconds
seleniumDriverPath                      =   find_credential('seleniumDriverPath')
monitor_threads                         =   [
                                                ['MonitorRouter','fun_monitor_restart_router']
                                            ]
anyThreadLife                           =   14400                                            # seconds [Used to kill the thread after this timer. So that Main thread can start a new copy]
