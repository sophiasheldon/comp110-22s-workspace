"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary 
schools: dict[str, int] 


# initialize to an empty dictionary 
schools = dict() 

# set a key-value pairing in the dictionary 
schools["UNC"] = 19_400 
schools["Duke"] = 6_717 
schools["NCSU"] = 26_150 

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary 
# by its key.
schools.pop("Duke")

# test for existence of a key
if "Duke" in schools: 
    print("Found the key 'Duke' in schools")
else: 
    print("No key 'Duke' in schools")

# update/reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200 

print(schools)

# Demonstration of dictionary literal 

# Example dictionary literal 
schools = {}  # same as dict()
print(schools)

# alternatively, initialize key-value pairs 
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")