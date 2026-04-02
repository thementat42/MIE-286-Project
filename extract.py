import json
import os


def get_score(test):
    total = len(test)
    mark = 0
    for question in test:
        if question["correct"] == True:
            mark += 1
    return mark/total

def get_avg_time(test):
    total_time = 0
    for question in test:
        total_time += question["time_taken"]
    
    return total_time/20


if __name__ == "__main__":

    DATA_PATH = "data/gain_data"

    gains = []
    gain_baselines = []

    gains_scores = []
    baseline_scores = []
    gains_times = []
    baseline_times = []

    for file in os.listdir(DATA_PATH):
        if "gain" in file:
            # print(file)
            with open(os.path.join(DATA_PATH, file)) as f:
                gains.append(json.load(f))
                # print(files)

    for file in os.listdir(DATA_PATH):
        if "baseline" in file:
            # print(file)
            with open(os.path.join(DATA_PATH, file)) as f:
                gain_baselines.append(json.load(f))
                # print(files)

    # print(gains[0][0]["problem"])
    # print(gain_baselines[0])
    # print(gains[0])
    print(get_score(gains[15]))

    for testg in gains:
        gains_scores.append(get_score(testg))
    for testg_time in gains:
        gains_times.append(get_avg_time(testg_time))

    for testb in gain_baselines:
        baseline_scores.append(get_score(testb))
    for testb_time in gain_baselines:
        baseline_times.append(get_avg_time(testb_time))

    print(gains_scores)
    print(gains_times)
    print(baseline_scores)
    print(baseline_times)
