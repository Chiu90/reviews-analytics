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

#篩選的快寫法
good = [d for d in data if 'good' in d ]
第一個d代表append(d)的d,他可以換成其他的東西，如果換成1，就代表如果每個d裡有good就印出一個1
bad = ['bad' in d for d in data]
在每一個d中如果有bad就印出true
bad = []
	for d in data:
		bad.append('bad' in d)


#文字計數
wc = {} #word count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1#
		else:
			wc[word] = 1#左邊去查找有嬤  沒有變成新增


for word in wc: #word是每個key
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	s = input('請問你想查什麼字:')
	if s == 'q':
		break
	if s in wc:
		print(s, '出現過的次數為:', wc[s])
	else:
		print('沒有出現過!')





