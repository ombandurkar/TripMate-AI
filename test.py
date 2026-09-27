from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights, airport_country_matches
from backend import run_travel_agent

# res = tavily_search("Best hotels in India")
# print(res)

# res = search_flights("Flight from Mumbai to Delhi")
# print(res)

res = run_travel_agent("I want to travel from Mumbai to Delhi and stay in a hotel for 3 days.", "test_user")
print(res)