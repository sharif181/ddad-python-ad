class Playlist:

    def __init__(self,campaign_id,campaign_title,primary_src,secondary_src,duration,priority):
        self.campaign_id = campaign_id
        self.campaign_title = campaign_title
        self.primary_src = primary_src
        self.secondary_src = secondary_src
        self.duration = duration
        self.priority = priority

    
    def getCamId(self):
        return self.campaign_id
    def getCamTitle(self):
        return self.campaign_title
    def getPrimarySrc(self):
        return self.primary_src
    def getSecondarySrc(self):
        return self.secondary_src
    def getDuration(self):
        return self.duration
    def getPriority(self):
        return self.priority