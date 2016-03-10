import define

'''This script reads in the file and analyses for names'''

def fileRead():
	i = 0
	off_days = {}
	with open("sample data.txt") as f:
    		content = f.readlines()
		name = ""
		for line in content:
			for word in line.split():
				if word[len(word)-1] == ',':
					word = word[:len(word)-1]
				if word in define.unusable_words:
					break
				if (word not in define.days):
					off_days[word] = []
					name = word
				else:
					off_days[name].append(word)
	if len(off_days.keys()) > 4:
		off_days = cutDict(off_days)
	return(off_days)

def cutDict(dic):
	new_dic = {}
	i = 0
	for key in dic.keys():
		new_dic[key] = dic[key]
		i+=1
		if i==4:
			break
	return new_dic
