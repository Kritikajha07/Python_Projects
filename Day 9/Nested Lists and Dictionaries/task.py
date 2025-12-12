# capitals={
#     "India": "Delhi",
#     "Pakistan":"Karachi"
# }
# travel_log={
#     "India":["Gujarat","Delhi","Kerela"],
#     "Pakistan":["Karachi","Lahore","Rawalpindi"]
# }
# # print(travel_log["India"])
# # print(travel_log)
# # for key in travel_log:
#     # print(key)
# # print(travel_log["India"][1])
#     # print(capitals[key])
# nested_list=["a","b",["c","d"]]
# print(nested_list[2])

travel_log={
    "India":{
        "cities_visited":["Gujarat","Delhi","Kerela"],
        "total_visits":18
    },

    "Pakistan":{
        "cities_visited":["Karachi","Lahore","Rawalpindi"],
        "total_visits":15
    }
}
print(travel_log["Pakistan"]["cities_visited"][2])

