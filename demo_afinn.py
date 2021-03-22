import os
from utils.readfile import read_afinn_txt

if __name__ == '__main__':
    # 准备一个路径
    path_afinn = os.path.join('files', 'AFINN.txt')
    infos_afinn = ['sentiment', 'score']

    # 实例化一个对象
    obj_afinn = read_afinn_txt.Afinn(path_afinn, infos_afinn)

    # 读取txt文件
    try:
        obj_afinn.read_afinn()
        # 输出afinn_dict
        for item in obj_afinn.afinn_dict:
            print(item)

    except Exception as e:
        print('读取文件异常！原因：' + str(e))