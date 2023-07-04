import requests
import csv

def get_data(api):
        response = requests.get(api)
        if response.status_code == 200:
            file = open('someFile.xlsx', 'w')
            file =  csv.writer(file)
            file.writerow(["CommitHash", "Reporter", "ReviewDate", "Comment"])
            for i in range(len(response.json())):
                CommitHash = response.json()[i]['commit_id']
                Reporter = response.json()[i]['user']['login']
                ReviewDate = response.json()[i]['created_at']
                Comment = response.json()[i]['body']
                file.writerow([CommitHash, Reporter, ReviewDate, Comment])
                #print(response.json()[i]['user']['login'])
                #print(response.json()[i]['body'])
                #print(response.json()[i]['created_at'])
                #print(response.json()[i]['commit_id'])
            print('done')
        else:
            print("The request is down, you should pick it up :(")

get_data("https://api.github.com/repos/zbantalexandru/testRepoForComments/pulls/1/comments");