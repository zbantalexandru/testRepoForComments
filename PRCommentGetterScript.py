import requests

def get_data(api):
        response = requests.get(api)
        if response.status_code == 200:
            print("sucessfully fetched the data")
            print(response.content)
        else:
            print("Acest api a cedat stresului :(")

get_data("https://api.github.com/repos/zbantalexandru/testRepoForComments/pulls/comments");