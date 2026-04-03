import json
import os
from typing import Literal

DATA_PATH = "data"

def get_data(feedback_type: Literal["gain"]|Literal["loss"]):
    path = os.path.join(DATA_PATH, feedback_type + "_data")
    for file in os.listdir(path):
        if feedback_type not in file:
            continue
        name = file.split("_")[0]
        baseline = name + "_baseline.json"
        with open(os.path.join(path, file)) as f:
            feedback_data = json.load(f)
        with open(os.path.join(path, baseline)) as f:
            baseline_data = json.load(f)
        yield baseline_data, feedback_data

def process(feedback_type: Literal["gain"]|Literal["loss"]):
    data = list(get_data(feedback_type))
    baseline_scores: list[float] = []
    baseline_times: list[float] = []
    feedback_scores: list[float] = []
    feedback_times: list[float] = []

    for participant in data:
        baseline, feedback = participant
        baseline_score = sum(problem['correct'] for problem in baseline)/len(baseline)
        baseline_time = sum(problem['time_taken'] for problem in baseline)/len(baseline)

        feedback_score = sum(problem['correct'] for problem in feedback)/len(feedback)
        feedback_time = sum(problem['time_taken'] for problem in feedback)/len(feedback)

        baseline_scores.append(baseline_score)
        baseline_times.append(baseline_time)
       
        feedback_scores.append(feedback_score)
        feedback_times.append(feedback_time)


        #print( f"{name}:\nBaseline: {baseline_score}, {baseline_time}\n{feedback_type}: {feedback_score}, {feedback_time}",end = "\n"+ "-"*50+"\n")
    
    return baseline_scores, baseline_times, feedback_scores, feedback_times

def write_file(filename: str):
    gain_baseline_scores, gain_baseline_times, gain_feedback_scores, gain_feedback_times = process("gain")
    loss_baseline_scores, loss_baseline_times, loss_feedback_scores, loss_feedback_times = process("loss")

    assert len(gain_baseline_scores) == len(gain_baseline_times) == len(gain_feedback_scores) == len(gain_feedback_times)
    assert len(loss_baseline_scores) == len(loss_baseline_times) == len(loss_feedback_scores) == len(loss_feedback_times)

    result = {
        "gain_baseline_accuracy": gain_baseline_scores,
        "gain_baseline_response_time": gain_baseline_times,
        "gain_feedback_accuracy": gain_feedback_scores,
        "gain_feedback_response_time": gain_feedback_times,
        
        "loss_baseline_accuracy": loss_baseline_scores,
        "loss_baseline_response_time": loss_baseline_times,
        "loss_feedback_accuracy": loss_feedback_scores,
        "loss_feedback_response_time": loss_feedback_times,
    }

    with open(filename, 'w') as f:
        json.dump(result, f)

write_file("x.test.json")