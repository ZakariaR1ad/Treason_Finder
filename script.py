from requests import *
from bs4 import BeautifulSoup


while(True):
    Name = input("Enter a valid github username > ")

    r = get(f"https://github.com/{Name}")
    if(r.status_code != 200):
        print("User not found ....")
    else:
        break



#Get all the followers

r = get(f"https://github.com/{Name}?tab=followers")
soup = BeautifulSoup(r.content.decode(),"html5lib")
table = soup.findAll('div',attrs={'class':'d-table table-fixed col-12 width-full py-4 border-bottom color-border-muted'})
tags = []
tags_dict = {}
for t in table:
    try:
        name = t.findAll('span',attrs={'class':'f4 Link--primary'})
        if(name[0].text == ""):
            tag = t.findAll('span',attrs={'class':'Link--secondary'})
        else:
            tag = t.findAll('span',attrs={'class':'Link--secondary pl-1'})
        tags.append(tag[0].text)
        if(tag[0].text in tags_dict.keys()):
            pass
        else:
            tags_dict[tag[0].text] = name[0].text
    except:
        pass

#Get all the following

r = get(f"https://github.com/{Name}?tab=following")
soup = BeautifulSoup(r.content.decode(),"html5lib")
table = soup.findAll('div',attrs={'class':'d-table table-fixed col-12 width-full py-4 border-bottom color-border-muted'})
tags_following = []
for t in table:
    try:
        name = t.findAll('span',attrs={'class':'f4 Link--primary'})
        if(name[0].text == ""):
            tag = t.findAll('span',attrs={'class':'Link--secondary'})
        else:
            tag = t.findAll('span',attrs={'class':'Link--secondary pl-1'})
        tags_following.append(tag[0].text)
        if(tag[0].text in tags_dict.keys()):
            pass
        else:
            tags_dict[tag[0].text] = name[0].text
    except:
        pass

F1 = open("ppl_not_following_you_back.txt","w")
F2 = open("ppl_you_are_not_following_back.txt","w")
print(f"you have {len(tags)} follower")
print(f"you are following {len(tags_following)} people")
print("list of people not following you back :")
for i in tags_following:
    if(not i in tags):
        print(tags_dict[i])
        F1.write(i+" "+tags_dict[i]+"\n")
print()
print("list of people you're not following back :")
for i in tags:
    if(not i in tags_following):
        print(tags_dict[i])
        F2.write(i+" "+tags_dict[i]+"\n")

F1.close()
F2.close()
