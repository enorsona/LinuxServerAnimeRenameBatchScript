import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--new', type=str, default=None, help="new name")
parser.add_argument('--origin', type=str, default=None, help="original name")
parser.add_argument('--dir', type=str, default=None, help="folder")
parser.add_argument('--season', type=int, default=1, help="season")
parser.add_argument('--infolder', type=bool, default=False, help="is in folder")
parser.add_argument('--len', type=int, default=2, help='number length')
parser.add_argument('--short', type=bool, default=False, help='short season like 01~13 01~26')
param = parser.parse_args()

default_dir = "/strx/contents/shared/unc-anime/"
default_target_dir = '/strx/contents/shared/anime/'

num = r'\d'


def digit():
    d = ''
    if param.short is True:
        for i in range(0, param.len):
            if i == 0:
                d = '[0-2]'
            else:
                d = d + num
    else:
        for i in range(0, param.len):
            d = d + num
    return d


# 命名类型转换
def under(old_name, mark):
    _to = old_name.split()
    to = ''
    for i in range(0, len(_to)):
        if i == 0:
            to = _to[i]
        else:
            to = to + mark + _to[i]
    return to


def check(now, old_name):
    _o = search(now, old_name)
    _u = search(now, under(old_name, '_'))
    _d = search(now, under(old_name, '.'))
    if _o is None and _u is None and _d is None:
        checked = True
    else:
        checked = False
    return checked


def search(string, key):
    result = re.search(key, string, re.I)
    return result


# 改名单元
def rename(new_name, old_name):
    # 设置操作路径
    os.chdir(op_path())
    # 列出文件列表
    files = os.listdir()
    # 遍历文件列表
    for i in range(0, len(files)):
        now = files[i]
        if check(now, old_name):
            continue
        elif search(now, r'[^sS]' + digit()) is None:
            continue
        else:
            dot = now.rfind('.')
            ext = now[dot:]
            ep = re.sub(r'\D', '', re.search(r'[^sS]' + digit(), now).group(0))
            _new_name = target_path() + new_name + ' - ' + str(ep) + ext
            os.renames(now, _new_name)


# 操作路径
def op_path():
    # 不在文件夹内时返回默认目录
    if param.infolder is False:
        directory = default_dir
        return directory
    else:
        # 在文件夹内且文件夹名为空时
        if param.dir is None:
            _name = param.new
        else:
            _name = param.dir

        os.chdir(default_dir)
        files = os.listdir()
        for i in range(0, len(files)):
            now = files[i]
            if search(now, _name) is None:
                continue
            else:
                print('[' + str(i) + ']' + now)
        _select = int(input('请选择文件夹'))
        _dir = files[_select]
        directory = default_dir + _dir
        return directory


def target_path():
    target = default_target_dir + param.new + '/Season 0' + str(param.season) + '/'
    return target


# 启动单元
def entry():
    # 如果原文件名没有传入
    if param.origin is None:  # → True
        # 新文件名即为原文件名
        rename(param.new, param.new)
    else:
        # 否则传入新文件名和原文件名
        rename(param.new, param.origin)


if __name__ == '__main__':
    entry()
