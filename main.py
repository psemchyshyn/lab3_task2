'''
Palvo Semchyshyn
22.02.2020
'''


import json
import time
import tweepy as tw


CONSUMER_KEY = 'eG16vH0njymriU5FGdhQiN0qS'
CONSUMER_SECRET = 'Mk2K5whzgmA9SoM4FJ13OZmZOJHgixyuCZsl2eELvnGA67kJa2'
ACCESS_TOKEN = '1230092016085848064-q3niy7e5uD9LBkzmEuOpop5RN3OxpF'
ACESS_TOKEN_SECRET = 'KyMKnE3aKfg4oxXiUnyssjbdWyXRrSOo30WzLRjH9Onup'


AUTH = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)
API_OBJ = tw.API(AUTH, wait_on_rate_limit=True)


def twitter_object_in_json(twit_id="1230961788470079488", path="twitt_in_json.json") -> None:
    """
    (str, str) -> None
    A function for translating Status twitter object into a json object
    and writing it into twitt_in_json.json file
    """
    with open(path, "w", encoding="utf8") as file_to_write:
        json.dump(API_OBJ.get_status(twit_id)._json, file_to_write, indent=4, ensure_ascii=False)


def read_json(path="twitt_in_json.json") -> dict:
    """
    (str) -> dict
    A function for reading a json file.
    The input is a path to file and the output is
    a dictionary
    """
    with open(path, "r", encoding="utf8") as data_file:
        twit_dict = json.load(data_file)
    return twit_dict


def crawling_through_json(twit_dict: dict) -> None:
    """
    A function for recursionaly crawling through dictionary,
    being navigated by user's input
    """
    for key in twit_dict:
        print(key)
    print("_"*30)
    user_key_choice = input("Enter the key you want: ")
    if user_key_choice not in twit_dict:
        print("No such key")
        return
    value = twit_dict.get(user_key_choice)
    print("...")
    time.sleep(1)
    if isinstance(value, dict):
        print(f"The value of the field <{user_key_choice}> is object...")
        while True:
            add_inp = "Type <yes> if you want information on the whole object or <no> otherwise: "
            next_answer = input(add_inp)
            if next_answer == "yes":
                print(f"The value in field <{user_key_choice}> is {value}")
                return
            elif next_answer == "no":
                print(f"Available keys in <{user_key_choice}> : ")
                print("_"*30)
                return crawling_through_json(value)
    else:
        print(f"The value of field <{user_key_choice}> is {value}")


def run() -> None:
    """
    () -> None
    A function for providing user input and running the
    programme
    """
    while True:
        us_input = input("Type tweet id you want to analyze or press ENTER for default output: ")
        if us_input.isdigit() and len(us_input) == 19:
            twitter_object_in_json(us_input)
            break
        elif us_input == "":
            twitter_object_in_json()
            break
    twit_dict = read_json()
    print("\nAvailable keys:\n" + "_"*30)
    crawling_through_json(twit_dict)


if __name__ == "__main__":
    run()
