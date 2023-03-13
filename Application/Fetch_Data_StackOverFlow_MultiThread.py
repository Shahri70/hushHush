import threading
import requests
import pandas as pd
import json
API_KEY = "FOlcyhNNMlh4cZyCHMdVsw(("
list_of_urls = []
for i in range(1, 85):
    url = f'https://api.stackexchange.com/2.2/questions?order=desc&sort=votes&site=stackoverflow&key={API_KEY}&pagesize=100&page={i}'
    list_of_urls.append(url)

spilited_urls = []
for i in range(0, len(list_of_urls), 20):
    spilited_urls.append([list_of_urls[i:i+20]])

ListOfResult = []


def fetch_data_from_stackoverflow(passed_url):

    for item in passed_url:
        result = requests.get(item)
        JSONformatResult = json.dumps(result.json())
        ListOfResult.append(JSONformatResult)


def pass_data_to_dataframe(list_of_result):
    StackOverFlowSelectedFields = []
    for i in range(len(list_of_result)):
        url_result = json.loads(list_of_result[i])
        if "items" in url_result:
            for i in url_result["items"]:
                if "user_id" in i["owner"]:
                    try:
                        selectedfield = {
                            "user_id": i["owner"]["user_id"],
                            "display_name": i["owner"]["display_name"],
                            "reputation": i["owner"]["reputation"],
                            "view_count": i["view_count"],
                            "answer_count": i["answer_count"],
                            "score": i["score"],
                            "tags": i["tags"],
                            "title": i["title"]
                        }
                    except:
                        try:
                            selectedfield = {
                                "user_id": i["owner"]["user_id"],
                                "display_name": "",
                                "reputation": i["owner"]["reputation"],
                                "view_count": i["view_count"],
                                "answer_count": i["answer_count"],
                                "score": i["score"],
                                "tags": i["tags"],
                                "title": i["title"]
                            }
                        except:
                            selectedfield = {
                                "user_id": i["owner"]["user_id"],
                                "display_name": "",
                                "reputation": i["owner"]["reputation"],
                                "view_count": i["view_count"],
                                "answer_count": i["answer_count"],
                                "score": i["score"],
                                "tags": i["tags"],
                                "title":""
                            }

                StackOverFlowSelectedFields.append(selectedfield)

    df = pd.DataFrame(StackOverFlowSelectedFields)
    return df


threadList = []  # t1,t2,t3,t4,t5
for i in range(len(spilited_urls)):
    t = threading.Thread(
        target=fetch_data_from_stackoverflow, args=spilited_urls[i])
    threadList.append(t)
    t.start()

for eachThread in threadList:
    eachThread.join()  # first t1 should join


data=pass_data_to_dataframe(ListOfResult)
data.to_csv("data/stackoverflow.csv")
data.to_feather("data/stackoverflow.ftr")
print(data)
