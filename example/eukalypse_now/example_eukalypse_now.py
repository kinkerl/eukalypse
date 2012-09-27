#example eukalyps
from configobj import ConfigObj
import sys
import os
import inspect
sys.path.append(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), '../../eukalypse'))
from eukalypse_now import EukalypseNow


#load a settings file
config = ConfigObj('default.cfg')


enow = EukalypseNow()
enow.run(config)
