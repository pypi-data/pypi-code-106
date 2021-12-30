import os
import sys

import requests

from .utils import CmdUtil,IoUtil,StringUtil,PathUtil
os.environ['ANSI_COLORS_DISABLED']="1"
import fire
def pkfire(*args,**kwargs):
    CmdUtil.run_command(['pkx','firex',*sys.argv[1:]])
def main():
    fire.Fire(pkfire)
if __name__ == '__main__':
    main()