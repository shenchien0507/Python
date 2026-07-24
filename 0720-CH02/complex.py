# Complex numbers(複數)
d = '-' *25
print(d,d)
print("Complex numbers 複數練習")
print(d,d)

c = 3 + 4j # 建立複數：實部（Real Part）+ 虛部（Imaginary Part）部
# 實部(real) = real part 
# 虛部(imag) = imaginary part
print(type(c)) # 查看變數 c 的型態（complex）
print(type(3))  # 查看 3 的型態（int）
print(type(4j))  # 查看 4j 的型態（complex）
print(type(3+4j)) # 查看 3+4j 的型態（complex）
print(type(c.real)) # 查看實部（Real Part）的資料型態（float）
print(type(c.imag)) # 查看虛部（Imaginary Part）的資料型態（float）

print(d,d)

print(c) # 輸出整個複數
print(c.real) # 取得複數的 Real Part（實部）
print(c.imag) # 取得複數的 Imaginary Part（虛部）


# 本章記住：
# Complex Number（複數） 由 Real Part（實部） 和 Imaginary Part（虛部） 組成。
# 複數格式固定為 實部 + 虛部（j）。
# .real 用來取得實部；.imag 用來取得虛部。
# Python 取得的實部、虛部會以 Floating Point（浮點數） 顯示，例如 3.0、4.0。