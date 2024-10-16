import requests
from .headers import headers
from .utils import log, mrh, log_error

def get_token(data, proxies=None):
    url = "https://major.bot/api/auth/tg/"
    payload = {"init_data": data}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        response.raise_for_status()
        data = response.json()

        if "access_token" in data:
            return data["access_token"]
        else:
            log(mrh + "Token not found in response data.")
            return None
    except requests.exceptions.RequestException as e:
        log(mrh + f"Request failed: check last.log for detail.")
        log_error(f"{e}")
        return None
    except ValueError as e:
        log(mrh + f"JSON decoding failed: check last.log for detail.")
        log_error(f"{e}")
        return None
