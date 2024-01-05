import yaml


def get_yaml(filepath: str):
    """

    :param filepath: 文件路径
    :return: yaml文件内容
    """
    with open(file=filepath, encoding='utf-8') as f:
        return yaml.safe_load(f.read())


def modify_yaml_file(file_path, key, new_value):
    """

    :param file_path: 文件路径
    :param key: 要修改的字典[key]
    :param new_value: 更新的值
    :return: yaml文件内容
    """
    # 读取YAML文件
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f.read())

    # 修改字典内容
    data[key] = new_value

    # 将修改后的内容写回到文件中
    with open(file_path, 'w') as file:
        return yaml.dump(data, file)



