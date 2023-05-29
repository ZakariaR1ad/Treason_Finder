from bs4 import BeautifulSoup
from requests import *

def get_following(github_username, tags_dict):
    r = get(f"https://github.com/{github_username}?tab=following")
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
            if(tag[0].text != None and tag[0].text != ""):
                tags_following.append(tag[0].text)
            else:
                tags_following.append(name[0].text)
            if(tag[0].text in tags_dict.keys()):
                pass
            else:
                tags_dict[tag[0].text] = name[0].text
        except:
            pass
    return tags_following

def get_followers(github_username):
    r = get(f"https://github.com/{github_username}?tab=followers")
    soup = BeautifulSoup(r.content.decode(),"html5lib")
    table = soup.findAll('div',attrs={'class':'d-table table-fixed col-12 width-full py-4 border-bottom color-border-muted'})
    tags, tags_dict = [], {}
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
    return tags,tags_dict