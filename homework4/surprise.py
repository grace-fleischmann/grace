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
    },
    "Procyon": {
        "RA": "07h 39m 18.1s",
        "Dec": "+05° 13' 29″",
        "Magnitude": .34, 
        "Spectral Type": "F5IV-V"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def star_names(targets): 
    for star in targets: 
        print(star)

def star_name_type(targets):
    for star in targets: 
        spectral_type = targets[star]["Spectral Type"]
        print(star, spectral_type)

def star_mag(targets): 
    for star in targets:
        if targets[star]["Magnitude"] > .1: 
            print(star, targets[star]["Magnitude"])

def brightest_star(targets): 
    closest_star = ""
    max_brightness = 1000
    smallest_dec_diff = 1000
    for star in targets:
        dec_str = targets[star]["Dec"]

        dec_degree = dec_str.split(" ")[0]
        dec_degree = dec_degree.replace("°","")
        dec_degree = dec_degree.replace("+","")
        dec_degree = dec_degree.replace("−", "-")
        dec_degree = int(dec_degree)
        # i got errors such as  dec_diff = abs(int(dec_degree) - 20)
            # ValueError: invalid literal for int() with base 10: '−16'
            #so i am taking out the signs 
        dec_diff = abs(dec_degree - 20)
        mag = targets[star]["Magnitude"]

        if dec_diff < smallest_dec_diff:
            smallest_dec_diff = dec_diff
            max_brightness = mag 
            closest_star = star 
        elif dec_diff == smallest_dec_diff:
            if mag < max_brightness: 
                max_brightness = mag
                closest_star = star 
    print("Best target", closest_star)

brightest_star(targets)