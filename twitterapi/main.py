import tweepy
import json
import os
base_dir = os.path.dirname(os.path.abspath(__file__))

con = "xFXAM3b49KeBTPsLOFMZ0vFZv"
cons = "dvycE1MyOuVe9s13gouIU8lqFAxyfQEu8asyoJPWHH72xkFCbj"
acc = "3142731804-lw4KbsKyW6iiy76zyfcBCiVbD8BPTQmjHkWq0FJ"
accs = "ijlAgfcxEwGfVK4s135L0J8yssE2m2X6sSyWt01rDOdhm"

auth = tweepy.OAuthHandler(con, cons)
auth.set_access_token(acc, accs)

api = tweepy.API(auth)

class IconSearch(tweepy.StreamListener):
    def on_data(self, data):
        filename = json.loads(data)["text"].split()[0]
        files = os.listdir(base_dir + "/../thumbs/")
        print(filename)
        if "{}.png".format(filename) in files:
            api.update_profile_image(base_dir + "/../thumbs/{}.png".format(filename))
            print("changed")

listener = IconSearch()
stream = tweepy.Stream(auth, listener)
target = ["#test8871", "#ctareIcon"]
print(os.listdir(base_dir + "/../thumbs/"))
print(target)
while True:
    try:
        stream.filter(track=target)
    except KeyboardInterrupt:
        break
    except:
        continue
