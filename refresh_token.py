import requests
import json

def refresh_token():
    client_id = "973579601522-aceufaar01sghcau01dbifhoo48dqgk1.apps.googleusercontent.com"
    client_secret = "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"

    refresh_token = "1//0gkJSTcEZ9NVnCgYIARAAGBASNwF-L9IrTfNQiK6LkTWWGE_LF4X1buDHaVeZ8AaSXM4m9MB2JALz4bEuT11fnGiwQFi-Sa2hEZ0"
    access_token = "ya29.a0AWY7CkkdpciYdjmzggx1Q25u3Kbw5XHX5piuIT2Ef2xWXGhuN6z5T3mBs4CzT1jSJ32ykET3pPIlc20E3PfuT7FGZdTNBu0A6-VfKx3HUfbrPw3qyWHDJIiFzW27sK3R7yMf_2d9VSOlBC7wsXadL4Eerl2KaCgYKAa0SARISFQG1tDrp5oldH-b_v44-dNiCZpso1g0163"

    if refresh_token is None and access_token is None:
        return {'error': 'Either refresh_token or access_token must be provided.'}

    url = "https://oauth2.googleapis.com/token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
    }

    if refresh_token is not None:
        params["grant_type"] = "refresh_token"
        params["refresh_token"] = refresh_token
    else:
        params["grant_type"] = "urn:ietf:params:oauth:grant-type:token-exchange"
        params["subject_token_type"] = "urn:ietf:params:oauth:token-type:access_token"
        params["subject_token"] = access_token

    response = requests.post(url, data=params)
    if response.status_code == 200:
        token_data = response.json()
        new_token = token_data.get("id_token", None)
        print(new_token)
        return {'access_token': new_token}
    else:
        print('Token refresh failed')
        return {'error': 'Token refresh failed.'}

refresh_token()
