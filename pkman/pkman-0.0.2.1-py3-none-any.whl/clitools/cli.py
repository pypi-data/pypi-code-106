import os
import sys
from .utils import CmdUtil,IoUtil
from .config import PACKGAE_CONFIG_FILENAME
os.environ['ANSI_COLORS_DISABLED']="1"
import fire
from . import apis

def load_pkg_info():
    pkg_info = IoUtil.json_load(os.path.join(os.getcwd(), PACKGAE_CONFIG_FILENAME))
    return pkg_info

class CLI:


    def hi(cls):
        print('Hi, welcome to use pkman !'.center(50, '*'))

    @classmethod
    def cmd(cls, *args, **kwargs):
        CmdUtil.run_command(sys.argv[2:])
    @classmethod
    def build(cls):
        pass
    @classmethod
    def config(cls):
        pass
    @classmethod
    def docs(cls):
        pass
    @classmethod
    def init(cls):
        apis.init()
    @classmethod
    def install(cls):
        pass
    @classmethod
    def list(cls):
        pass
    @classmethod
    def ls(cls):
        pass
    @classmethod
    def login(cls):
        pass
    @classmethod
    def logout(cls):
        pass
    @classmethod
    def publish(cls):
        pass
    @classmethod
    def run(cls,cmd):
        pkg_info=load_pkg_info()
        scripts=pkg_info['scripts']
        if cmd in scripts:
            CmdUtil.run_command([scripts[cmd]])
        else:
            raise Exception('Command not found: %s'%(cmd))
    @classmethod
    def search(cls):
        pass
    @classmethod
    def uninstall(cls):
        pass
    @classmethod
    def unpublish(cls):
        pass
    @classmethod
    def update(cls):
        pass
    @classmethod
    def version(cls):
        pkg_info=load_pkg_info()
        print(pkg_info['version'])
    @classmethod
    def test(cls):
        return cls.run('test')


    @classmethod
    def testsysargv(cls, *args, **kwargs):
        import sys
        print("sys.argv:", sys.argv)
        print("executable:", sys.executable)

def main():
    fire.Fire(CLI())

if __name__ == '__main__':
    main()