import requests
import json
import time

url = "https://api.d-id.com/talks"

payload = {
    "script": {
        "type": "text",
        "input": "안녕하세요. 저는 김태권입니다.",
        "provider": {
            "type": "microsoft",
            "voice_id": "ko-KR-BongJinNeural",
            "voice_config": {"style": "cheerful"},
        },
    },
    "source_url":"https://create-images-results.d-id.com/google-oauth2%7C109366194011084691279/upl_GNgtpYmEvl6tkxh1Dqt7U/image.jpeg",
    "config": {"stich": "true"},
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jeF9sb2dpY19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfY3VzdG9tZXJfaWQiOiIiLCJpc3MiOiJodHRwczovL2F1dGguZC1pZC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDg4NjU5MzU1MjIzOTEyMDY0ODAiLCJhdWQiOlsiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTQ1NjQ0OTQsImV4cCI6MTY5NDY1MDg5NCwiYXpwIjoiR3pyTkkxT3JlOUZNM0VlRFJmM20zejNUU3cwSmxSWXEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MifQ.3Z5-OmzeZlqImRLfFjiW0PO7-GqeprIirJiDXCJsboHL85CtTm1WPGe07402KIvqA4fG3szUMSIhr62Q6Tlom6qsbeI2lnpNjb1aEzVJQQQ4nl2qEQ5BUmetYYlRffICdprpvzJst5IJS6RakpJyYcYLkGnE5I5swbbTa8tbsa58TezW01JVsA5aBTd4FK1GvTZLfFLNuDyuVvahan49bcotg7_GVX0GbOtdlpQpQJCwU9z4DIlRLLn8IH9SUtu50LSrcMzMfpLpHkvIEvEpw6QTW4KkHqYkQXLEQqCrWojVwfUS5qWcDEHBvg0pSrH-llPGnbmAVXbuxVdtYhX-ng",
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

# 아이디 결과 처리
res = json.loads(response.text)

id = res["id"]
print("id = ", id)

for i in range(30):
    print(f'변환까지 {i}/30 초 남았습니다.')
    time.sleep(1)



url = "https://api.d-id.com/talks/" + id

result = requests.get(url, headers=headers)

print(result.text)

# 오디오 추출
audio_res = json.loads(result.text)

video_link = audio_res["result_url"]

print("영상경로")
print(video_link)


# response = requests.get(url, headers=headers)

