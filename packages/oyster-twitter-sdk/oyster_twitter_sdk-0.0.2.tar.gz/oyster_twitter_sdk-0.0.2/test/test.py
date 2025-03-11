from oyster_twitter_sdk import OysterTwitterSDK

# Initialize the SDK
sdk = OysterTwitterSDK()

# Fetch existing keys and tokens
keys_and_tokens = sdk.fetch_keys_and_tokens()
print(keys_and_tokens)
