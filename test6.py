
import requests
import json


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=cNwQffNd9LpDbtahASyTKQYv&client_secret=iUeNj4673qhCl0TJId33LWwRk0iPZbHr"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/text2image/sd_xl?access_token=" + get_access_token()

    payload = json.dumps({
        "prompt": "cat",
        "negative_prompt": "white",
        "size": "1024x1024",
        "steps": 20,
        "n": 2,
        "sampler_index": "DPM++ SDE Karras"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    with open('response.txt', 'w') as f:
        f.write(response.text)
    # print(response.text)



if __name__ == '__main__':
    main()



