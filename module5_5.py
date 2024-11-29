class User:
    def __init__(self, nickname, passw, age):
        self.nickname = nickname
        self.password = passw
        self.age = age


class Video:
    def __init__(self,title,duration,adult_mode = False):
        self.title= title
        self.duration  = duration
        self.adult_mode = adult_mode
        self.time_now = 0

class UrTube:
    def __init__(self,):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self,nickname,password):
        for user in self.users:
            if nickname == user.nickname:
                if password == user.password:
                    self.current_user = user
                    break
                else:
                    print("wrong pass")
        if not self.current_user:
            print("user not found")
    def register(self,nickname, password, age):
        exist = False
        for user in self.users:
            if nickname == user.nickname:
                print(f"user{nickname} already exists")
                exist = True
                break
        if not exist:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
    def log_out(self):
        self.current_user=None

    def add(self,*videos):
        for video in videos:
            exist = False
            for saved_video in self.videos:
                if video.title == saved_video.title:
                    exist = True
                    break
            if not exist:
                self.videos.append(video)

    def get_videos(self,query):
        lst = []
        for video in self.videos:
            if query.lower() in video.title.lower():
                lst.append(video)
        return lst



