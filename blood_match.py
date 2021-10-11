import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

r = requests.get(server_name+"get_patients/rj161")
print(r.text)

rid1 = requests.get(server_name+"get_blood_type/M1")
print(rid1.text)

rid2 = requests.get(server_name+"get_blood_type/F6")
print(rid1.text)

blood_match_json = {"Name": "rj161", "Match": "No"}
rpost = requests.post(server_name+"match_check", json=blood_match_json)

print(rpost.text)