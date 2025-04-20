# Dictionary

# my_dict = {
#   "fname":"abc",
#   "lname":"def",
#   "loc":"thane"
# }

# # Looping through a dictionary to get the key

# for ele in my_dict:
#   print(ele)


# # Looping through a dictionary to get the key
# for key in my_dict:
#   print(my_dict[key])


# # to get both key and value
# for key in my_dict:
#   print(f"{key}:{my_dict[key]}")

# Nested list

travel_log = {
  "france":["paris","lille","dijon"],
  "germany":["stuttgart","berlin"]
}

print(travel_log["france"][1])

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

travel_location = {
  "france":{
    "num_times_visited":8,
    "cities_visited":["paris","lille","dijon"]
  },
  "germany":{"cities_visited":["stuttgart","berlin"],
  "total_visits":10}
}
print(travel_location["france"]["cities_visited"][2])
print(travel_location["germany"]["cities_visited"][0])
print(travel_location["germany"]["total_visits"])
