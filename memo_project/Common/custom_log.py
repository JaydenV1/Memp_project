import time
import datetime
import os
from colorama import Fore
import inspect

now_dir = os.path.dirname(os.path.dirname(__file__))  # 获取主目录路径
now_time = datetime.datetime.now()
str_time = now_time.strftime("%Y-%m-%d")
log_dir = now_dir + '/Log/'


def info_log(text):
    date = time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time()))
    log_text = "[INFO]{}: {}\n".format(date, text)
    print(Fore.GREEN + str(log_text).strip())
    log_name = "{}_info.txt".format(str_time)
    with open(log_dir + log_name, "a", encoding="utf-8") as f:
        f.write(log_text)


def error_log(text):
    date = time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time()))
    log_text = "[ERROR]{}: {}\n".format(date, text)
    print(Fore.RED + str(log_text).strip())
    log_name = "{}_error.txt".format(str_time)
    with open(log_dir + log_name, "a", encoding="utf-8") as f:
        f.write(log_text)


def warning_log(text):
    date = time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time()))
    log_text = "[WARN]{}: {}\n".format(date, text)
    print(Fore.BLUE + str(log_text).strip())
    log_name = "{}_error.txt".format(str_time)
    with open(log_dir + log_name, "a", encoding="utf-8") as f:
        f.write(log_text)


def log_method_call(func):
    def wrapper(*args, **kwargs):
        class_name = args[0].__class__.__name__  # 获取类名
        method_name = func.__name__  # 获取方法名
        # stack = inspect.stack()  # 获取方法执行的代码路径
        docstring = inspect.getdoc(func)  # 获取方法注释
        # code_path = f"{stack[1].filename}:{stack[1].lineno}"
        # info_log(f"at {code_path}: {docstring}")
        info_log(f'TestCase: {method_name} of class {class_name}')
        info_log(f"Case msg: {docstring}")
        return func(*args, **kwargs)

    return wrapper


def log_class_methods(cls):
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if name.startswith('testCase'):
            setattr(cls, name, log_method_call(method))  # 类级别的装饰器，第一个形参：类，第二个形参：方法，第三形参：方法的装饰器
    return cls


if __name__ == '__main__':
    info_log("hello word!!!")
    error_log("蠢问题拉")


"""
20230429bug:
1.获取方法执行的代码路径 读取的是unittest的源码路径，不是方法执行的路径
2.如果是使用这个装饰器，beautifulreport的描述为null
"""