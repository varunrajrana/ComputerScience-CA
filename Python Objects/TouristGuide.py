destinations=["Paris, France","Shanghai, China","Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

attractions = [[] for i in range(len(destinations))]
#print(attractions)

test_traveller=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  return destinations.index(destination)

def get_traveller_location(traveller):
  return get_destination_index(traveller[1]) 

def add_attraction(destination,attraction):
  try:
    destination_index=get_destination_index(destination)
    attractions[destination_index].append(attraction)
    return
  except:
    print("Error here")
    return

add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination,interests):
  attractions_with_interest=[]
  destination_index=get_destination_index(destination)
  attractions_in_city=attractions[destination_index]
  for possible_attraction in attractions_in_city:
    attraction_tags=possible_attraction[1]
    for interest in interests:
      if attraction_tags.count(interest)>0:
        attractions_with_interest.append(possible_attraction[0])
      else:
        continue
  return attractions_with_interest


def get_attractions_for_traveler(traveller):
  traveller_destination=traveller[1]
  traveller_interests=traveller[2]
  traveller_attractions=find_attractions(traveller_destination,traveller_interests)
  interests_string=(f"Hi {traveller[0]}, we think you'll like these places around {traveller_destination}: ")
  for attraction in traveller_attractions:
    interests_string+="the "+attraction
  return interests_string

print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))
