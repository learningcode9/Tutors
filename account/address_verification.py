import os

from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_street import Lookup as StreetLookup


def run(addressee,street,city,state,zipcode):
    auth_id = "9a7b8041-9ac4-7e15-75b0-780771fc3d92"
    auth_token = "xMvDBs26P88X0Esk8q5D"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_custom_header({'User-Agent': 'smartystreets (python@0.0.0)', 'Content-Type': 'application/json'}).build_us_street_api_client()
    # client = ClientBuilder(credentials).with_proxy('localhost:8080', 'user', 'password').build_us_street_api_client()
    # Uncomment the line above to try it with a proxy instead

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-street-api#input-fields

    lookup = StreetLookup()
    # lookup.input_id = ""  # Optional ID from your system
    lookup.addressee = addressee
    lookup.street = street
    lookup.street2 = ""
    # lookup.secondary = secondary
    # lookup.urbanization = ""  # Only applies to Puerto Rico addresses
    lookup.city = city
    lookup.state = state
    lookup.zipcode = zipcode
    # # lookup.candidates = 3
    lookup.match = "Invalid"  # "invalid" is the most permissive match,
                              # this will always return at least one result even if the address is invalid.
                              # Refer to the documentation for additional Match Strategy options.

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return

    result = lookup.result
    # print(result[0])
   
    

    if not result:
        print("No candidates. This means the address is not valid.")
        return False
    else:
        print("correct address")
        return True

    # first_candidate = result[0]
    

    # print("Address is valid. (There is at least one candidate)\n")
    # print("ZIP Code: " + first_candidate.components.zipcode)
    # print("County: " + first_candidate.metadata.county_name)
    # print("Latitude: {}".format(first_candidate.metadata.latitude))
    # print("Longitude: {}".format(first_candidate.metadata.longitude))



#if __name__ == "__main__":
#     run()
