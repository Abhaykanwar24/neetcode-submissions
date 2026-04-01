class TimeMap:

    def __init__(self):
        self.keyStore = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""

        res = ""   
        for t, v in self.keyStore[key]:
            if t <= timestamp:
                res = v  
            else:
                break     
        return res
