import os
import requests

with open('resume_summery.txt', 'r') as f:
    file_contents = f.read()
    line = file_contents.split('\n')



# bearer_token = os.environ["REPHRASE_API_KEY"]
bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTM2MjMyNjQ5NzU5OTY3MTg5OTgiLCJhdWQiOlsiaHR0cHM6Ly9kaXkucmVwaHJhc2UuYWkvYXV0aDAiLCJodHRwczovL3JlcGhyYXNlYWktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc5NzUwMTQ0LCJleHAiOjE2Nzk4MzY1NDQsImF6cCI6IjNLVTVqdkVxV0pCQ1VLblBYMjZvbmFTUHkzakozMEo0Iiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSByZWFkOnJlcGhyYXNlLmFpIGFsbDpkaXkgcmVhZDpyZXBocmFzZS5haSJ9.inIMbEdTFaV1uF4dp418E7lVGvS1rLNyVIHdHbB250B5BdnyB8aE8lI2-F2zOCSJXjn8Y61jdhnYxql0Scc3F7U2gU4DDkXwrCvLhCXWRJ5x_dCBvyMwVlfWkma52wzRp4qyhmRX-Z2ZcIDhOPnnHCsMjn1qf0BZ7hwY49ZBBzICxWYbRIqAn1DBnfwvk7_-nucdkt28njrb-bZvg0tSomVye289hutqeb8VCxf0wwfNVgoW_aa9CxLas1t2WIutmyhqTjFFI7itqi8CCctyXs4QNtaemVNXsSLc-Sg8zlzLwjapNhNhLRgFxtn9glfwqIPq6cp2mfEI3ptBdRXkmw"

url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

payload = {
    "videoDimension": {"height": 1080, "width": 1920},
    "scenes": [
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://www.iitbhu.ac.in/contents/iitbhu/img/slider/iit_bhu_slider_03.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": f"<speak>{line[0]}</speak>",
                            "transcript_type": "ssml_limited",
                        },
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://www.iitbhu.ac.in/contents/iitbhu/img/slider/iit_bhu_slider_03.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": f"<speak>{line[1]}</speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://www.iitbhu.ac.in/contents/iitbhu/img/slider/iit_bhu_slider_03.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": f"<speak>{line[2]}</speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://www.iitbhu.ac.in/contents/iitbhu/img/slider/iit_bhu_slider_03.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": f"<speak>{line[3]}</speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
    ],
    "title": "Into to MJ",
    "thumbnailUrl": "https://blog.siriusxm.com/wp-content/uploads/2022/11/MichaelJacksonChannel-1117.jpg",
}
headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
    "content-type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(f"CAMPAIGN_ID= {response.text}")