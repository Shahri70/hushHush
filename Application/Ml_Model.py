import pandas as pd
import numpy as np
import os
import time
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator
import multiprocessing
import utilities
animation =[".    ","..   ","...  ",".... ","....."]
idxx = 0
cwd = os.getcwd()
os.chdir(cwd)
os.makedirs('Ml_Data', exist_ok=True)
DataFrame=pd.read_feather("data/stackoverflow.ftr")
print("******"*5,"\nThis Is Data That Fetched from StackOverFlow\n",DataFrame)
DataFrame.dropna(subset=["display_name","reputation","view_count","tags","title"],inplace=True)
DataFrame.dropna(inplace=True)
DataFrame.drop('user_id', axis=1,inplace=True)
#print(DataFrame,"\n")
DataFrame = DataFrame.sort_values(['score','reputation', 'view_count'], ascending=[False,True, False])
#print(DataFrame,"\n")
List_Of_Tags=["reinforcement-learning","reinforcementlearning","machine-learning","tensorflow","scikit-learn","pytorch","deep-learning","python","python-3.x","numpy","sklearn","scikit","Scipy","pandas","svm","knn-clustering","deep-learning","sklearn"]
DataFrame = DataFrame[DataFrame["tags"].apply(lambda x: any(w.lower() in s.lower() for w in List_Of_Tags for s in x))]
DataFrame.reset_index(inplace=True)
#print(DataFrame)
X = DataFrame.iloc[:, [5,3,2]].values
distortion = []
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    distortion.append(kmeans.inertia_)
kn = KneeLocator(range(1, 20), distortion, curve='convex', direction='decreasing')
elbow_point = kn.knee

kmeans = KMeans(n_clusters=elbow_point, init='k-means++', random_state=42)
labels = kmeans.fit_predict(X)
DataFrame['cluster'] = labels
"""
plt.plot(range(1, 20), distortion)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('distortion')
plt.show()
"""
#print(DataFrame)
DataFrame_Clustered={}
for i in range(0,elbow_point):
    cluster_filter = DataFrame['cluster'] == i
    cluster_filter = DataFrame.apply(lambda x: x[cluster_filter].head(30))
    DataFrame_Clustered[i]=cluster_filter
DataFrame = pd.concat(DataFrame_Clustered.values(), axis=0, ignore_index=True)
DataFrame = DataFrame.drop('index', axis=1)
#print(DataFrame)
"""
for i in range(0, len(DataFrame), 9):
    data_DataFrame=[]
    index={}
    idxx+=1
    for j in range(9) :
        percent=format((i+j)/len(DataFrame)*100, ".1f")
        print(f"{percent} %"," Of Data Have Been Collected" +animation[idxx % len(animation)], end="\r")
        if i+j < len(DataFrame):
            name_to_evaluate=DataFrame.loc[i+j,'display_name']
            data_DataFrame.append(name_to_evaluate)
            index[name_to_evaluate]=i+j
    data_to_be_added=check_availabality(data_DataFrame)
    if len(data_to_be_added)!=0:
        #print(data_to_be_added)
        for x in data_to_be_added:
            for k, v in index.items():
                if k.lower()==x["name"].lower():
                    try:
                        DataFrame.loc[v,'Email']=x["email"][0]
                    except:
                        None
                    try:
                        DataFrame.loc[v,'location']=x["location"]
                    except:
                        None
                    try: 
                        DataFrame.loc[v,'followers_git']=x["followers"]
                    except:
                        None
                    try:
                        DataFrame.loc[v,'public_repos_git']=x["public_repos"]
                    except:
                        None
                    try:
                        DataFrame.loc[v,'GitHub_created_at']=x["created_at"]
                    except:
                        None
    time.sleep(10)
print("                                               ",end="\r")
DataFrame.to_feather("Ml_Data/Ml_Data.ftr")  
"""
"""
df = pd.read_feather('Ml_Data/Ml_Data.ftr')
df = df.dropna(subset=['Email'])
df.reset_index(inplace=True)  
df = df.drop('index', axis=1) 
DataFrame_Clustered={}
for i in range(0,elbow_point):
    cluster_filter = df['cluster'] == i
    cluster_filter = df.apply(lambda x: x[cluster_filter].head(3))
    DataFrame_Clustered[i]=cluster_filter
df = pd.concat(DataFrame_Clustered.values(), axis=0, ignore_index=True)
df.reset_index(inplace=True) 
df = df.drop('index', axis=1)
df.to_feather("Ml_Data/final.ftr")  
df=df[df["followers_git"]>50]
print(df)  
candidates=candidate_email()
candidates=[ x for x in candidates if "github.com" not in x ]
print(candidates)
"""
candidates=["shahriarbabaki@yahoo.com"]
utilities.emailing("sending",candidates)
while True:
    utilities.evaluation_answer(candidates)
    utilities.emailing("searching",candidates)
    time.sleep(5) 
    client=utilities.mongo_local()
    db=client.hushHush  
    collection = db.Email
    query1 = {"In_time": True,"solution": True}
    query2 = {"In_time": True,"solution": False}
    query3 = {"In_time": False,"solution": True}
    query4 = {"In_time": False,"solution": False}
    email1 = collection.find(query1)
    email2 = collection.find(query2)
    email3 = collection.find(query3)
    email4 = collection.find(query4)
    for ema in email1:
        utilities.emailing_final(ema["recipient"],"confirmed")
        candidates.remove(ema["recipient"])
        x=ema["recipient"]
        collection.delete_many({"recipient": "x"})
    for ema2 in email2:
        utilities.emailing_final(ema2["recipient"],"failed")
        candidates.remove(ema2["recipient"])
        x=ema2["recipient"]
        collection.delete_many({"recipient": "x"})
    for ema3 in email3:
        utilities.emailing_final(ema3["recipient"],"failed")
        candidates.remove(ema3["recipient"])
        x=ema3["recipient"]
        collection.delete_many({"recipient": "x"})
    for ema4 in email4:
        utilities.emailing_final(ema4["recipient"],"failed")
        candidates.remove(ema4["recipient"])
        x=ema4["recipient"]
        collection.delete_many({"recipient": "x"})
    if len(candidates)==0:
        print("All the candidates have been evaluated, thanks for using our application")
        break
    time.sleep(30)

