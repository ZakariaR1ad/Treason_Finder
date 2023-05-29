import streamlit as st
from requests import *
from Utils import *


st.title("Treason Finder")
github_username = st.text_input("Enter a valid github username")



if st.button("Search"):
    st.write("Searching for", github_username)
    r = get(f"https://github.com/{github_username}")
    if(r.status_code != 200):
        st.write("❌ User not found ....")
    else:
        st.write("✅ User found")
        st.write("Getting followers")

        #Get all the followers
        tags, tags_dict = get_followers(github_username)
        
        #Get all the following
        st.write("Getting following")
        tags_following = get_following(github_username, tags_dict)
        F1 = open("ppl_not_following_you_back.txt","w")
        F2 = open("ppl_you_are_not_following_back.txt","w")

        # TODO: check if number is correct
        st.write(f"🔔 you have {len(tags)} follower")
        st.write(f"📌 you are following {len(tags_following)} people")
        
        st.write(f"list of people {github_username} not following you back :")
        header = "<tr><th>Username</th><th>Fullname</th><th>Github link</th></tr>"
        elements = []
        for i in tags_following:
            if(not i in tags):
                # print(tags_dict[i]) # for debugging
                elements.append(f'<tr> <td>{i}</td> <td>{tags_dict[i]}</td> <td><a href="https://github.com/{i}">https://github.com/{i}</a></td> </tr>')
                F1.write(i+" "+tags_dict[i]+"\n")
        st.markdown('<table style="width:100%">'+header+"".join(elements)+"</table>", unsafe_allow_html=True)        
        
        st.markdown("<br/>", unsafe_allow_html=True)

        st.write(f"📌 list of people {github_username} not following back :")
        elements = []
        for i in tags:
            if(not i in tags_following):
                
                # print(tags_dict[i]) # for debugging
                elements.append(f'<tr> <td>{i}</td> <td>{tags_dict[i]}</td> <td><a href="https://github.com/{i}">https://github.com/{i}</a></td> </tr>')
                # st.write(tags_dict[i])
                F2.write(i+" "+tags_dict[i]+"\n")
                # close the files
        # close <ul> 
        st.markdown('<table style="width:100%">'+header+"".join(elements)+"</table>", unsafe_allow_html=True)        

        F1.close()
        F2.close()
    

