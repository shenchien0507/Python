# Scientific Notation（科學記號）
# e 表示 ×10 的幾次方
d = '-' *25
print(d,d)
print('Scientific Notation 科學記號練習')
print(d,d)

print(12.345) # 一般浮點數
print(1.2345e2) # 1.2345 × 10² = 123.45
print(1.2345e8) # 1.2345 × 10⁸ = 123450000.0
print(1.2345e-2) # 1.2345 × 10⁻² = 0.012345

print(d,d)
print('type顯示型態')
print(d,d)

print(type(12.345))
print(type(1.2345e2))
print(type(1.2345e8))
print(type(1.2345e-2))


# 本章記住：
# 只要使用 e，Python 回傳的型態就是 float，所以整數結果也會顯示成 .0。
# e 是 Scientific Notation（科學記號），表示 ×10 的幾次方。
# e 後面是正數，表示乘以 10ⁿ，小數點往右移。
# e 後面是負數，表示乘以 10⁻ⁿ，小數點往左移。

# 一句話記住
# 看到 e，不用先想「×10」，直接想「小數點移動」：e 後面是正數，小數點往右移；e 後面是負數，小數點往左移；位數不夠就補 0
# 只要使用科學記號（e），Python 就會把結果當成 float，因此即使數值是整數，也會顯示成 1000.0，而不是 1000。
# e+n：小數點右移 n 位，不夠補 0。
# e-n：小數點左移 n 位，不夠補 0。
