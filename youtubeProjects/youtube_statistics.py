import requests # pip install request 
import json

class YTstats:

    def __init__(self,api_key,channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None

    def get_channel_statistics(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        # print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        # print(data) --> Fetch all data for the json formate for this print ======
        # json data to filter record for fetching just like items to get zero index value and fetching statistic value
        try:
            data = data["items"][0]["statistics"]
        except:
            data=None

        self.channel_statistics = data
        return data

    def dump(self):
        if self.channel_statistics is None:
            return

        channel_title = "Coding Shiksha" # TODO: get channel name from the data 
        channel_title = channel_title.replace(" ","_").lower()
        file_name = channel_title + '.json'
        with open(file_name,'w') as f:
            json.dump(self.channel_statistics, f, indent=4)

        print('file dumped and Mission Success Full')


