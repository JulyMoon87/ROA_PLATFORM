from replit import db
db["key"] = "value"
db["key"]
del db["key"]
keys = db.keys()
matches = db.prefix("prefix")
