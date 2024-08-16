from packages import YoutubeAuthorization
from packages import YoutubeActions


def test():
    pass


def main():
    profiles_directory = r'C:\work\activity_project\youtube_comments\profiles'
    profile_directory = r'C:\work\activity_project\youtube_comments\profiles\i.am.tequila1236@gmail.com'
    link_to_video = 'https://www.youtube.com/watch?v=L6kWCS6TKGs&ab_channel=IT-%D1%81%D0%BF%D0%B5%D1%86.%D0%94%D0%B5%D0%BD%D0%B8%D1%81%D0%9A%D1%83%D1%80%D0%B5%D1%86'
    comment = 'ну я бы этот топ вопросов еще расширил бы)'

    yt_auth = YoutubeAuthorization(login='i.am.tequila1236@gmail.com',
                                   password='ne_FF_ex07641',
                                   profiles_directory=profiles_directory)

    yt_actions = YoutubeActions(profile_directory=profile_directory)

    # yt_auth.auth()
    yt_actions.send_a_comment(link_to_video, comment)


if __name__ == '__main__':
    main()
