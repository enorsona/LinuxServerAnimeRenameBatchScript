import os, re
import sys


yes: list[str] = ['yes', 'y']
no: list[str] = ['no', 'n']


def get_return(_default):
    if _default.lower() in yes:
        return 1
    elif _default.lower() in no:
        return 0


def entry():
    os.chdir('/shared/unc-anime/')
    _l = os.listdir()
    for i in range(0, len(_l)):
        print('[' + str(i) + ']: ' + _l[i])
    _input = int(input('请选择文件夹：'))
    os.chdir(os.getcwd() + '/' + _l[_input])
    print('当前文件夹为：' + os.getcwd())
    print('当前默认移动目标为：/shared/anime/')
    _path = '/shared/anime/'
    _new_dir = input('请输入目标文件夹名：')
    _season = str('/Season 0' + (input('请输入季数：')))
    _p = _path + _season + _new_dir
    print('指定目标文件夹为：' + _p)
    _confirm = input('要继续吗？[Y/N]')
    if get_return(_confirm) == 0:
        sys.exit()
    elif get_return(_confirm) == 1:
        os.mkdir(_p)
        for i in range(0, len(_l)):
            _e = _l[i][_l[i].rfind('.'):]
            _c = _l[i][(re.search(r'\d\d', _l[i]).span()[0]):(re.search(r'\d\d', _l[i]).span()[1])]
            os.renames(_l[i], _p + _c + _e)


if __name__ == '__main__':
    entry()
