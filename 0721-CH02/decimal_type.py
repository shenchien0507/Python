# decimal處理浮點數，提高準確
import decimal # 匯入decimal模組
f1,f2=10.0,3.0 # 宣告f1,f2變數並指定變數值為浮點數10.0和3.0
d1=decimal.Decimal(10) # 使用decimal()方法宣告d1為decimal型別，值為10
d2=decimal.Decimal('3.0')
print(type(d1)) # 顯示d1變數的類別
print(f1/f2) # 顯示f1除以f2的值
print(d1/d2) # 顯示d1除以d2的值
d3=decimal.Decimal('2.345') #宣告d3為decimal型別變數，值為字串常值'2.345'
d4=decimal.Decimal('6.78')
print(d3+d4) # 有效位數為三位
print(d3*d4) # 有效位數為五位(3+2)

# +/- 取小數點後位數最多位為最多有效位數
# * 取小數點後位數相+為最多有效位數