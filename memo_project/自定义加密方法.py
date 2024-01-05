import base64

a = "周杰伦"
b = "abc"

# print(a.encode("gbk"))  # 编码
# print(a.encode("utf-8"))
#
# print(base64.b64encode(b'\xe5\x91\xa8\xe6\x9d\xb0\xe4\xbc\xa6'))

"""
中文 → b"\xd6"  字节 bytes → 01010101  bit 位
"""

"""
作业：
写一个自定义加密函数，给你一个字符，你要先转换成字节，再进行base64编码，然后根据你提供的秘钥组合成  
body + 秘钥  (字节的组合)
把字节转成字符串返回回去。

解码方式

"""


def encode_str(body, key):
    '''
    :param body: 需要加密的内容
    :param key: 秘钥
    :return: 加密后的字符串
    '''
    if type(body) and type(key) in (str, bytes, bytearray):
        byte_body = body.encode('utf-8')
        byte_key = key.encode('utf-8')
        import base64
        base64_body_byte = base64.b64encode(byte_body)
        base64_key_byte = base64.b64encode(byte_key)
        res = str(base64_body_byte + base64_key_byte)
        print(res)
    else:
        print('你输入的数据类型不支持编码')


encode_str('Jayden', '我的生日')


def decode_str(body: bytes or str, key):
    import base64
    if type(body) and type(key) in (str, bytes, bytearray):
        body_byte = base64.b64decode(body)
        key_byte = key.encode('utf-8')
        res = body_byte.strip(key_byte)
        res = res.decode('utf-8')
        print(res)
        print('请输入字符串')
    else:
        print('你输入的数据类型不支持编码')


decode_str(b'SmF5ZGVu5oiR55qE55Sf5pel', '我的生日')
