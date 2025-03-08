#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


from requests.structures import CaseInsensitiveDict
import copyreg
from io import BytesIO
import random
import string
from urllib.parse import unquote, quote
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
import base64
import binascii
import hashlib
import pickle
import re
import sys


def tobytes(s, encoding="UTF-8") -> bytes:
    """
    convert to bytes
    """
    if isinstance(s, bytes):
        return s
    elif isinstance(s, bytearray):
        return bytes(s)
    elif isinstance(s,str):
        return s.encode(encoding)
    elif isinstance(s, memoryview):
        return s.tobytes()
    else:
        return bytes([s])

def tostr(value, encoding='UTF-8') -> str:
    if value is None:
        return value
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        return value.decode(encoding)
    return str(value)


def tobool(value) -> bool:
    """Return whether the provided string (or any value really) represents true. Otherwise false.
    Just like plugin server stringToBoolean.
    Replace distutils.strtobool
    """
    if not value:
        return False

    val = tostr(value).lower()
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return True
    elif val in ('n', 'no', 'f', 'false', 'off', '0'):
        return False
    else:
        raise ValueError("invalid truth value %r" % (val,))



if sys.version_info >= (3, 9):
    # If Python version is 3.9 or newer, use the built-in removesuffix method
    def removesuffix(s, suffix):
        return s.removesuffix(suffix)
    def removeprefix(s, prefix):
        return s.removeprefix(prefix)
else:
    def removesuffix(self: str, suffix: str) -> str:
        return self[:-len(suffix)] if self.endswith(suffix) else self


    def removeprefix(self: str, prefix: str) -> str:
        if self.startswith(prefix):
            return self[len(prefix):]
        else:
            return self[:]


def url_encode_all(string: str) -> str:
    """
    对所有字符都进行url编码
    @param string:
    @return:
    """
    return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)


def url_decode(string: str) -> str:
    """
    解码url
    @param string:
    @return:
    """
    return unquote(string)


def url_encode(string: str) -> str:
    """
    url编码
    @param string:
    @return:
    """
    return quote(string)


def q_encode_all(text: str, charset: str = "utf-8") -> str:
    """
    RFC 2047 Q编码实现，强制编码所有字符。
    
    参数:
        text: 要编码的字符串
        charset: 字符集，默认为"utf-8"
    
    返回:
        编码后的字符串，格式如=?charset?Q?encoded_text?=
    """
    # 将文本转为指定字符集的字节
    encoded_bytes = text.encode(charset, errors="replace")
    
    # 手动将所有字节转为=XX形式
    qp_text = "".join(f"={byte:02X}" for byte in encoded_bytes)
    
    return f"=?{charset}?Q?{qp_text}?="


def uuencode(binary_data):
    """
    类似java中的UUEncoder实现
    """
    if isinstance(value, str):
        value = value.encode('utf-8')
    # 分块将二进制数据进行 uuencode 编码
    chunk_size = 45
    # At most 45 bytes at once
    encoded_data = ''
    for i in range(0, len(binary_data), chunk_size):
        chunk = binary_data[i:i+chunk_size]
        encoded_chunk = binascii.b2a_uu(chunk)
        encoded_data += encoded_chunk.decode('utf-8')
    return 'begin 644 encoder.buf\n' + encoded_data + 'end\n'




def base64decode(value: str, encoding='utf-8', errors='strict') -> str:
    """
    python3 返回的是bytes
    Decodes string value from Base64 to plain format
    >>> base64decode('Zm9vYmFy')
    'foobar'

    'ignore'：忽略无法解码的字符。直接跳过无法处理的字符，继续解码其他部分。
    'replace'：使用特定字符替代无法解码的字符，默认使用 '�' 代替。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('utf-8', errors='replace') 输出 '世界�'。
    'strict'：默认行为，如果遇到无法解码的字符，抛出 UnicodeDecodeError 异常。
    'backslashreplace'：使用 Unicode 转义序列替代无法解码的字符。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('ascii', errors='backslashreplace') 输出 '\\xe4\\xb8\\x96\\xe7\\x95\\x8c'。
    'xmlcharrefreplace'：使用 XML 实体替代无法解码的字符。例如，b'\xe4\xb8\x96\xe7\x95\x8c'.decode('ascii', errors='xmlcharrefreplace') 输出 '&#19990;&#30028;'。
    'surrogateescape'：将无法解码的字节转换为 Unicode 符号 '�' 的转义码。例如，当解码 Latin-1 字符串时，b'\xe9'.decode('latin-1', errors='surrogateescape') 输出 '\udce9'。

    """
    return str(base64.b64decode(value), encoding=encoding, errors=errors)


