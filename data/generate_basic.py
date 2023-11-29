import numpy as np
rng = np.random.default_rng()

def generate_gpa(av_gpa):
    gpa = rng.normal(av_gpa, 0.2)
    return "{:.02f}".format(gpa)


if __name__ == "__main__":
    print(generate_gpa(3.13))