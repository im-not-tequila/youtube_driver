import os


directory = "./profiles"


if not os.path.exists(directory):
    os.makedirs(directory)


class Settings:
    PROFILES_DIRECTORY = './profiles'
