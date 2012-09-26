from eukalypse import Eukalypse

import os
import datetime

class EukalypseNow:
	def run(self, config):
		reportfolder = os.path.join(config['general']['report_output_path'], str(datetime.datetime.now()))
		os.makedirs(reportfolder)
		e = Eukalypse()
		e.browser = 'chrome'
		e.output = reportfolder

		for test_key in config['tests']:
			test = config['tests'][test_key]
			eukalypse_result_object = e.compare(test_key, test['reference_image'], test['url'])
			print eukalypse_result_object.clean

		e.disconnect()

		#write report

		#sendmail
		if config['general']['report_send_mail']:
			print "mailsending not yet implemented"
		#	config['general']['operator_name']
		#	config['general']['operator_mail']
