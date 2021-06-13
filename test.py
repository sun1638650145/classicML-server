import json, requests
from classicML.benchmarks.wrapper_utils import average_timer


@average_timer(repeat=10)
def main():
    data = json.dumps({
      "x": [0, 0],
    })
    headers = {"content-type": "application/json"}
    json_response = requests.post(
        url='http://127.0.0.1:1234/v0/fit/',
        data=data,
        headers=headers
    ).text

    return json_response


print(main())