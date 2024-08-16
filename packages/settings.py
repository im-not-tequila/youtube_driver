import os


directory = "./profiles"


if not os.path.exists(directory):
    os.makedirs(directory)


class Settings:
    PROFILES_DIRECTORY = 'C:/work/activity_project/youtube_driver/profiles'
