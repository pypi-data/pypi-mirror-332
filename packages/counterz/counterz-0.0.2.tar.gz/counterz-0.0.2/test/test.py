from counterz import OysterTwitterSDK

# Initialize the SDK
sdk = OysterTwitterSDK()

# # Generate keys and tokens (15-20 minutes operation)
# response = sdk.generate_keys_and_tokens()

# Fetch existing keys and tokens
keys_and_tokens = sdk.fetch_keys_and_tokens()

# # Verify encumbrance
# verification = sdk.verify_encumbrance()