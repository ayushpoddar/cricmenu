import requests
import subprocess
import rumps
import re
import notification

class CricMenu(rumps.App):

    # unreqd_events = ["no run", "1 run", "2 runs", "3 runs"]
    defaultTitle = "No live score"

    def __init__(self):
        super(CricMenu, self).__init__(name="Live Score")
        self.title = self.defaultTitle
        self.match_id = self.getMatchID()
        self.runs = None
        self.wickets = None

    
    @rumps.timer(10)
    def update(self, sender):
        '''Update score every n seconds'''
        self.getScore()


    @rumps.clicked("Enter Match URL")
    def changeMatchId(self, sender):
        self.match_id = self.getMatchID()


    def getMatchApiUrl(self):
        '''Returns the API URL for the match'''
        return "https://www.espncricinfo.com/ci/engine/match/" + self.match_id + ".json"


    def getMatchURL(self):
        '''Ask user to input Match URL. Returns URL entered'''
        command = '''
            osascript -e 'text returned of (display dialog "Match URL from ESPNCricInfo?" buttons {"OK"} default answer "" default button 1)'
            '''
        url = subprocess.check_output(command, shell=True, text=True)
        return url


    def getMatchID(self):
        '''Get the match ID'''
        url = self.getMatchURL()
        return re.findall(r'\d+', url)[-1]


    def getRunsAndWickets(self):
        '''Returns dict with runs and wickets. Returns None otherwise'''
        if self.title == self.defaultTitle: return
        score = re.findall(r'[0-9/]+', self.title)[0]
        splittedScore = [int(s) for s in score.split("/")]
        return { "runs": splittedScore[0], "wickets": splittedScore[1] }


    def shouldNotifyForParam(self, param):
        '''Returns true if notification should be sent for runs/wickets
           Also sets the runs and wickets attributes'''
        diff = { "runs": 3, "wickets": 0 }
        x = self.getRunsAndWickets()
        if x and param in diff:
            prevRec = self.__getattribute__(param)
            self.__setattr__(param, x[param])
            return prevRec is not None and self.__getattribute__(param) - prevRec > diff[param]


    def conditionallyNotify(self):
        '''Send notification in case of boundary or wicket'''
        if self.shouldNotifyForParam("runs"):
            notification.notify("CricMenu", "Boundary!")
        if self.shouldNotifyForParam("wickets"):
            notification.notify("CricMenu", "Wicket!")


    def setTitle(self, jsonData):
        '''Set title using the json data provided. Returns nothing'''
        self.title = re.sub(r'\(.*?\)', '', jsonData['match']['current_summary_abbreviation']).replace("  ", " ").strip()


    def getScore(self):
        '''Get data from espncricinfo API'''
        data = self.fetchScoreAPI()
        if data:
            self.setTitle(data)
            self.conditionallyNotify()


    def fetchScoreAPI(self):
        '''Get JSON data from API. Returns JSON data or None'''
        if not self.match_id: return None
        try:
            x = requests.get(self.getMatchApiUrl())
            return x.json() if x.ok else None
        except:
            return None


if __name__ == "__main__":
    CricMenu().run()


