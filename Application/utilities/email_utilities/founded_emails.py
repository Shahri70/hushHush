import os
import pandas as pd
def candidate_email():
    cwd = os.getcwd()
    os.chdir(cwd)
    df = pd.read_feather('Ml_Data/final.ftr')
    df=df[df["followers_git"]>50]
    list_of_emails=[]
    for index, row in df.iterrows():
        list_of_emails.append(row["Email"])
    list_of_emails.append("mohamadreza.yazdankhah@gmail.com")
    list_of_emails.append("shahriyarbabaki@gmail.com")
    return list_of_emails  
