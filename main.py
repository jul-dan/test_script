import json

print ("Hello World 1")

output = {
    "db_password": {
    "sensitive": True,
    "value": "notasecurepassword"
  },
  "db_username": {
    "sensitive": False,
    "value": "admin"
  }
}

print("My output:")
print (output)

with open("output/qovery-output.json", "w") as outfile:
    json.dump(output, outfile)