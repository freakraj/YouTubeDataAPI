from youtube_statistics import YTstats

API_KEY = "AIzaSyA2ohcW74PFz84ZKU9j5kOgQ6zmObg0leQ"
# channel_id = "UCbXgNpp0jedKWcQiULLbDTA"
channel_id ="UCR6d0EiC3G4WA8-Rqji6a8g"

yt = YTstats(API_KEY,channel_id)
yt.get_channel_statistics()
yt.dump()
# print(data)