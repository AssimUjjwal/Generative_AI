import requests
with open('output.txt', 'r') as f:
    file_contents = f.read()


url = "https://chatgpt-4-bing-ai-chat-api.p.rapidapi.com/chatgpt-4-bing-ai-chat-api/0.2/send-message/"

payload = f"bing_u_cookie=1Mo53xnYzwpA4p1mxCj5fhPQ9TE0xNDI2hHst5hAgQfjB-lc7tlUOI7kPydN1Obp9PfMmPxV2UzdorvIOOb8FPYjHBojpz9uBtM6Q83Vdnkm8J5JXg45fa6g0vTHl8Zvb5oYonhZ7DLbw_A2OCUFf_L-PE5_-VNnQrfkLoiFB2riCJr91YkEb6oarAEd2m5wgccbQ3CV5fvW5hncAPE10tnRo2b1ru96zGw57FrW1nXQ&question=summerize%20this%20information%20in%205%20bullet%20points:{file_contents}"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "b78d7f2d9emsh6878d36873f4c15p1cb84djsn996f8906bfde",
	"X-RapidAPI-Host": "chatgpt-4-bing-ai-chat-api.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)