"""sharepoint_syncher

Usage:
  md2site run --content=<path_to_content_dir> --output=<path_to_output_dir> --log=<path_to_logs_dir>
  sharepoint_syncher version

Options:
  -h --help                         Show this screen.
  --content=<path_to_content_dir>   Source directory of markdown files
  --output=<path_to_output_dir>     Output directory of staticize site
  --log=<path_to_logs_dir>          The logs directory

"""

import os
import sys
import docopt
import datetime
import zc.lockfile
import logging

from .lib import Staticizer

def _create_logger(log_path):
    """ making log file """
    _now = datetime.datetime.now()
    _fname = '%s.sharesyncher.log' % _now.strftime("%Y.%m.%d.%H.%M")
    _path = os.path.join(log_path, _fname)
    _level='DEBUG'
    
    logger = logging.getLogger('com_micheg.md2site')
    level = getattr(logging, _level, 'DEBUG')
    logger.setLevel(level)

    format = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")

    # stdout
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(format)
    logger.addHandler(stream_handler)

    # file
    file_handler = logging.FileHandler(_path)
    file_handler.setFormatter(format)
    logger.addHandler(file_handler)
    
    return logger

def _run(LOG, content_dir, output_dir):
    """ read configs """
    LOG.info('Starting Staticizing')
    tmp = Staticizer('tmpl', 'public', content_dir, output_dir, LOG)
    tmp.render_home()
    tmp.render_files()
    tmp.copy_static_files()
    LOG.info('procedure end...')


def main():
    """ """
    arguments = docopt.docopt(__doc__)
    content = arguments.get('--content')
    output = arguments.get('--output')
    log = arguments.get('--log')

    LOG = None
    lock_file = 'running.lck'
    lock = None
    
    LOG = _create_logger(log)
    
    if arguments['run']:
        try:
            lock = zc.lockfile.LockFile(lock_file)
        except zc.lockfile.LockError:
            LOG.error(f'can get lock...')
            return 1
        try:
            _run(LOG, content, output)
        except:
            LOG.error(f'something has gone very wrong')
        lock.close()

    return 0