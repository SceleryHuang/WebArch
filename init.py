import os

root_path = os.getcwd()

dir_list = ['dbconnector','exceptions','helper','route','session','template_engine','view','wsgi_adapter']

children = {'name':'__init__.py','children':None,'type':'file'}

dir_map = [{
    # name 为框架的名字，记得修改好名字，不然脚本运行会报错，建议使用与后续实验匹配的“sylfk”来命名
    'name': 'sylfk',
    'children': [{
        'name': directory,
        'type': 'dir',
        'children': [children]
    } for directory in directory_list] + [children],
    'type': 'dir'
}]


def create(path,kind):
    if kind == 'dir':
        os.mkdir(path)
    else:
        open(path,'w').close()

def gen