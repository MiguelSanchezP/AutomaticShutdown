# AutomaticShutdown
## Description
Little python that shuts a Linux machine down when there is a period of thirty minutes without activity. The values specified on this file may vary depending on the CPU of every system. 
## Dependencies
* `sysstats/sar` This comand is used to record the activity of the CPU on intervals of 10 minutes.
* `python3` It is necessary to compile the file and execute it
## Installation
There is no installation needed for this file, but for a correct behaviour of this script, it should be added to cron with the time specification `@reboot`. The user whose cron is given the instruction should not have restrictions when shutting down the machine.

Additionally, the user may like to generate his own CPU usage statistics through different situations and analyse them with the `plot.py` file that is also found on the project, this way he can adjust the values of the script to others more suitable.
