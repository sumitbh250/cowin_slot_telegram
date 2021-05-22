import json
import re
import requests
import sys
import time
import urllib
import consts

class Cowin():
  def __init__(self):
    self.init_session()
  def init_session(self):
    url_oc = "https://www.cowin.gov.in/home"
    self._headers = {
        'authority': 'cdn-api.co-vin.in',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'accept': 'application/json, text/plain, */*',
        'dnt': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'origin': 'https://www.cowin.gov.in',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.cowin.gov.in/',
        'accept-language': 'en-US,en;q=0.9',
    }
    self._session = requests.Session()
    request = self._session.get(url_oc, headers=self._headers, timeout=5)
    self._cookies = dict(request.cookies)
  def get_availability(self):
    # district = "143"
    # 143 NorthWest Delhi
    # 364 Akola
    # 322 Ratlam
    # 312 Bhopal
    # 507 Ajmer
    # 345 Shivpuri
    # 141 Central Delhi
    # 149 South Delhi
    # 664 Kanpur
    district = sys.argv[1]
    url = ""
    if int(sys.argv[3]) == 0:
      url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+district+"&date=" + consts.date
    elif int(sys.argv[3]) == 1:
      url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id="+district+"&date=" + consts.date
    elif int(sys.argv[3]) == 2:
      url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode="+district+"&date="+ consts.date
    response = self._session.get(url, headers=self._headers, timeout=5, cookies=self._cookies)
    dajs = response.json()
    return dajs

def send(chat_ids, token, msg):
  """
  Send a mensage to a telegram user specified on chatId
  chat_id must be a number!
  """

  print(msg)
  responses = []
  for chat_id in chat_ids:
    send_text = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=Markdown&text=%s'
    # send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg
    response = requests.get(send_text % (token, chat_id, msg))
    responses.append(response.json())
  return responses

def main():
  c = Cowin()
  prev_names = ""
  cont_errors = 0
  while True:
    try:
      names = ""
      response = c.get_availability()
      for center in response['centers']:
        # print(center)
        for session in center['sessions']:
          if session['min_age_limit'] == int(sys.argv[2]) and session['available_capacity'] > 10:
            # print(center)
            names += center['name'] + " " + session['date'] + " " + \
                     "Available: " + str(session['available_capacity']) + " " + \
                     "Dose1: " + str(session['available_capacity_dose1']) + " " + \
                     "Dose2: " + str(session['available_capacity_dose2']) + " " + \
                     session['vaccine'] + " "+ center['district_name'] + " " + \
                     center['fee_type'] + " " + \
                     "Age:" + str(session['min_age_limit']) + "\n"
      cont_errors = 0
      if names != "" and names != prev_names:
        print(send(consts.message_ids, consts.bot_token, names))
        prev_names = names
        time.sleep(2)
        continue
        # if "GMC" in center['name']:
        #   print(center)
      time.sleep(5)
    except Exception as ex:
      cont_errors += 1
      time.sleep(15)
      print(ex, str(cont_errors))
      # print(response)

if __name__ == "__main__":
  main()
