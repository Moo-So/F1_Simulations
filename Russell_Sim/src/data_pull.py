import fastf1 #using the fastf1 library

fastf1.Cache.enable_cache('data/cache')
#reaching into fastf1 and grabs Cache tool handling saving/loading data locally

session_2023 = fastf1.get_session(2023, 'Singapore', 'R')
session_2023.load()
# Load the 2023 Singapore GP race session
#downlaods/loads real data for that session, (lap times, telemetry, etc)

russell_2023 = session_2023.laps.pick_drivers('RUS')
# Pull Russell's laps specifically (his driver code is RUS)

#print(russell_2023) updated to the one below so more narrowed
print(russell_2023[['LapNumber', 'LapTime', 'Compound']])

last_lap_2023 = russell_2023.iloc[-1] #selects last row position so the final lap
telemetry_2023 = last_lap_2023.get_telemetry() #gets details second by second for the lap

print(telemetry_2023[['X', 'Y', 'Speed']]) #narrow print to x,y,speed so more readable
# Checking how the data behaves right before the repeated placeholder values
#UPDATE: Hypothesis on repeated end values beinf null/placeholder signal if False.
#Checks below disproved it

print(telemetry_2023[['X', 'Y', 'Speed']].tail(30)) #showed all 0s
#print(telemetry_2023[['X', 'Y', 'Speed']].iloc[-60:-25]) #checking motion transiton
#^revealing the window for is quite bigger

#finding the exact transition point programmatically, data cleaning technique
repeat_start = telemetry_2023[telemetry_2023['X']==-13097.0].index[0]
print(f"Repeated data starts at row index: {repeat_start}")

#show transition 15 rows before & 5 after
#confirmed this is the final resting postion
# speed decelerates gradually (96 -> 0 km/h) and X/Y change continuously
# right up to this point, rather than jumping abruptly.
print(telemetry_2023[['X', 'Y', 'Speed']].loc[repeat_start-15:repeat_start+5])

#doing the same for 2025

session_2025 = fastf1.get_session(2025, 'Singapore', 'R')
session_2025.load()
#load 2025 Singapore GP race session (Russell's win)

russell_2025 = session_2025.laps.pick_drivers('RUS')
#pull lap for 2025

#print(russell_2025) updated to below, more narrow
print(russell_2025[['LapNumber', 'LapTime', 'Compound']])

#
fastest_lap_2025 = russell_2025.pick_fastest()
#select fastest lap of race rather than arbitrary one^

telemetry_2025 = fastest_lap_2025.get_telemetry()
#second by second detail of that lap^

print(telemetry_2025[['X', 'Y', 'Speed']])