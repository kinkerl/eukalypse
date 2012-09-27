#example eukalyps
from configobj import ConfigObj
from eukalypse_now import EukalypseNow

#load a settings file
config = ConfigObj('default.cfg')

enow = EukalypseNow()
enow.run(config)
