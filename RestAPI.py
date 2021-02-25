import requests
import base64 

primary_endpoint = "https://yourcompany-api.exigo.com/3.0/"

auth_key = "{}@{}:{}" # There's a handful of ways you're 'supposed' to store these, but everyone just hardcodes them

# However exigo is doing something pretty atypical and not providing an api key, but they give instructions on how to calculate it

login = "Admin"
company = "BusinessLLC"
password = "SuP3rS3kret"

# Exigo's Auth key is is base64Encoded(yourlogin@yourcompany:yourpassword)
auth_key = base64.b64encode( auth_key.format(login,company,password).encode() )

def update_bill(update_packet = None, **kwargs):
    # The API call to update bill probably looks something like this

    headers = {"Authorization" : "Basic " + auth_key}

    # I'm adding a couple of quality of life things that will make this a 
    # little more complicated, but should make the function itself easier to use
    # Things between *** are optional
    # ****************************************************************************
    allowed_fields = [
        "vendorBillID", 
        "customerID" ,
        "customerKey" ,
        "warehouseID" ,
        "currencyCode" ,
        "datePaymentDue", 
        "reference" ,
        "dateReceived", 
        "amount" ,
        "isOtherIncome",
        "notes" ,
        "statusType" ,
        "payableType" ,
        "taxablePeriodTy", 
        "taxablePeriodID" ,
        ]
    

    # This will let you use the funciton in a variety of ways without need to rewrite it for specific cases
    if update_packet is None: update_packet = {}
    if kwargs: update_packet.update(kwargs)

    illegal_keys = list(set(update_packet.keys()) -  set(allowed_fields))
    for key in illegal_keys: del update_packet[key]

    # *****************************************************************************

    # It's not very common to see anything other than GET/POST requests, but it's not difficult to accomodate for either
    # Exigo's update_bill call uses a PATCH request
    r = requests.patch(primary_endpoint+"bill", data=update_packet, headers=headers)

    results = r.json()

    # logic for attempting a retry could go here
    # This may not be a good indicator of success, exigo may send a "Bad Request" upon failure insted
    # I can't test to determine
    return "result" in results.keys()

def create_customer_file(customer_id, file_name, file_path, create_path=False, **kwargs):
    headers = {"Authorization" : "Basic " + auth_key}
    
    packet = {
        "customerID":customer_id,
        "fileName"  : file_name,
    }

    with open(file_path, 'rb') as f:
        packet["fileData"] = f.read()

    if kwargs: packet.update(kwargs)

    r = requests.patch(primary_endpoint+"file", data=packet, headers=headers)

    results = r.json()
    return results
# This is the recommended way of providing an entry point for a python script. If this isn't here, code will run from the top down

if __name__ == "__main__":
    # Update bill function, 3 ways:

    # 1. When you already have the packet you want to send
    # For this example, a 1-level dictionary containing the data need to update can be passed in
    packet = {
        "vendorBillID": 1,
        "customerID": 1,
        "warehouseID": 1,
    }

    update_bill(packet)

    # 2. When you have all of the variable names but they aren't in a dictionary
    # I imagine this is more useful for testing

    update_bill(vendorBillID=1, customerID=1, warehouseID=1)

    # 3. Do both at the same time, because why not?
    
    packet = {
        "vendorBillID": 1,
        "customerID": 1,
    }

    update_bill(packet, warehouseID=1)

    # In any of the use cases, keys that aren't allowed are stripped before being send off to the API
    # This will always work, but won't throw an error in the case of a typo in the field name
    # Food for thought for design choices