# 指定變數值
x=5 # 指定x變數值為常值5
y=x # 指定y變數值為變數x的值
print(id(x), id(y)) # 顯示變數x,y的記憶體位置
x=3+y # 指定x變數值為運算是3+y的結果
print(id(x)) # 顯示變數x的記憶體位
a,b=2,3 # 指定a,b變數值為常值2,3
print(id(a),(id(b)))
a,b=b,a # a,b變數值交換
print(id(a),id(b))