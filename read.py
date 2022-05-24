data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有',len(data),'筆資料')

print(data[0])
print('------------')
#算每一個留言的平均字數
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print(sum_len / len(data))

#清單篩選
new = []
for d in data:
 	if len(d) < 100:
 		new.append(d)
print('一共有',len(new),'留言長度小於一百')
print(new[0])

good =[]
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'比留言提到good')