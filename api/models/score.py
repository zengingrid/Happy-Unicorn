class Score:
    # represents a player's score, has 4 private attributes: id, name, score, and time.
    def __init__(self, identifier, name, score, time):
        self._identifier = identifier
        self._name = name
        self._score = score
        self._time = time

    @property
    def name(self):
        # Getter for name
        return self._name

    @property
    def identifier(self):
        # Getter for id
        return self._identifier

    @property
    def score(self):
        # Getter for score
        return self._score
    
    @property
    def time(self):
        return self._time

    def to_json(self):
        # serialization: saves score instance to a json string.
        return {"identifier": self._identifier, "name": self._name, "score": self._score, "time": self._time}

    @classmethod
    def from_json(cls, data):
        # deserialization, creates a score instance.        
        return cls(identifier=data["identifier"], name=data["name"], score=data["score"], time=data["time"])
