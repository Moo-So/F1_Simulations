import fastf1 #using the fastf1 library

fastf1.Cache.enable_cache('data/cache')
#reaching into fastf1 and grabs Cache tool handling saving/loading data locally

session_2023 = fastf1.get_session(2023, 'Singapore', 'R')
session_2023.load()
# Load the 2023 Singapore GP race session
#downlaods/loads real data for that session, (lap times, telemetry, etc)

russell_2023 = session_2023.laps.pick_drivers('RUS')
# Pull Russell's laps specifically (his driver code is RUS)

print(russell_2023)

#doing the same for 2025

session_2025 = fastf1.get_session(2025, 'Singapore', 'R')
session_2025.load()
#load 2025 SIngapore GP race session (Russell's win)

russell_2025 = session_2025.laps.pick_drivers('RUS')
#pull lap for 2025

print(russell_2025)