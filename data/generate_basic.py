import numpy as np
import pandas as pd
import random
rng = np.random.default_rng()
basestats = pd.read_csv('basestats.csv')
av_gpa = basestats['GPA'].iloc[0]


def generate_gpa():
    gpa = rng.normal(av_gpa, 0.2)
    return "{:.02f}".format(gpa)


def get_home_region():
    regions = basestats.columns[1:]
    probs = []
    for region in regions:
        pct = basestats[region].iloc[0]
        probs.append(float(pct.strip('%'))/100)

    return random.choices(regions, weights=probs, k=1)[0]



if __name__ == "__main__":
    print(generate_gpa())
    print(get_home_region())