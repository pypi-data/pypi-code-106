import subprocess
import sys


def run_command(args):
    return subprocess.call(" ".join(args), shell=True)
def run_python_script(path,args):
    return run_command([sys.executable,path,*args])
def gen_fire_argv(*args, **kwargs):
    argv = []
    for arg in args:
        argv.append(str(arg))
    for k, v in kwargs.items():
        argv.append('--%s=%s' % (k, v))
    return argv


