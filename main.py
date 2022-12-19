import json

print ("Hello World 1")

output = {
    "db_password": {
    "value": "notasecurepassword"
  },
  "db_username": {
    "value": "admin"
  }
}

print("My output:")
print (output)

with open("output/qovery-output.json", "w") as outfile:
    json.dump(output, outfile)