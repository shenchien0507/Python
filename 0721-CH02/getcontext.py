# decimal常用函式
import decimal # 匯入decimal模組
d1=decimal.Decimal.from_float(123.4567) # 把(123.4567)float型別變數轉成decimal型別變數
d2=decimal.Decimal.from_float(34.5678) # 把(34.5678)float型別變數轉成decimal型別變數
print(decimal.getcontext()) # 取出目前decimal資料型別運算設定
print(decimal.getcontext().prec) # 顯示decimal，prec設定值
print(decimal.getcontext().rounding) # 顯示decimal，rounding設定值
print(d1+d2) 
decimal.getcontext().prec=8 # 修改prec值為8位數
print(d1+d2) 

# prec值設定位數不包含小數點 ex:prec=8"123.45678/prec=10"12345.06789"
# rounding設定值有:"round_half_even","rount_down","round_up"