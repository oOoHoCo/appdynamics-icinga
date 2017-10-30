#!/usr/bin/env python
import argparse
import base64
import json
import urllib
import urllib2


def dumpclean(obj):
	if type(obj) == dict:
		for k, v in obj.items():
			if hasattr(v, '__iter__'):
				print k
				dumpclean(v)
			else:
				print '%s : %s' % (k, v)
	elif type(obj) == list:
		for v in obj:
			if hasattr(v, '__iter__'):
				dumpclean(v)
			else:
				print v
	else:
		print obj


translate_status = {
	0: 'OK',
	1: 'WARNING',
	2: 'CRITICAL',
	3: 'UNKNOWN'
}


def main():
	status = 3

	parser = argparse.ArgumentParser(description="Shop Operations Appdynamics Metric Check")
	parser.add_argument("-H", "--host", help="hostname/IP of appdynamics controller",
	                    default="http://accshmonitorfebsa01.fe.server.lan")
	parser.add_argument("-P", "--port", help="port number off Appdynamics controller(default: 8090)", default="8090")
	parser.add_argument("-u", "--username", help="username (username@customer)")
	parser.add_argument("-p", "--password", help="password")
	parser.add_argument("-d", "--duration", help="duration to query in minutes (default: 5)", default="5")
	parser.add_argument("-a", "--application", help="application name")
	parser.add_argument("-c", "--current",
	                    help="use the current value - only for BTs that carry this info (default: false)",
	                    default=False)
	parser.add_argument("-b", "--businesstransaction", help="Business Transaction")
	parser.add_argument("-w", "--warning", help="warning threshold", type=int)
	parser.add_argument("-m", "--max", help="critical threshold", type=int)
	parser.add_argument("-n", "--name", help="Name Shown in Additional Info, otherwise given BT will be used")
	args = parser.parse_args()

	try:
		addinfo = args.businesstransaction
		if args.name:
			addinfo = args.name
		bt = urllib.quote_plus(args.businesstransaction)
		url_to_query = '{}:{}/controller/rest/applications/{}/metric-data?metric-path={}&time-range-type=BEFORE_NOW&duration-in-mins={}&output=JSON'.format(
			args.host, args.port, args.application, bt, args.duration)
		request = urllib2.Request(url_to_query)
		if args.username:
			base64string = base64.b64encode('{}:{}'.format(args.username, args.password))
			request.add_header("Authorization", "Basic {}".format(base64string))
		request.add_header("Accept", "application/json")
		url = urllib2.urlopen(request)

		result = json.loads(url.read())
		if args.current:
			value = result[0]['metricValues'][0]['current']
			if value > args.max:
				if status != 2:
					status = 2
			if value > args.warning:
				if status != 2 and status != 1:
					status = 1
			if value < args.warning:
				if status != 2 and status != 1 and status != 0:
					status = 0
		else:
			value = result[0]['metricValues'][0]['value']
			if value > args.max:
				if status != 2:
					status = 2
			if value > args.warning:
				if status != 2 and status != 1:
					status = 1
			if value < args.warning:
				if status != 2 and status != 1 and status != 0:
					status = 0
		print("{} - {} is at {} ms ({} warning | {} critical)".format(translate_status[status],
		                                                              addinfo, value, args.warning, args.max))
		exit(status)
	except Exception, e:
		print("{} - {} - {}".format(translate_status[status], addinfo, e))
		exit(3)


if __name__ == "__main__":
	main()
  
