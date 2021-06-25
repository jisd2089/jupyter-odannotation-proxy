import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel('INFO')


def setup_odannotation():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """
    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'icons', 'example: foo.svg'
    )

    # Make sure executable is in $PATH
    def _get_odannotation_command(port):
        executable = shutil.which('odannotation')
        if not executable:
            raise FileNotFoundError('Can not find odannotation executable in $PATH')
        # Create theia working directory
        home_dir = os.environ.get('HOME') or '/home/jovyan'
        working_dir = f'{home_dir}/odannotation'
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
            logger.info("Created directory %s" % working_dir)
        else:    
            logger.info("Directory %s already exists" % working_dir)
        return ['odannotation']
    
    return {
        'command': '_get_odannotation_command',
        'timeout': 20,
        'new_browser_tab': True,
        'launcher_entry': {
            'title': 'Odannotation IDE',
            'icon_path': _get_icon_path()
        },
    }
