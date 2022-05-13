import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions

authenticator = IAMAuthenticator('qsFaYrmyeiy4vocDlvgt7XKpvc19zaoK9ss1tAFNnAV_')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.kr-seo.natural-language-understanding.watson.cloud.ibm.com/instances/a84f9ca3-7be7-4dc6-a487-30e558c6b381')


def getSentiment(text):
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(sentiment=SentimentOptions())
    ).get_result()
    print(json.dumps(response, indent=2))
    print(text)
    return response