def base64encode(value) -> str:
    """
    python3 返回的是bytes
    Encodes string value from plain to Base64 format
    >>> base64encode('foobar')
    'Zm9vYmFy'
    """
    if isinstance(value, str):
        value = value.encode('utf-8')

    return str(base64.b64encode(value), encoding='utf-8')

def base64_urlencode(value) -> str:
    """
    base64encode + urlencode
    """

    return url_encode(base64encode(value))


def base64_urldecode(value: str, encoding='utf-8', errors='strict') -> str:
    """
    urldecode + base64decode
    """
    return base64decode(url_decode(value), encoding=encoding, errors=errors)



def urlsafe_base64encode(value) -> str:
    """
    base64.urlsafe_b64encode
    """
    if isinstance(value, str):
        value = value.encode('utf-8')

    return str(base64.urlsafe_b64encode(value), encoding='utf-8')


def urlsafe_base64decode(value: str, encoding='utf-8', errors='strict') -> str:
    """
    base64.urlsafe_b64decode
    """
    return str(base64.urlsafe_b64decode(value), encoding=encoding, errors=errors)



def base64pickle(value):
    """
    Serializes (with pickle) and encodes to Base64 format supplied (binary) value
    >>> base64pickle('foobar')
    'gAJVBmZvb2JhcnEALg=='
    """

    retVal = None

    try:
        retVal = base64encode(pickle.dumps(value, pickle.HIGHEST_PROTOCOL))
    except:
        warnMsg = "problem occurred while serializing "
        warnMsg += "instance of a type '%s'" % type(value)
        print(warnMsg)

        try:
            retVal = base64encode(pickle.dumps(value))
        except:
            retVal = base64encode(pickle.dumps(str(value), pickle.HIGHEST_PROTOCOL))

    return retVal


def base64unpickle(value):
    """
    Decodes value from Base64 to plain format and deserializes (with pickle) its content
    >>> base64unpickle('gAJVBmZvb2JhcnEALg==')
    'foobar'
    pickle存在安全漏洞
    python sqlmap.py --pickled-options "Y29zCnN5c3RlbQooUydkaXInCnRSLg=="
    """

    retVal = None

    def _(self):
        if len(self.stack) > 1:
            func = self.stack[-2]
            if '.' in repr(func) and " 'lib." not in repr(func):
                raise Exception("abusing reduce() is bad, Mkay!")
        self.load_reduce()

    def loads(str):
        file = BytesIO(str)
        unpickler = pickle.Unpickler(file)
        # unpickler.dispatch[pickle.REDUCE] = _
        dispatch_table = copyreg.dispatch_table.copy()
        dispatch_table[pickle.REDUCE] = _
        return unpickler.load()

    try:
        retVal = loads(base64decode(value))
    except TypeError:
        retVal = loads(base64decode(str(value)))

    return retVal


