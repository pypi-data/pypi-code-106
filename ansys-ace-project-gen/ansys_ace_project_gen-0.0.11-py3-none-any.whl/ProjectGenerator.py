# Copyright (c) 2022 Ansys, Inc. and its affiliates. Unauthorised use, distribution or duplication is prohibited
# LICENSE file is in the root directory of this source tree.
import os
import subprocess
import shutil
import emoji
import coloredlogs
import logging
from easygui import *

os.environ['COLOREDLOGS_LOG_FORMAT'] = '%(asctime)s [%(levelname)s] %(message)s'
os.environ['COLOREDLOGS_DATE_FORMAT'] = '%H:%M:%S'
os.environ['COLOREDLOGS_FIELD_STYLES'] = 'levelname=15; asctime=14'
os.environ['COLOREDLOGS_LEVEL_STYLES'] = 'info=35;debug=28;warning=202;error=14;error=background=red'
# Create a logger object.
logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def hasPipx():
    try:
        subprocess.run(["pipx", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logger.info("pipx installed")
        return True
    except:
        logger.error("pipx is not installed. Follow these instructions https://pypa.github.io/pipx/installation/")
        return False


def get_templates(templates_directory):
    templates = None

    if not os.path.isdir(templates_directory):
        logger.error("Templates not found")
        raise Exception('templates directory not found')
    else:
        templates = os.listdir(templates_directory)
    return [x for x in templates if x != 'shared' and not x.startswith('.') and not x.startswith('README')]


def copy_template(templates_directory, template, destination):
    # Copy shared resources
    shared_directory = os.path.join(templates_directory, 'shared')
    shutil.copytree(shared_directory, destination, dirs_exist_ok=True)

    # Copy template resources
    template_directory = os.path.join(templates_directory, template)
    shutil.copytree(template_directory, destination, dirs_exist_ok=True)


def generate_project_folder(root_directory, project_name=None, user_template=None):
    templates_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
    available_templates = get_templates(templates_dir)

    if not project_name:
        project_name = enterbox("Project Name", "Ansys ACE Project Generator", "What should we name your project ?")

    destination_directory = os.path.join(root_directory, project_name)
    if os.path.isdir(destination_directory):
        logger.error(f"Directory already exists at path {destination_directory}")
        exit(1)

    if not user_template:
        logger.error("A template choice is missing in your command")
        logger.info("Get help for commands with pipx run ansys-ace-project-gen --help")
        exit(1)
    if user_template in available_templates:
        copy_template(templates_dir, user_template, destination_directory)
    else:
        logger.error(f"Selected template not available.")
        logger.info("Here are the templates available.")
        print(available_templates)
        exit(1)

    logger.info(f"{project_name} initialized successfully !")
    print(emoji.emojize(f"""{Colors.OKCYAN}We recommend you the following steps to pursues")
        1- Go inside the created directory by running cd ./{project_name} 
        2- Push this project in git remote repository"
            2.1 [Optional] -  git init
            2.1 [Optional] -  git remote add origin <git_repository_url>")
            2.1 [Optional] -  git add . && git commit -m \"initial commit\"")
            2.1 [Optional] -  git push origin main {Colors.OKCYAN} 

    {Colors.WARNING}:collision: :star-struck: :star-struck: :star-struck: :star-struck: :collision:{Colors.WARNING}"""))
    logger.info(emoji.emojize('Success :thumbs_up:  :clapping_hands:'))
