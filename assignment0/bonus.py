import csv
list1=['','','','','']
list2=['trade-wars-news1.txt','trade-wars-news2.txt','trade-wars-news3.txt','trade-wars-news4.txt','trade-wars-news5.txt']
for i in range(0,5):
    list1[i]=open(list2[i],'r+',encoding='UTF-8')
    list1[i]=list1[i].read()
    list1[i]=list1[i].strip()
    list1[i]=list1[i].replace('\n','')
    list1[i]=list1[i].replace('“','')
    list1[i]=list1[i].replace('”','')
    list1[i]=list1[i].replace(',','')
    list1[i]=list1[i].replace(':','')
    list1[i]=list1[i].replace('(','')
    list1[i]=list1[i].replace(')','')
    list1[i]=list1[i].replace('？','')
    list1[i]=list1[i].replace('‘','')
    list1[i]=list1[i].replace('[','')
    list1[i]=list1[i].replace(']','')
    list1[i]=list1[i].replace('.','').lower().split()
wordlist=list1[0]+list1[1]+list1[2]+list1[3]+list1[4]
stop_words=['the','and','of','a','in','to','that','is','as','on','with','it','for','has','are','not','have','its','from','would','by','this','at','be','which','an','up','said','also','they','about','but']
countlist={}
for word in wordlist:
    if word in countlist.keys():
        countlist[word]=countlist[word]+1
    else:
        countlist[word]=1
for m in range(0,len(stop_words)):
    if stop_words[m] in countlist.keys():
        countlist.pop(stop_words[m])
sort=sorted(countlist.items(),key=lambda d:d[1],reverse=True)
print(sort[0:16])
with open('bonus.csv','w',newline='',) as f:
    writer=csv.writer(f)
    header=['keyword','frequency']
    writer.writerow(header)
    for i in range(0,len(sort)):
        writer.writerow([sort[i][0],sort[i][1]])
