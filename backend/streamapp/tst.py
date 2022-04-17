if True:

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

        meetingdetails = {"topic": "Stand Up Call",
                        "type": 2,
                        "start_time": "2022-04-14T10: 21: 57",
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
            y = json.loads(r.text)
            join_URL = y["join_url"]
            meetingPassword = y["password"]

            print(
                f'\n here is your zoom meeting link {join_URL} and your \
                password: "{meetingPassword}"\n')
            ss="here is your zoom meeting link "+ str(join_URL) + "and your password: "+str(meetingPassword)
            return ss
        asa=createMeeting()
        print(asa)
         