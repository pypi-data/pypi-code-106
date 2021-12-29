import argparse
import os

# Due to the pymatgen is incorrect of band gap with 2 spin. we use vaspkit for extract data.
import pandas as pd
import pymatgen.io.vasp
from mgetool.imports import BatchFile
import os

import numpy as np


# 1
# LAECHG=.TRUE.
# LCHARG = .TRUE.
# NSW = 0
# IBRION = -1 (前面有了NSW = 0, 这个也可以不设置)

# 2
# chmod u+x ~/bin/chgsum.pl
# chmod u+x ~/bin/bader

from pymatgen.io.vasp import Potcar, Poscar


def cal(d, store=False, store_name="temp.csv"):
    """Run linux cmd and return result, make sure the vaspkit is installed."""
    old = os.getcwd()
    os.chdir(d)
    try:
        #
        cmd_sys()
        # >>>
        result = read(d, store=store, store_name=store_name)
        # <<<

        os.chdir(old)
        return result
    except BaseException as e:
        print(e)
        print("Error for:", d)

        os.chdir(old)
        return None


def cal_all(d, repeat=0, store=False, store_name="temp_all.csv"):
    data_all = []
    col = None
    for di in d:
        res = cal(di)

        if isinstance(res, pd.DataFrame):
            col = res.columns
            res = res.values
            if repeat <= 1:
                data_all.append(res)
            else:
                for i in range(repeat):
                    res2 = res
                    res2[:, 0] = res2[:, 0] + f"-S{i}"
                    data_all.append(res2)
        else:
            pass
    data_all = np.concatenate(data_all, axis=0)
    result = pd.DataFrame(data_all, columns=col)

    if store:
        result.to_csv(store_name)
        print("'{}' are sored in '{}'".format(store_name, os.getcwd()))

    return data_all


def read(d, store=False, store_name="temp.csv"):
    """Run linux cmd and return result, make sure the vaspkit is installed."""
    if os.path.isfile("POTCAR") and os.path.isfile("POSCAR"):
        potcar = Potcar.from_file("POTCAR")
        symbols = Poscar.from_file("POSCAR").structure.atomic_numbers

        zval = []
        for i in symbols:
            for j in potcar:
                if j.atomic_no == i:
                    zval.append(j.ZVAL)
                    break

        zval = np.array(zval)

        with open("ACF.dat", mode="r") as f:
            msg = f.readlines()

        msg = [i for i in msg if ":" not in i]
        msg = [i for i in msg if "--" not in i]
        msg = [i.replace("\n", "") if "\n" in i else i for i in msg]
        msg = [i.split(" ") for i in msg[1:]]
        msg = [[k for k in i if k != ""] for i in msg]
        msg2 = np.array(msg).astype(float)

        msg_append = (msg2[:, 4] - zval).reshape(-1, 1)
        msg_f = np.full(msg2.shape[0], fill_value=str(d)).reshape(-1, 1)
        msg2 = np.concatenate((msg_f, msg2, msg_append), axis=1)
        ta = np.array(["File", "Atom Number", "X", "Y", "Z", "CHARGE", " MIN DIST", " ATOMIC VOL",
                       "Bader Ele Move"])

        result = pd.DataFrame(msg2, columns=ta)
        if store:
            result.to_csv(store_name)
            print("'{}' are sored in '{}'".format(store_name, os.getcwd()))

        return result
    else:
        return None


def cmd_sys(cmds=("chgsum.pl AECCAR0 AECCAR2", "bader CHGCAR -ref CHGCAR_sum")):
    if not cmds:
        pass
    else:
        for i in cmds:
            os.system(i)


def run(args, parser):
    if args.job_type in ["S", "s"]:
        res = cal(args.path_name, store=True, store_name=args.out_name)

        print(args.dir_name, res)
    else:
        assert args.job_type in ["M", "m"]
        bf = BatchFile(args.path_name, suffix=args.suffix)
        bf.filter_dir_name(include=args.dir_include, exclude=args.dir_exclude, layer=args.layer)
        bf.filter_file_name(include=args.file_include, exclude=args.file_exclude)
        bf.merge()

        fdir = bf.file_dir

        fdir.sort()

        if not fdir:
            raise FileNotFoundError("There is no dir meeting the requirements after filter.")

        if not args.abspath:
            absp = os.path.abspath(args.path)
            fdir = [i.replace(absp, ".") for i in fdir]

        if "All" not in args.out_name or "all" not in args.out_name:
            name = "All_" + args.out_name
        else:
            name = args.out_name

        cal_all(fdir, repeat=args.repeat, store=True, store_name=name)


