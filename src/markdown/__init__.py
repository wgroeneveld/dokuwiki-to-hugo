# https://docs.python.org/3/tutorial/modules.html
# you need to define __all__ to be able to let from x import * work...
# there is no out-of-the-box dynamic solution
# see http://stackoverflow.com/questions/1057431/loading-all-modules-in-a-folder-in-python

from os.path import dirname, basename, isfile
import glob

modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
print('loaded markdown converters: ' + ', '.join(__all__))
