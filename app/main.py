from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


TEAM_NAMES = {"1": "nodegpt", "2": "bitwise",
              "3": "gituardo", "4": "sickfault",
              "5": "debug-divas", "6": "codex"}
#MICROSERVICE_LINK = "http://17313-teachers2.s3d.cmu.edu:8080/section_info/"

TEAM_MENTORS = {"1": "Seckhen", "2": "Aadi",
              "3": "Steve", "4": "Seckhen",
              "5": "Aadi", "6": "Steve"}

@app.get("/team_name/{team_id}")
def get_team_name(team_id: str):

    if team_id is None:
        raise HTTPException(status_code=404, detail="Missing team id")

    team_id = team_id.lower()


    # TODO Fix this to return correct values for correct team ids.
    if team_id in TEAM_NAMES:
        return {
            "team_name": TEAM_NAMES[team_id]
        }
    else:
        raise HTTPException(status_code=404, detail="Invalid team id")
