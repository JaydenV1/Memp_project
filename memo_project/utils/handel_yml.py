# handel_yml
# 2022 / 3 / 11
# # =======
# Jayden

import os
import yaml


def get_yml_data(filepath: str):  # 申明传入的是字符串类型
    with open(filepath, encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())  # 获取yaml数据


if __name__ == '__main__':
    from handel_path import config_path

    resp = get_yml_data(os.path.join(config_path, 'all_elements.yaml'))
    print(resp)
