# 浮點數資料，float函式
f, i =1.2345, 12345 
print(type(f)) # 顯示浮點數變值f的類別
f2=float(i) # 用float函式將整束變數i轉成浮點數
print(f2)# 顯示f2的變數值
print(float.is_integer(f)) # 用is_integer()檢查變數(f)是否為整數
print(float.is_integer(f2)) # 用is_integer()檢查變數(f2)是否為整數
# is_integer是檢查一個浮點數數值是否等於整數(即小數點後是否全為0)
print(isinstance(f2, int))
# isinstance資料型態是否為整數
print(round(f,2)) # 用round()函式將變數f四捨五入到小數二位
print(round(f)) # 用round()函式將變數f四捨五入到整數