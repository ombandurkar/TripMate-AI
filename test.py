from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights, airport_country_matches

# res = tavily_search("Best hotels in India")
# print(res)

res = search_flights("Flight from Mumbai to Delhi")
print(res)