# print函數顯示各種資料練習
print("-"*25,1,"-"*25)
print('Python', 3.8)
print('台北', '台中', '台南', sep=',')
print('高雄', '屏東', sep='\t')
print('價目表:', end='')
money=30
print('陽春麵', money, '元')

print("-"*25,2,"-"*25)

# print轉換字串的型別字元輸出各種常值和變數練習
print('%c%s先生'%('張','無忌'))
wt,price =3, 20.5
print('%s%d斤,共%f元'%('香蕉',wt,wt*price))

print("-"*25,3,"-"*25)

# print設定寬度來格式化輸出各種資料
print('%d'%(12345))
print('%8d'%(12345))
print('%-8d'%(12345))
print('%3d'%(-12345))
print('%c'%('A'))
print('%4c'%('A'))
print('%c'%(65))
print('%s'%('ABCDE'))
print('%8s'%('ABCDE'))
print('%3s'%('ABCDE'))
print('%6.2s'%('ABCDE'))

print("-"*25,4,"-"*25)

# print修飾自原來格式化輸出浮點數資料
print('%f'%12345.67)
print('%f'%-12.345)
print('%.2f'%12.345)
print('%8.2f'%-12.3456)
print('%3.1f'%123.45)
print('%8.0f'%-1234.56)
print('%8.0f'%1234.56)
print('%E'%1234567.89)
print('%e'%123.4)
print('%10.2e'%12345.6)
print('%10.2E'%0.000123456)

print("-"*25,5,"-"*25)

# print修飾字元來格式化各種資料
print('%#x'%12345)
print('%08d'%12345)
print('%-8d'%12345)
print('% d'%12345)

print("-"*25,6,"-"*25)

# print格式字串內使用溢出,並觀察輸出結果
print('1234567890!\a')
print('12345\b67890!')
print('1234567890!\n')
print('123\r4567890!')
print('123\t4567')
print('12\\3\'45\"67')

print("-"*25,7,"-"*25)

# print使用各種引數串列方式顯示
print('汽水2打24瓶')
print('汽水%d打24瓶'%2)
print('%s%d打%d瓶'%('汽水',2,24))
dozen=2
print('%s%d打%d瓶'%('汽水',dozen,dozen*12))

