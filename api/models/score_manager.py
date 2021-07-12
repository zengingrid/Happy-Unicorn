import json
import os
import random
from datetime import datetime

from .score import Score

class ScoreManager:
    # loads data from a JSON file and saves changes to the same file.
    def __init__(self, filename="scores.json"):
        self._scores = dict()
        self._filename = filename

        if not os.path.exists(filename):
            return None
        
        with open(filename, "r") as fp:
            json_data = json.load(fp)
            
            for obj in json_data:
                score = Score.from_json(obj)
                self._scores[score._identifier] = score


    def get_scores(self):
        # Returns the list of scores
        return self._scores


    def get_score_by_id(self, score_id):
        # get student by score_id
        manager = ScoreManager()
        for key in manager._scores.keys():
            if key == score_id:
                return manager._scores[score_id] 


    def add_score(self, name, score):
        # add new score to scores
        identifier = random.randint(1,1000000)
        time = datetime.now().strftime('%d-%m-%y %H:%M')
        if identifier not in self._scores.keys():
            new_score = Score(identifier, name, score, time)
            self._scores[identifier] = new_score
            return True
        else:
            return False
    

    def remove_score_by_id(self, score_id):
        # remove a score by score_id
        if score_id in self._scores.keys():
            del self._scores[score_id]
            return True
        else:
            return False


    def save(self):
        # save/update the JSON file
        list_of_scores = json.dumps([score.to_json() for score in self._scores.values()])
        with open(self._filename, "w") as fp:
            fp.write(list_of_scores)

