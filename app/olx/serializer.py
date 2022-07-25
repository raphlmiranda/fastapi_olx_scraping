from bs4 import BeautifulSoup
from typing import Dict, Text, List


class Serializer:

    def bs4_serializer(self, obj: BeautifulSoup) -> Dict:
        try:
            ad: List[BeautifulSoup] = obj.find('div', {'class': 'sc-12rk7z2-4 bGMpGA'}).find_all('div')
            ad_description: Text = ad[1].text.strip()
            ad_information: List[BeautifulSoup] = ad[3].find_all('span')

            return {
                'description': ad_description,
                'price': ad[9].text.strip(),
                'rooms': ad_information[0].text.strip(),
                'area': ad_information[2].text.strip(),
                'tax': ad_information[4].text.strip(),
            }
        except Exception as e:
            print(e)
            return {}