class CLICommand:
    """
    批量提取 bader，保存到当前工作文件夹。 查看参数帮助使用 -h。
    在 featurebox 中运行，请使用 featurebox bader ...
    若复制本脚本并单运行，请使用 python bader.py ...

    首先，请确保 运算子文件夹(sample_i_dir)包含应有 vasp 输入输出文件。
    parent_dir(为上层目录，或者上n层目录)

    Notes:
        1. 前期准备
        需要以下文件：~/bin/bader, ~/bin/chgsum.pl
        并赋予权限:
        # chmod u+x ~/bin/chgsum.pl
        # chmod u+x ~/bin/bader

        # INCAR文件参数要求：
        # LAECHG= .TRUE.
        # LCHARG = 11
        # NSW = 0
        # IBRION = -1

        2.运行文件要求:
        chgsum.pl,bader,
        AECCAR0，AECCAR2，CHGCAR


    如果在 featurebox 中运行多个案例，请指定顶层文件夹:

    Example:

        $ featurebox bader -p /home/parent_dir -if AECCAR0

    如果在 featurebox 中运行单个案例，请指定运算子文件夹:

    Example:

        $ featurebox bader -t s -p /home/parent_dir/***/sample_i_dir -if AECCAR0

    """

    @staticmethod
    def add_arguments(parser):
        parser.add_argument('-p', '--path_name', type=str, default='.')
        parser.add_argument('-t', '--job_type', type=str, default='m')
        parser.add_argument('-s', '--suffix', help='suffix of file', type=str, default=None)
        parser.add_argument('-if', '--file_include', help='include file name.', type=str, default="AECCAR0")
        parser.add_argument('-ef', '--file_exclude', help='exclude file name.', type=str, default=None)
        parser.add_argument('-id', '--dir_include', help='include dir name.', type=str, default=None)
        parser.add_argument('-ed', '--dir_exclude', help='exclude dir name.', type=str, default=None)
        parser.add_argument('-l', '--layer', help='dir depth, default the last layer', type=int, default=-1)
        parser.add_argument('-abspath', '--abspath', help='return abspath', type=bool, default=True)
        parser.add_argument('-repeat', '--repeat', help='repeat times', type=int, default=0)
        parser.add_argument('-o', '--out_name', help='out file name.', type=str, default="bader.csv")

    @staticmethod
    def run(args, parser):
        run(args, parser)


if __name__ == '__main__':
    """
    Example:
        $ python bader.py -p /home/dir_name -if AECCAR0
    """
    parser = argparse.ArgumentParser(description="Get d band centor.Examples:\n"
                                                 "python bader.py -p /home/dir_name -if AECCAR0")
    parser.add_argument('-p', '--path_name', type=str, default='.')
    parser.add_argument('-t', '--job_type', type=str, default='m')
    parser.add_argument('-s', '--suffix', help='suffix of file', type=str, default=None)
    parser.add_argument('-if', '--file_include', help='include file name.', type=str, default="AECCAR0")
    parser.add_argument('-ef', '--file_exclude', help='exclude file name.', type=str, default=None)
    parser.add_argument('-id', '--dir_include', help='include dir name.', type=str, default=None)
    parser.add_argument('-ed', '--dir_exclude', help='exclude dir name.', type=str, default=None)
    parser.add_argument('-l', '--layer', help='dir depth, default the last layer', type=int, default=-1)
    parser.add_argument('-abspath', '--abspath', help='return abspath', type=bool, default=True)
    parser.add_argument('-repeat', '--repeat', help='repeat times', type=int, default=3)
    parser.add_argument('-o', '--out_name', help='out file name.', type=str, default="bader.csv")
    args = parser.parse_args()
    run(args, parser)