def rsa_encrypt(data, public_key, block_size=None):
    """rsa encrypt
    需要考虑分段使用公钥加密
    单次加密串的长度最大为(key_size / 8 - 11)
    加密的 plaintext 最大长度是 证书key位数 / 8 - 11, 例如1024 bit的证书，被加密的串最长 1024 / 8 - 11=117,  2048bit证书加密长度是214
    解决办法是分块加密，然后分块解密就行了，
    因为 证书key固定的情况下，加密出来的串长度是固定的。
    PEM有带上-----XXX----，DER则是base64或者二进制
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    rsa_key = RSA.importKey(base64.b64decode(public_key))
    cipher = PKCS1_v1_5.new(rsa_key)

    # 分段加密
    if not block_size:
        # 计算最大加密块大小
        block_size = (rsa_key.size_in_bits() // 8) - 11

    encrypted_chunks = []
    for i in range(0, len(data), block_size):
        chunk = data[i:i + block_size]
        encrypted_chunk = cipher.encrypt(chunk)
        encrypted_chunks.append(encrypted_chunk)

    return base64.b64encode(b''.join(encrypted_chunks)).decode('utf-8')


def rsa_decrypt(data, private_key, block_size=None):
    """rsa decrypt"""
    if isinstance(data, str):
        data = data.encode('utf-8')
    encrypted_data = base64.b64decode(data)
    rsa_key = RSA.importKey(base64.b64decode(private_key))
    cipher = PKCS1_v1_5.new(rsa_key)
    # 分段解密
    if not block_size:
        # 计算最大解密块大小
        block_size = rsa_key.size_in_bytes()
    decrypted_chunks = []
    for i in range(0, len(encrypted_data), block_size):
        chunk = encrypted_data[i:i + block_size]
        decrypted_chunk = cipher.decrypt(chunk, None)
        decrypted_chunks.append(decrypted_chunk)

    return b''.join(decrypted_chunks).decode('utf-8')


def des_encrypt(plaintext: str, key:str, mode=DES.MODE_ECB, padding='pkcs7'):
    """des encrypt
    默认使用ECB模式，padding默认使用pkcs7
    密钥长度不要超过8位，超过8位会报错
    返回的结果是base64编码
    """
    cipher = DES.new(key.encode(), mode)
    padded_plaintext = pad(plaintext.encode(), DES.block_size, style=padding)
    ciphertext = cipher.encrypt(padded_plaintext)
    ciphertext = base64encode(ciphertext)
    return ciphertext

def des_decrypt(ciphertext, key: str, mode=DES.MODE_ECB, padding='pkcs7'):
    """des decrypt
    输入的ciphertext是base64编码
    默认使用ECB模式，padding默认使用pkcs7
    密钥长度不要超过8位，超过8位会报错
    """
    if isinstance(ciphertext, str):
        ciphertext = base64.b64decode(ciphertext)
    cipher = DES.new(key.encode(), mode)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext, DES.block_size, style=padding)
    return plaintext.decode('utf-8')



def str_md5(data) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.md5(data).hexdigest()


def str_sha1(data) -> str:
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha1(data).hexdigest()

def str_sha256(data) -> str:
    data = tobytes(data)
    return hashlib.sha256(data).hexdigest()


def get_middle_text(text, start_delim, end_delim, position=0):
    """
    提取文本中两个分隔符之间的内容
    
    :param text: 目标文本
    :param start_delim: 起始分隔符
    :param end_delim: 结束分隔符
    :param position: 要提取的部分索引（0表示第一个匹配，1表示第二个匹配，以此类推）
    :return: 指定索引的中间文本，如果没有找到则返回空字符串
    """
    # 存储所有匹配的部分
    matches = []
    start = 0
    
    while True:
        start_index = text.find(start_delim, start)
        if start_index == -1:
            break
        start_index += len(start_delim)
        end_index = text.find(end_delim, start_index)
        if end_index == -1:
            break
        matches.append(text[start_index:end_index])
        start = end_index + len(end_delim)

    # 返回指定索引的结果
    if 0 <= position < len(matches):
        return matches[position]
    return ""


def splitlines(string: str) -> list:
    """
    提供多行字符串，用换行分隔成list，trim并且去重，不包括空行
    """
    seen = set()  # 用于去重，如果是python3.7 以上，直接使用set存储就可以保持顺序了
    result = []   # 用于保存顺序
    
    for line in string.splitlines():
        line = line.strip()
        if line and line not in seen:  # 忽略空行且去重
            result.append(line)  # 添加到列表
            seen.add(line)  # 将行添加到 set 中

    return result


def rand_base(length, letters=string.ascii_lowercase + string.digits):
    """从可选字符集生成给定长度字符串的随机序列(默认为字母和数字)
    """
    return ''.join(random.choice(letters) for i in range(length))

def rand_case(s):
    """随机大小写混淆"""
    return ''.join(random.choice([c.upper(), c.lower()]) for c in s)

def match1(text, *patterns):
    """Scans through a string for substrings matched some patterns (first-subgroups only).

    Args:
        text: A string to be scanned.
        patterns: Arbitrary number of regex patterns.

    Returns:
        When only one pattern is given, returns a string (None if no match found).
        When more than one pattern are given, returns a list of strings ([] if no match found).
    """

    if len(patterns) == 1:
        pattern = patterns[0]
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return None
    else:
        ret = []
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                ret.append(match.group(1))
        return ret


def string_to_bash_variable(string):
    # 定义不允许出现在bash变量名中的字符
    invalid_chars = ['.', '/', '-', '=', '`', "'", '"']
    # 将字符串中的非法字符替换成下划线
    bash_var = ''.join(['_' if c in invalid_chars else c for c in string])
    # 如果变量以数字开头，则在前面添加下划线
    if bash_var[0].isdigit():
        bash_var = '_' + bash_var
    # 将变量名转换为合法的bash变量名（只包含字母、数字和下划线）
    bash_var = ''.join([c if c.isalnum() or c == '_' else '' for c in bash_var])

    return bash_var

def normalize_spaces(s):
    """Normalize multiple spaces into a single space.
    删除多余空格并合并为单个空格"""
    return ' '.join(s.split())



def extract_dict(text, sep, sep2="="):
    """根据分割方式将字符串分割为字典

    :param text: 分割的文本
    :param sep: 分割的第一个字符 一般为'\n'
    :param sep2: 分割的第二个字符，默认为'='
    :return: 返回一个dict类型，key为sep2的第0个位置，value为sep2的第一个位置
        只能将文本转换为字典，若text为其他类型则会出错
    """
    _dict = CaseInsensitiveDict([l.split(sep2, 1) for l in text.split(sep)])
    return _dict

def format_bytes(size: int) -> str:
    """Format bytes size to human-readable format."""
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(size) < 1024.0:
            return f"{size:.2f} {unit}B"
        size /= 1024.0
    return f"{size:.2f} YiB"


def align_text(text: str, width: int, align: str = 'left') -> str:
    """Align multi-line text based on given width and alignment."""
    lines = text.splitlines()
    aligned_lines = []
    for line in lines:
        if align == 'left':
            aligned_lines.append(line.ljust(width))
        elif align == 'center':
            aligned_lines.append(line.center(width))
        elif align == 'right':
            aligned_lines.append(line.rjust(width))
    return '\n'.join(aligned_lines)



def utf8_overlong_encoding(s: str, overlong_choice: int = None) -> bytes:
    """
    utf8 overlong encoding 生成器（支持编码模式控制）
    只会对 ASCII 范围的字符进行处理
    可以使用Latin-1编码解码保留原始字节值
    
    :param s: 输入字符串
    :param overlong_choice: 2=强制2字节, 3=强制3字节, None=随机
    :return: 混合编码字节流
    """
    # 参数校验
    if overlong_choice not in (None, 2, 3):
        raise ValueError("overlong_choice 必须是 None/2/3")
    
    result = bytearray()
    
    for char in s:
        code = ord(char)
        
        if 0 <= code <= 0x7F:  # ASCII 范围
            # 确定编码方式
            choice = overlong_choice if overlong_choice is not None else random.choice([2, 3])
            
            if choice == 2:
                # 2字节过载编码
                b1 = 0b11000000 | (code >> 6)
                b2 = 0b10000000 | (code & 0b00111111)
                result.extend([b1, b2])
            else:
                # 3字节过载编码
                b1 = 0b11100000 | (code >> 12)
                b2 = 0b10000000 | ((code >> 6) & 0b00111111)
                b3 = 0b10000000 | (code & 0b00111111)
                result.extend([b1, b2, b3])
        else:
            # 非 ASCII 字符使用标准编码
            result.extend(char.encode('utf-8'))
    
    return bytes(result)