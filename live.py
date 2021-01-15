import requests
import pprint

x = requests.get("https://www.espncricinfo.com/ci/engine/match/1223872.json")

x = x.json()

unreqd_keys = ["centre", "description", "innings",
                "live", "live_clipper", "live_video",
                "match_card", "middle_column", "official",
                "other_scores", "score_source", "series",
                "substitute", "team", "tiebreaker",
                "weather"]
unreqd_events = ["no run", "1 run", "2 runs", "3 runs"]

for k in unreqd_keys:
    del x[k]

prev_comms_id = None
recent_ball = x['comms'][0]['ball'][0]
match = x['match']
print(match["current_summary_abbreviation"])
if "event" in recent_ball:
    event = recent_ball["event"]
    comm_id = recent_ball["comms_id"]
    dismissal = recent_ball["dismissal"]
    if comm_id != prev_comms_id:
        prev_comms_id = comm_id
        if event.lower() not in unreqd_events or len(dismissal) > 0:
            # Notify
            pass
