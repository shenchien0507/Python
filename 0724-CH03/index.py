# 使用[]運算子讀取單一字元
d= '-'*25
print(d,1,d)
print('使用[]運算子讀取單一字元')

s1 = 'python 基礎必修課'
print(s1[3])
print(s1[-2])
# print(s1[16]) # 無16位字元,會報錯,無法執行後續,故註解不執行

print(d,2,d)
print('使用[]運算子讀取單一字元')

s = 'python 基礎必修課'
print(s[:])
print(s[7:])
print(s[:6])
print(s[5:8])
print(s[9:6:-1])
print(s[::2])
print(s[::-1])
print(s[::-2])




