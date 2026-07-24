# .format()字串格式化輸出
d = '-' *25
print(d,d)
print('.format()字串格式化輸出練習')
print(d,'1',d)

s1 = '電車月票'
s2 = 1280
print('項目:{0} 金額:{1}元'.format(s1, s2))

print(d,'2',d)

str1 = '張三'
num1 = 17
print('我是{name}今年{age}歲'.format(name = str1, age = num1))

print(d,'3',d)

print('{:.2f}'.format(0.666666))
print('{:,}'.format(1000*1000))
print('{:.2%}'.format(0.666666))
print('{:.0f}'.format(0.666666))
print('|{:6}|'.format('字串'))
print('|{:>6}|'.format(1000))
print('|{:<6}|'.format('字串'))
print('{:$^6}'.format(1000))
print('{0}{{}}'.format('顯示'))


