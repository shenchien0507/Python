# 邏輯運算子的練習
print((1 < 2) and ('A' == 'a'))
# 1<2 為 True，'A'=='a' 為 False (Python 英文字母大小寫不同)
# True and False → False
print((-1 < 0) or (-1 > 100))
# -1<0 為 True，-1>100 為 False
# True or False → True
print(not('A' != 'a'))
# != 是不等於意思
# 'A'!='a' 為 True (大小寫不同)
# not True → False
print(not 2)
# python只有0會視為Flase,其餘數字都是為True
# 數字 2 視為 True
# not True → False
print(2 and 3)
# 2 和 3 都是真值(True)
# and 會回傳最後一個值 → 3
print(2 or 3)
# 2 為 True
# or 找到第一個 True 就回傳 → 2
print('a' or 'b')
# 'a' 為非空字串(True)
# or 回傳第一個 True → 'a'
print(0 and 3)
# 0 為 False
# and 遇到第一個 False 就回傳 → 0
print('' or 'b')
# '' 空字串為 False
# or 繼續找下一個 True → 'b'

# 回傳值規則

# and規則
# 初學者口訣:找 False，沒有就回最後一個。
# 遇到第一個 False 就回傳它；如果全部都是真值，就回傳最後一個值
# and 想成「全部都要成立」
# 所以它一直找 False，找到就停止。

# or規則
# 初學者口訣:找 True，找到就回第一個，沒有就回最後一個。
# 遇到第一個 True 就回傳它；如果全部都是假值，就回傳最後一個值。
# or 想成「有一個成立就好」
# 所以它一直找 True，找到就停止。