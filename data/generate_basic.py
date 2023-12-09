import numpy as np
import pandas as pd
import random
import os
rng = np.random.default_rng()
cwd = os.getcwd()
basestats = pd.read_csv(cwd+'/../data/basestats.csv')
citiesbyregion = pd.read_csv(cwd+'/../data/citiesbyregion.csv', thousands=',')
av_gpa = basestats['GPA'].iloc[0]
spanish_fluent = basestats['SpanishFluent'].iloc[0]

def generate_gpa():
    gpa = rng.normal(av_gpa, 0.2)
    return "{:.02f}".format(gpa)

def get_spanish_fluent():
    return random.choices([True, False], [spanish_fluent, 1-spanish_fluent], k=1)[0]

def get_home_region():
    regions = basestats.columns[2:]
    probs = []
    for region in regions:
        pct = basestats[region].iloc[0]
        probs.append(float(pct.strip('%'))/100)

    return random.choices(regions, weights=probs, k=1)[0]

def get_home_city(region):
    citiesDf = citiesbyregion[citiesbyregion['Region'] == region]
    popsum = citiesDf['Pop'].sum()
    pcts = (citiesDf['Pop']/popsum).tolist()
    return random.choices(citiesDf['City'].tolist(), pcts, k=1)[0]
    

def get_area_code(city):
    return citiesbyregion[citiesbyregion['City'] == city]['Area Code'].iloc[0]

def get_years(year):
    start = 2024 - year
    end = start + 4 if year < 5 else start+5
    return ('September ' + str(start), 'June ' + str(end))

if __name__ == "__main__":
    print(generate_gpa())
    region = get_home_region()
    print(region)
    city = get_home_city(region)
    print(city)
    print(get_area_code(city))
    print(get_years())