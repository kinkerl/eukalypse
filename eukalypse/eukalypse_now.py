from eukalypse import Eukalypse

import os
import datetime
import sys
import ConfigParser
import logging as logger
logger.basicConfig(level=logger.INFO)


class EukalypseNow:
	def run(self, config):


		config = ConfigParser.ConfigParser()
		config.read("config.cfg")

		reportfolder = os.path.join(config.get('general', 'report_output_path'), str(datetime.datetime.now()))
		os.makedirs(reportfolder)
		e = Eukalypse()
		e.browser = 'chrome'
		e.output = reportfolder


#fix me here
#		for test_key in config['tests']:
#			test = config['tests'][test_key]
#			eukalypse_result_object = e.compare(test_key, test['reference_image'], test['url'])
#			logger.debug(eukalypse_result_object.clean)

		e.disconnect()

		#write report

		#sendmail
		if config.get('general', 'report_send_mail'):
			logger.warn("mailsending not yet implemented")


def main(argv):
	"""
	the main function. the command line arguments are processed here and the next actions are started here too
	"""
	args = argv[1:]

	#cli options
	from optparse import OptionParser
	parser = OptionParser(usage = "eukalypse now")

	parser.add_option("--config", dest="config", default=None, help="supply a configuration")
	(options, args) = parser.parse_args(args)

	enow = EukalypseNow()
	enow.run(options.config)

if __name__ == '__main__':
	try:
		main(sys.argv)
	except Exception as e:
		raise