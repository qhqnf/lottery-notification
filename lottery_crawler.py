import requests
from bs4 import BeautifulSoup
import re
import json


def winning_price_cralwer():

    url = "https://dhlottery.co.kr/gameInfo.do?method=buyLotto"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")

    winning = soup.find(id="jackpot1st").text
    winning = int(re.sub(",", "", winning))

    return winning


def ifttt_request():

    winning_price = winning_price_cralwer()
    url = "https://maker.ifttt.com/trigger/lottery/with/key/p0sCqzm_P4-g7GLE6NkwwKRiKOJTiN182ajGz7Wd8c-"
    headers = {"Content-Type": "application/json"}
    data = {"value1": winning_price}

    if winning_price > 3000000000:
        requests.post(url, data=json.dumps(data), headers=headers)
    else:
        return


if __name__ == "__main__":
    ifttt_request()