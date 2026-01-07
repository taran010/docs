# This is a test file to verify GitHub Advanced Security push protection
# This should trigger secret scanning if properly configured

# Fake Stripe test key (matches pattern but not a real key)
STRIPE_SECRET_KEY = "sk_test_51AbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdefghij"

# This should be detected by GitHub's secret scanning
def process_payment():
    stripe_key = "sk_test_51AbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdefghij"
    print(f"Using Stripe key: {stripe_key}")
