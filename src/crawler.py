import requests

from bs4 import BeautifulSoup

from src.constants import URL_WEB, CONTENT_CLASS


class WODCrawler:

    @staticmethod
    def _get_web_content(day: str) -> str:
        """
        Get the daily WOD from Crossfit Web page

        :param day: day str (format: yymmdd)
        :return: content: return the daily wod information
        """
        # URL format:  'https://www.crossfit.com/210115'
        page = requests.get('{0}/{1}'.format(URL_WEB, day))
        soup = BeautifulSoup(page.content, 'html.parser')

        article_element = soup.find('div', class_=CONTENT_CLASS)
        if article_element is None:
            return ''

        return article_element.get_text()

    @staticmethod
    def _beautify_content(content: str) -> str:
        special_headers = ['beginner option:', 'intermediate option:']
        sentences = content.split('\n')
        parsed_content = []
        for sentence in sentences:
            if len(sentence) > 0 and sentence.casefold() in special_headers:
                parsed_content.append('')
                parsed_content.append('*' * 10)
                parsed_content.append(sentence)
                parsed_content.append('')
                continue

            parsed_content.append(sentence)

        return "\n".join(parsed_content)

    def get_wod(self, formatted_day):
        # 2. get web content
        web_content = WODCrawler._get_web_content(formatted_day)
        if web_content == '':
            return 'No content for this day'

        beautified_content = WODCrawler._beautify_content(web_content)
        message = "{0}\n\n{1}".format(formatted_day, beautified_content)

        return message
