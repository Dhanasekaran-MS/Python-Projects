travel_log=[
  {"country":"France",
   "cities_visited" : ["Paris","Little","Dijon"],
   "total_visits":12,
  },
   {"country":"Germany" ,
    "cities_visited" :["Berlin","Hamburg","stuttgart"],
    "total_visits":5,
   }
]

def add_new_data(country_name,cities,no_visits):
  new_city={}
  new_city["country"]=country_name
  new_city["cities_visited"]=cities
  new_city["total_visits"]=no_visits
  travel_log.append(new_city)

add_new_data("Russia",["moscow","saint petersburg"],3)
print(travel_log)
  
  
