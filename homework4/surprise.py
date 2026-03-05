# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

#writing a function that uses a loop to print the name of each star 

def print_name_star(targets): 
    for name in targets: 
        print(name)
    return name
print_name_star(targets) 

#write a function that uses a loop to print the name of each star with its spectral type 
def name_spectral(targets): 
    for name in targets: 
        spectral_type = targets[name]["Spectral Type"]
        print(name, spectral_type)
    return spectral_type
name_spectral(targets)

#write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag 
def magnitude_condition(targets): 
    for name in targets: 
        if targets[name]["Magnitude"] > 0.1: 
            print(name)
    return name 
magnitude_condition(targets)

targets["Antares"] = {
    "RA": "16h 29m 24.4s",
    "Dec": "-26° 25′ 55″",
    "Magnitude": 1.06,
    "Spectral Type": "M1.5 Iab-Ib"
}

print (targets)

def declination_star(targets):
    list_subtraction = {}
    for name in targets:
        first_part = targets[name]["Dec"]
        declination = first_part.split(" ")[0]
        final_degree = (
            declination
            .replace("°","")
            .replace("+", "")
            .replace("−","-")
        )
        integer_degree = int(final_degree)
        subtracting_answer = abs(20-integer_degree) 
        list_subtraction[name] = subtracting_answer
        brightest_star = min(list_subtraction, key=list_subtraction.get)
        minimum_difference = list_subtraction[brightest_star]
    return(brightest_star, minimum_difference)



print(declination_star(targets))






