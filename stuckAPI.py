from pprint import pprint

import requests


class StackQuestions:
    link_of_api = 'https://api.stackexchange.com/2.3/questions'

    def get_questions(self):
        params = {'order': 'desc', 'sort': 'activity', 'site': 'stackoverflow',
                  'tagged': 'python', 'fromdate': '1673740800', 'todate': '1673913600'}
        response = requests.get(self.link_of_api, params=params)
        pprint(response.json())
        return response.json()


getting_quests = StackQuestions()
result = getting_quests.get_questions()
