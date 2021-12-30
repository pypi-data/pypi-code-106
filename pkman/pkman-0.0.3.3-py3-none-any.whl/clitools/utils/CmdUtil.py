import subprocess
import sys
import os
from .AppDataManager import AppDataManager
from . import StringUtil,IoUtil
app_data_manager=AppDataManager('.pkman/tmp_code')

def run_command(args):
    return subprocess.call(" ".join(args), shell=True)
def run_batch_code(code):
    filename=StringUtil.hash_text(code)[:10]+'.bat'
    file_path=app_data_manager.tempfile(filename)
    IoUtil.write_txt(code,file_path)
    res=os.system(file_path)
    os.remove(file_path)
    return res
def run_python_script(path, args, extend_path=None):
    if extend_path is None:
        extend_path = []
    cmd=[sys.executable,path,*args]
    if extend_path:
        if os.name == 'nt':
            code = 'set PYTHONPATH=%s' % (';'.join(extend_path)) + ' & ' + ' '.join(cmd)
            return run_command([code])
        else:
            code='export PYTHONPATH=%s'%(':'.join(extend_path))+' && '+ ' '.join(cmd)
            return run_command([code])
    else:
        return run_command(cmd)
def gen_fire_argv(*args, **kwargs):
    argv = []
    for arg in args:
        argv.append(str(arg))
    for k, v in kwargs.items():
        argv.append('--%s=%s' % (k, v))
    return argv


