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
        st.write(f"🔔 you have {len(tags_dict)} follower")
        st.write(f"📌 you are following {len(tags)} people")
        
        st.write(f"list of people {github_username} not following you back :")
        st.markdown('<div class="container">', unsafe_allow_html=True)
        all_items = []
        st.markdown('<ul>', unsafe_allow_html=True)
        for i in tags_following:
            if(not i in tags):
                st.markdown(
                    """
                    <style>
                    .container {
                        display: flex;
                        justify-content: space-between;
                    }
                    
                    .box {
                        flex-basis: 48%;
                        border: 1px solid black;
                    }
                    </style>
                    """
                    , unsafe_allow_html=True
                )
                # print(tags_dict[i]) # for debugging
                all_items.append(f"<li>{tags_dict[i]}</li>")
                # st.write(tags_dict[i])
                F1.write(i+" "+tags_dict[i]+"\n")
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown(f'<div class="box">{"".join(all_items)}</div>', unsafe_allow_html=True)

        # st.markdown('</div>', unsafe_allow_html=True)
        st.write(f"📌 list of people {github_username} not following back :")
        # st.markdown('<div class="container">', unsafe_allow_html=True)
        all_items = []
        #  open <ul>
        st.markdown('<ul>', unsafe_allow_html=True)
        for i in tags:
            if(not i in tags_following):
                st.markdown(
                    """
                    <style>
                    .container {
                        display: flex;
                        justify-content: space-between;
                    }
                    .box {
                        flex-basis: 48%;
                        padding: 10px; 
                        margin-bottom: 10px;
                        border: 1px solid black;
                    }
                    </style>
                    """
                    , unsafe_allow_html=True
                )
                # print(tags_dict[i]) # for debugging
                all_items.append(f"<li>{tags_dict[i]}</li>")

                # st.write(tags_dict[i])
                F2.write(i+" "+tags_dict[i]+"\n")
                # close the files
        # close <ul> 
        st.markdown('</ul>', unsafe_allow_html=True)
        st.markdown(f'<div class="box">{"".join(all_items)}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        F1.close()
        F2.close()
    

