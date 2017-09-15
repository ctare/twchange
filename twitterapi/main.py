import tweepy
import json
import os
base_dir = os.path.dirname(os.path.abspath(__file__))

con = os.environ["CON"]
cons = os.environ["CONS"]
acc = os.environ["ACC"]
accs = os.environ["ACCS"]

auth = tweepy.OAuthHandler(con, cons)
auth.set_access_token(acc, accs)

api = tweepy.API(auth)

dbg = None
class IconSearch(tweepy.StreamListener):
    def on_data(self, data):
        response = json.loads(data)
        # ----
        global dbg
        dbg = response
        # ----
        text = response["text"].split()
        if len(text) == 3:
            if text[:2] == ["get", "list"]:
                api.update_status(status=reply_text,in_reply_to_status_id=status_id)
        filename = text[0]
        files = os.listdir(base_dir + "/../thumbs/")
        print(filename)
        if "{}.png".format(filename) in files:
            api.update_profile_image(base_dir + "/../thumbs/{}.png".format(filename))
            print("changed")

listener = IconSearch()
stream = tweepy.Stream(auth, listener)
target = ["#test8871", "#ctareIcon", "vim"]
print(os.listdir(base_dir + "/../thumbs/"))
print(target)
while True:
    try:
        stream.filter(track=target)
    except KeyboardInterrupt:
        break
    except:
        continue
