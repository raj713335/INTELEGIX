import requests
import json
def Optimal_a(url="en.wikipedia.org/Albert_Einstein"):
    json_data=requests.get("https://xtools.wmflabs.org/api/page/prose/"+url)
    json_data=json_data.json()
    print(json_data)
    unique_references=json_data['unique_references']
    data=json_data['words']
    print(unique_references)
    print(data)

    return(unique_references/data)
# Optimal_A()

def Optimal_b(url=""):
    pass



def main():
    Articles_list=["https://en.wikipedia.org/wiki/2020_United_States_presidential_election",
    "https://en.wikipedia.org/wiki/CNN",
    "https://en.wikipedia.org/wiki/Los_Angeles",
    "https://en.wikipedia.org/wiki/Mexican%E2%80%93American_War",
    "https://en.wikipedia.org/wiki/Texian_Army"]

    A=0
    B=0
    Optimal_A=0
    Optimal_B=0
    for i in range(len(Articles_list)):
        temp_list=str(Articles_list[i][8:]).replace('/wiki',"")

        print(temp_list)
        A+=Optimal_a(temp_list)
        B+=Optimal_B(temp_list)

    Optimal_A=(1/50)*(A)
    print(A)
    print(Optimal_A)

if __name__=="__main__":
    main()