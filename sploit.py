import requests
import argparse

API_KEY = "" # Используйте свой api-key
ALFABANK_USER_ID = "" # Используйте свой user_id


def send_finish_game_session(
        master_of: str,
        win_count: int,
        device: str,
        api_key: str = API_KEY,
        alfabank_user_id: str = ALFABANK_USER_ID
) -> tuple:
    url = f"https://tiger.prod.qortex.ru/api/rps/finish-game-session/{alfabank_user_id}/"

    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json",
        "Referer": "https://savemoney.alfabank.ru/",
    }

    payload = {
        "master_of": master_of,
        "win_count": win_count,
        "alfabank_user_id": alfabank_user_id,
        "device": device
    }

    response = requests.post(url, json=payload, headers=headers, timeout=10)
    return response.json(), response.status_code


def send_create_nick(
        nick: str,
        api_key: str = API_KEY,
        alfabank_user_id: str = ALFABANK_USER_ID
) -> tuple:
    url = f"https://tiger.prod.qortex.ru/api/rps/create-nick/{alfabank_user_id}/"

    headers = {
        "Authorization": f"Api-Key {api_key}",
        "Content-Type": "application/json",
        "Referer": "https://savemoney.alfabank.ru/",
    }

    payload = {"nick": nick}

    response = requests.post(url, json=payload, headers=headers, timeout=10)
    return response.json(), response.status_code


def main(num_requests: int = 0, nick: str = None):
    if nick:
        send_create_nick(nick=nick)

    if num_requests > 0:
        for i in range(num_requests):
            send_finish_game_session(
                master_of="rock",
                win_count=5,
                device="iphone"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--num_requests',
        type=int,
        default=0,
    )
    parser.add_argument(
        '--nick',
        type=str,
    )
    args = parser.parse_args()

    main(
        num_requests=args.num_requests,
        nick=args.nick
    )
