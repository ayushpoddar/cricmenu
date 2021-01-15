import requests
import subprocess
import pprint
import rumps
import threading
import re

class CricMenu(rumps.App):

    unreqd_events = ["no run", "1 run", "2 runs", "3 runs"]

    def __init__(self):
        super(CricMenu, self).__init__(name="Live Score")
        self.prev_comms_id = None
        self.title = "No live score"
        self.match_id = "1223872"

    
    @rumps.timer(5)
    def update(self, sender):
        thread = threading.Thread(target=self.getScore)
        thread.start()


    @rumps.clicked("Enter Match URL")
    def changeMatchId(self, sender):
        self.match_id = self.getMatchID()


    def getMatchURL(self):
        command = '''
            osascript -e 'text returned of (display dialog "Match URL from ESPNCricInfo?" buttons {"OK"} default answer "" default button 1)'
            '''
        url = subprocess.check_output(command, shell=True, text=True)
        return url


    def getMatchID(self):
        '''Get the match ID'''
        url = self.getMatchURL()
        return re.findall(r'\d+', url)[-1]

        
    def getScore(self):
        '''Get data from espncricinfo API'''
        if not self.match_id: return
        x = requests.get("https://www.espncricinfo.com/ci/engine/match/" + self.match_id + ".json")
        x = x.json()
        self.recent_ball = x['comms'][0]['ball'][0]
        self.title = re.sub(r'\(.*?\)', '', x['match']['current_summary_abbreviation']).replace("  ", " ")
        del x

if __name__ == "__main__":
    CricMenu().run()


# if "event" in recent_ball:
#     event = recent_ball["event"]
#     comm_id = recent_ball["comms_id"]
#     dismissal = recent_ball["dismissal"]
#     if comm_id != prev_comms_id:
#         prev_comms_id = comm_id
#         if event.lower() not in unreqd_events or len(dismissal) > 0:
#             # Notify
#             pass
