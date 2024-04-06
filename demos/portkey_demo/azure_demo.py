import portkey as pk
from portkey import Config,LLMOptions
from getpass import getpass

# Enter the password on the prompt window.
API_KEY = getpass("Enter your PORTKEY_API_KEY ")

# Setting the API key
pk.api_key = API_KEY

# NOTE: For adding custom url, uncomment this line and add your custom url in a selfhosted version.
# pk.base_url = ""
