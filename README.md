appd_metric_check.py
--------------------

appdynamics nagios/icinga metric check. use if you want to use icinga/nagios for alarming.

    usage: appd_metric_check.py [-h] [-H HOST] [-P PORT] [-u USERNAME]
                                [-p PASSWORD] [-d DURATION] [-a APPLICATION]
                                [-c CURRENT] [-b BUSINESSTRANSACTION] [-w WARNING]
                                [-m MAX] [-n NAME]

    Shop Operations Appdynamics Metric Check

    optional arguments:
      -h, --help            show this help message and exit
      -H HOST, --host HOST  hostname/IP of appdynamics controller
      -P PORT, --port PORT  port number off Appdynamics controller(default: 8090)
      -u USERNAME, --username USERNAME
                            username (username@customer)
      -p PASSWORD, --password PASSWORD
                            password
      -d DURATION, --duration DURATION
                            duration to query in minutes (default: 5)
      -a APPLICATION, --application APPLICATION
                            application name
      -c CURRENT, --current CURRENT
                            use the current value - only for BTs that carry this
                            info (default: false)
      -b BUSINESSTRANSACTION, --businesstransaction BUSINESSTRANSACTION
                            Business Transaction
      -w WARNING, --warning WARNING
                            warning threshold
      -m MAX, --max MAX     critical threshold
      -n NAME, --name NAME  Name Shown in Additional Info, otherwise given BT will
                            be used
