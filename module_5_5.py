import time


class User:
    def __init__(self, nickname, passw, age):
        self.nickname = nickname
        self.password = hash(passw)
        self.age = age

    def __str__(self):
        return f"{self.nickname}"

    def __eq__(self, other):
        return ((isinstance(other, User) and
                 self.nickname == other.nickname) and
                self.password == hash(other.password))


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return ((isinstance(other, User) and
                 self.title.lower().strip() == other.title.lower().strip()))


class UrTube:
    def __init__(self, ):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname:
                if hash(password) == user.password:
                    self.current_user = user
                    break
                else:
                    print("неверный пароль")
        if not self.current_user:
            print("пользователь не найден")

    def register(self, nickname, password, age):
        exist = False
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                exist = True
                break
        if not exist:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            exist = False
            for saved_video in self.videos:
                if video == saved_video:
                    exist = True
                    break
            if not exist:
                self.videos.append(video)

    def get_videos(self, query):
        lst = []
        for video in self.videos:
            if query.lower() in str(video).lower():
                lst.append(video.title)
        return lst

    def watch_video(self, title: str):
        v = None
        for video in self.videos:

            if title.strip().lower() == str(video).lower().strip():
                v = video
                # print("found: ",v)
                break
        if not v:
            return

        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if v.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        for t in range(v.duration):
            v.time_now = t
            print(t, '', end='')
            time.sleep(1)
        print("Конец видео")
        v.time_now = 0


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')
