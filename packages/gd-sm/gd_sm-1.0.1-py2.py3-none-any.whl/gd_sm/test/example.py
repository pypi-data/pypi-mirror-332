from gd_sm import *

# sm2使用示例
s2 = sm2.SM2()  # 示例化一个sm2对象
print(f"实例化一个sm2对象，私钥:{s2.private_key}, 公钥:{s2.public_key}")  # 打印对象的公私钥
data = "C27AA65FCA082F8959D8B0F71764B6C5CA02C0AAD27C0CF6B393E61136B82EA9"  # 待处理的数据,16进制字符串格式
sign_data = s2.sign(data)  # 使用私钥签名
valid_sign = s2.verify(data, sign_data)  # 公钥验签
assert valid_sign is True
enc_data = s2.encrypt(data)  # 公钥加密
dec_data = s2.decrypt(enc_data)  # 私钥解密
assert dec_data.lower() == data.lower()

# sm3使用示例
data = "C27AA65FCA082F8959D8B0F71764B6C5CA02C0AAD27C0CF6B393E61136B82EA9"  # 待处理的数据,16进制字符串格式
data_hash = sm3.sm3_hash(data)
valid_hash = sm3.check_sm3(data, data_hash)
assert valid_hash is True

# sm4使用示例
data = "C27AA65FCA082F8959D8B0F71764B6C5CA02C0AAD27C0CF6B393E61136B82EA9"  # 待处理的数据,16进制字符串格式
key = "000102030405060708090A0b0c0d0e0f"
iv = "00000101020203030404050506060707"
enc_data = sm4.encrypt(key, data)  # 默认ecb模式，pkcs7 padding
dec_data = sm4.decrypt(key, enc_data)
assert dec_data.lower() == data.lower()
enc_data = sm4.encrypt(key, data, mode="cbc", iv=iv)  # cbc模式，pkcs7 padding
dec_data = sm4.decrypt(key, enc_data, mode="cbc", iv=iv)
assert dec_data.lower() == data.lower()
