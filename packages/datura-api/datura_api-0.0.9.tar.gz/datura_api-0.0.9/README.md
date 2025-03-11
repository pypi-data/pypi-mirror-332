# Datura API

## Introduction

AI-Powered Search Engine and API for Advanced Data Discovery

Datura AI is the driving force behind Desearch, an advanced AI-powered search engine built on Subnet 22. Designed for deep data discovery and intelligent desearch, Desearch helps users extract, analyze, and compile insights from multiple sources with precision and efficiency.

Datura AI is a game-changer for those seeking efficient data analysis and desearch capabilities. It is designed to effortlessly collect and process data from numerous sources.

One of the standout features, Subnet 22, significantly enhances desearch functionality by allowing users to target specific data needs and compile results from multiple sources efficiently. This ensures users save valuable time and effort.

​
## Use Cases

API Key
Learn how to create and manage API keys for authenticating your requests. In order to create the API key, you should have the account.

Sign Up / Log In

Visit Datura Console https://console.datura.ai/ and log in to your account. If you don’t have an account, create one first.

Navigate to API Keys

After logging in to Datura Console, go to the API Keys page.

Generate New Key

Click on the “Generate API Key” button.
Give your key a name for easy identification.
Click on the “Generate” button to create the key.
Copy the key immediately and store it securely. You will not be able to see it again.


from datura_api.datura_api_sdk import DaturaApiSDK

isinstance = DaturaApiSDK(api_key="YOUR_API_KEY")

result = isinstance.basic_twitter_search(
    payload={
        "query": "from:elonmusk #AI since:2025-03-01 until:2025-03-10",
        "sort": "Top",
        "user": "elonmusk",
        "start_date": "2025-03-01",
        "end_date": "2025-03-10",
        "lang": "en",
        "verified": True,
        "blue_verified": False,
        "is_quote": False,
        "is_video": False,
        "is_image": False,
        "min_retweets": 0,
        "min_replies": 0,
        "min_likes": 0,
    }
)

print("result", result)


## Contact

For more information or a demo, contact us at [contact@datura.ai](mailto:contact@datura.ai).
