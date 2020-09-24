class Badge:
    def __init__(self,user,repositorie):
        self.badges=""
        self.user=user 
        self.repositorie=repositorie

    def badge_followers(self):
        twitter="![followers](https://img.shields.io/github/followers/"+self.user+"?style=social )"
        self.badges=self.badges+" "+twitter
 
    def badge_forks(self):
        fork=" ![forks](https://img.shields.io/github/forks/"+self.user+"/"+self.repositorie+"?style=social)"
        self.badges=self.badges+" "+fork
    def badges_contributors(self):
        contributors="![contributors](https://img.shields.io/github/contributors/"+self.user+"/"+self.repositorie+")"
        self.badges=self.badges+" "+contributors
    def badges_lastcommit(self):
        last_commit="![last-commit](https://img.shields.io/github/last-commit/"+self.user+"/"+self.repositorie+")"
        self.badges=self.badges+""+last_commit
    def badges_size(self):
        size="![size](https://img.shields.io/github/repo-size/"+self.user+"/"+self.repositorie+")"
        self.badges=self.badges+" "+size
    def get_badge(self):
        
        return self.badges