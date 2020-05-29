"""Creates the folder skeleton for a new Python project"""
import os
import logging
from textwrap import dedent


def check_empty(directory, warn=False):
    """Checks if the directory is empty and raises a error or warning.

    Ars:
    - directory (str)
    - warn (bool): only warn errors rather than raising IOError

    Return: True if the directory was empty or did not exist
    """
    if os.path.exists(directory) and os.listdir(directory):
        if warn:
            logging.warn="Forcing project creation in non-empty dir: {}".format(directory)
            return False
        else:
            #If the path already exists and it is not empty, raise an error
            err_msg = '''
                {directory} already exists and it is not empty.

                Please use a unique root directory, or specify -f to overwrite the existing project.

                '''.format(directory=directory)
            raise IOError(000, dedent(err_msg))


def create_folders(project_name, root_dir, force=False):
    """Creates all of the requisite folders in the project skeleton"""
    # Create root if needed; error/warn if non-empty
    if check_empty(root_dir, warn=force):
        make_folder(root_dir, exist_ok=force) #Create the root directory

    dirnames = (project_name, 'bin', 'tests', 'docs')

    #Create all the other directories
    for item in dirnames:
        directory = create_path(root_dir, item)
        make_folder(directory, ' +++')


def make_folder(path, prefix='', exist_ok=True):
    """Creates the directory and prints a message to notify the user"""
    os.makedirs(path, exist_ok=exist_ok)

    if os.path.exists(path) is False: #If we were unable to make the directory for some reason...
        err_msg = 'Unable to create root directory {path_}. Unknown error!'.format(path_=path)
        raise IOError(000, err_msg, '')

    print("create: {prefix} {path_}".format(
        prefix=prefix,
        path_=os.path.abspath(path)
    ))


def create_path(current_directory, new_folder_name):
    """Gets the absolute path of the new folder we're going to create"""
    current_directory = os.path.abspath(current_directory)
    return os.path.join(current_directory, new_folder_name)
