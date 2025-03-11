from gpiopico.input_devices import *
from gpiopico.output_devices import *
from gpiopico.utils import *

"This import only load with raspi pico w or wh"
try:
    from gpiopico.network_device import Network
except ImportError:
    print('Import Error, cant use Network')
    pass
