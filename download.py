from requests import get

import re


class NutcDownloader:

    def __init__(self, sem: str):
        self.sem = sem
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        }

    def get_all_url(self):
        url = 'http://aisap.nutc.edu.tw/public/clsno_list.js'

        response = get(url, verify=False, headers=self.headers)

        pattern = rf'D\d_{self.sem}'
        sem_compile = re.compile(pattern)

        g_Clsno = {}
        text = response.text

        all_clsno = text.split('\n')[1:]
        for clsno in all_clsno:
            if sem_compile.search(clsno):
                exec(clsno)

        result = []
        for i in g_Clsno.values():
            for j in i:
                result.append(j[0])

        return result

    def get_html_text(self, clsno: str):
        url = rf'http://aisap.nutc.edu.tw/public/day/course_list.aspx?sem={self.sem}&clsno={clsno}'

        response = get(url, verify=False, headers=self.headers)

        return response.text
