import argparse
from compileall import compile_dir
from gooey import Gooey, GooeyParser


@Gooey(program_name="Test program",
       default_size=(710, 700),
       navigation='TABBED', 
       header_bg_color = '#638dbe',
       body_bg_color = '#FFF900')

def parse_args():
    parser = GooeyParser()
    price_group = parser.add_argument_group('Acció')
    price_group.add_argument("accio",
            metavar='Quina accio fem?',
            action = 'store',
            choices=['Compilar', 'Executar','Llegir'])
    postcode_group = parser.add_argument_group('File')
    postcode_group.add_argument('fitxer',
                        metavar='A quin fitxer li fem la acció?',
                        widget='FileChooser',
                        help = "file name")
    args = parser.parse_args()
    return args

def resultat(message):
    import wx
    app = wx.App()
    dlg = wx.MessageDialog(None, message, 'dsfasdfa', wx.ICON_INFORMATION)
    dlg.ShowModal()

def show_error_message(message):
    import wx
    app = wx.App()
    dlg = wx.MessageDialog(None, message, 'Whoops', wx.ICON_INFORMATION)
    dlg.ShowModal()

def compilar(fitxer):
    import os
    import compileall
    import shutil

    path = os.path.dirname(fitxer)
    fitxer = os.path.basename(fitxer)
    
    os.system('cd '+ path)
    compileall.compile_file(path+'\\'+fitxer, force=True)
    f_name, f_ext = os.path.splitext(fitxer)
    shutil.copyfile(path+"\\__pycache__\\"+f_name +".cpython-39.pyc", path+"\\"+f_name+".cpython-39.pyc")
    shutil.rmtree(path+"\\__pycache__")

def executar(fitxer):
    exec(fitxer)

def llegir(fitxer):
    try:
        with open(fitxer, 'r') as f:
            print(f.read())
    except Exception as e:
        print("Document illegible. Comprova que sigui text pla")

if __name__ == '__main__':
    args = parse_args()

    accio = args.accio
    fitxer = args.fitxer

    if accio == "Compilar":
        compilar(fitxer)
    elif accio == "Executar":
        executar(fitxer)
    elif accio == "Llegir":
        llegir(fitxer)
