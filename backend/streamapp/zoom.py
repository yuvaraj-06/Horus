import jwt
import requests
 
from time import time
import sys
 
import requests
import authlib
import os
import urllib.request 
from pathlib import Path
from typing import Optional, Dict, Union, Any
from authlib.jose import jwt
from requests import Response
import http.client
import json
API_SEC= 'huOp7UmoZULenoebGtD6xTnvJp8OwsHk6gUn'
API_KEY = 'pc4mHiLdQnSb7MKrz3pj7A'

def generateToken():
            api_key = API_KEY
            api_secret = API_SEC
            jwt_token_exp = 518400
            jwt_token_algo = "HS256"


            iat = int(time())

            jwt_payload: Dict[str, Any] = {
                "aud": None,
                "iss": api_key,
                "exp": iat + jwt_token_exp,
                "iat": iat
            }

            header: Dict[str, str] = {"alg": jwt_token_algo}

            jwt_token: bytes = jwt.encode(header, jwt_payload, api_secret)

            return  jwt_token.decode('UTF-8')

meetingdetails = {"topic": "The title of your zoom meeting",
				"type": 2,
				"start_time": "2019-06-14T10: 21: 57",
				"duration": "45",
				"timezone": "Europe/Madrid",
				"agenda": "test",

				"recurrence": {"type": 1,
								"repeat_interval": 1
								},
				"settings": {"host_video": "true",
							"participant_video": "true",
							"join_before_host": "False",
							"mute_upon_entry": "False",
							"watermark": "true",
							"audio": "voip",
							"auto_recording": "cloud"
							}
				}



def createMeeting():
	headers = {'authorization': 'Bearer ' + generateToken(),
			'content-type': 'application/json'}
	r = requests.post(
		f'https://api.zoom.us/v2/users/me/meetings',
		headers=headers, data=json.dumps(meetingdetails))

	print("\n creating zoom meeting ... \n")
	# print(r.text)
	# converting the output into json and extracting the details
	y = json.loads(r.text)
	join_URL = y["join_url"]
	meetingPassword = y["password"]

	print(
		f'\n here is your zoom meeting link {join_URL} and your \
		password: "{meetingPassword}"\n')
createMeeting()
def get_trans():

    API_KEY= 'pc4mHiLdQnSb7MKrz3pj7A'
    API_SECRET= 'huOp7UmoZULenoebGtD6xTnvJp8OwsHk6gUn'
    ASSEMBLY_AI_TOKEN = "10692a818d514b6cbaf0c3b785d542e8"
    class Zoom:
        def __init__(self, api_key: str, api_secret: str):
            self.api_key = api_key
            self.api_secret = api_secret
            self.jwt_token_exp = 518400
            self.jwt_token_algo = "HS256"

        def generate_jwt_token(self) -> bytes:
            iat = int(time())

            jwt_payload: Dict[str, Any] = {
                "aud": None,
                "iss": self.api_key,
                "exp": iat + self.jwt_token_exp,
                "iat": iat
            }

            header: Dict[str, str] = {"alg": self.jwt_token_algo}

            jwt_token: bytes = jwt.encode(header, jwt_payload, self.api_secret)

            return jwt_token

    zoom = Zoom(API_KEY, API_SECRET)
    jwt_token: bytes = zoom.generate_jwt_token()
    jwt_token_str = jwt_token.decode('UTF-8')
    print(jwt_token_str)
    conn = http.client.HTTPSConnection("api.zoom.us")

    headers = { 'authorization': 'Bearer ' + jwt_token_str}

    conn.request("GET", "/v2/users?page_size=30&status=active", headers=headers)

    res = conn.getresponse()
    data = res.read()
    user_dict = json.loads(data.decode("utf-8"))
     
    USER_ID = user_dict['users'][0]['id']

    print(USER_ID)
    conn = http.client.HTTPSConnection("api.zoom.us")

    conn.request(
        'GET', '/v2/users/' + USER_ID +
        '/recordings?trash_type=meeting_recordings&mc=false&page_size=30',
        headers=headers
        )

    res = conn.getresponse()
    data = res.read()
    meeting_dict = json.loads(data.decode("utf-8"))
    print(meeting_dict)
    MEETING_ID = str(meeting_dict['meetings'][0]['id'])

    print(MEETING_ID)
    conn.request(
    "GET", '/v2/meetings/' + MEETING_ID + '/recordings', headers=headers
    )

    res = conn.getresponse()
    data = res.read()

    response_obj = (data.decode("utf-8"))

    print(response_obj)
    meeting_dict = json.loads(response_obj)
    download_url = meeting_dict['recording_files'][0]['download_url']
    print(download_url)
    authorized_url = download_url + "?access_token=" + jwt_token_str
    endpoint = 'https://api.assemblyai.com/v2/transcript'

    json1 = {
        'audio_url': authorized_url
    }

    heads = {
        'authorization': ASSEMBLY_AI_TOKEN,
        'content-type': 'application/json'
    }

    resp = requests.post(endpoint, json=json1, headers=heads)
    print(resp.json())
    status_point = 'https://api.assemblyai.com/v2/transcript/' + resp.json()['id']

    status_header = {'authorization':ASSEMBLY_AI_TOKEN} 

    status_check = requests.get(status_point, headers=status_header)

    print(status_check.json())
    #createMeeting()
    

    while status_check.json()['status'] in ['queued', 'processing']:
        status_check = requests.get(status_point, headers=status_header)
        time.sleep(5)
        continue

    print(status_check.json()['status'])
    print('\n', status_check.json()['text'])
    print('\n', status_check.json())
get_trans()