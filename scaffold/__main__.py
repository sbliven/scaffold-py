"""Creates a project skeleton for a new python project, per the recommended steps
in Learn Python the Hard Way Exercise #46 (http://learnpythonthehardway.org/book/ex46.html)"""

import argparse
from scaffold import projectfolders, projectfiles
import os
import logging

parser = argparse.ArgumentParser(description='Scaffolding tool for simple Python projects', epilog='Report any issues to [Github url]')
parser.add_argument('-p','--project',required=True, nargs=1, help='The name of the project to create')
parser.add_argument('-f','--force',default=False, action='store_true', help='Force creation in a non-empty directory')
parser.add_argument('-d','--dir',required=False, nargs=1, help='The root directory for the project (default: current directory)')
parser.add_argument('-v', '--verbose', help='Long messages', default=False, action='store_true')

args = parser.parse_args() #Unpack the commandline arguments

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG if args.verbose else logging.WARN)

root_dir = os.getcwd() #Get the current working directory as our default root project directory

if args.dir != None: #If the user set an explicit output directory
    root_dir = args.dir[0]

def main():
    try:
        projectfolders.create_folders(args.project[0], root_dir, force=args.force)
        projectfiles.create_files(args.project[0], root_dir)
    except IOError as e:
        logging.debug(e, exc_info=True)
        print(e.strerror)

if __name__ == "__main__":
    main()
