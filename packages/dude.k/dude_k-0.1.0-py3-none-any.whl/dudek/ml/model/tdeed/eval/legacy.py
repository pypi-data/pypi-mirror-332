"""
File containing main evaluation functions
"""

import random

# Standard imports
import numpy as np
import os
import zipfile
import json

from SoccerNet.Evaluation.utils import EVENT_DICTIONARY_BALL, LoadJsonFromZip
from SoccerNet.utils import getListGames

from dudek.data.team_bas import BASLabel
from dudek.ml.data.tdeed import TdeedVideoClip

# Local imports

# Constants
FPS_SN = 25


"""
File containing auxiliar score functions
"""

# Standard imports
from SoccerNet.Evaluation.ActionSpotting import average_mAP
import numpy as np


def compute_amAP(
    targets_numpy,
    detections_numpy,
    closests_numpy,
    framerate=25,
    metric="tight",
    event_team=False,
):

    if metric == "loose":
        deltas = np.arange(12) * 5 + 5
    elif metric == "tight":
        deltas = np.arange(5) * 1 + 1
    elif metric == "at1":
        deltas = np.array([1])  # np.arange(1)*1 + 1
    elif metric == "at2":
        deltas = np.array([2])
    elif metric == "at3":
        deltas = np.array([3])
    elif metric == "at4":
        deltas = np.array([4])
    elif metric == "at5":
        deltas = np.array([5])

    if event_team:
        ntargets = np.zeros(targets_numpy[0].shape[1])
        for i in range(len(targets_numpy)):
            ntargets += targets_numpy[i].sum(axis=0)

    (
        mAP,
        mAP_per_class,
        mAP_visible,
        mAP_per_class_visible,
        mAP_unshown,
        mAP_per_class_unshown,
    ) = average_mAP(
        targets_numpy,
        detections_numpy,
        closests_numpy,
        framerate=framerate,
        deltas=deltas,
    )

    if event_team:
        mAP_per_class = mAP_per_class * ntargets
        mAP_per_class = [
            (mAP_per_class[i * 2] + mAP_per_class[(i * 2) + 1])
            / (ntargets[i * 2] + ntargets[i * 2 + 1])
            for i in range(len(mAP_per_class) // 2)
        ]
        mAP = np.mean(mAP_per_class)

        mAP_per_class_visible = mAP_per_class_visible * ntargets
        mAP_per_class_visible = [
            (mAP_per_class_visible[i * 2] + mAP_per_class_visible[(i * 2) + 1])
            / (ntargets[i * 2] + ntargets[i * 2 + 1])
            for i in range(len(mAP_per_class_visible) // 2)
        ]
        mAP_visible = np.mean(mAP_per_class_visible)

        mAP_per_class_unshown = mAP_per_class_unshown * ntargets
        mAP_per_class_unshown = [
            (mAP_per_class_unshown[i * 2] + mAP_per_class_unshown[(i * 2) + 1])
            / (ntargets[i * 2] + ntargets[i * 2 + 1])
            for i in range(len(mAP_per_class_unshown) // 2)
        ]
        mAP_unshown = np.mean(mAP_per_class_unshown)

    return {
        "mAP": mAP,
        "mAP_per_class": mAP_per_class,
        "mAP_visible": mAP_visible,
        "mAP_per_class_visible": mAP_per_class_visible,
        "mAP_unshown": mAP_unshown,
        "mAP_per_class_unshown": mAP_per_class_unshown,
    }


def print_results(results, classes, metric, event_team=False):
    classes_inv = {v: k for k, v in classes.items()}
    print("--------------------------------------------------")
    print("mAP results for metric:", metric)
    print("--------------------------------------------------")
    print("mAP - {:0.2f}".format(results["mAP"] * 100))
    print("mAP per class:")
    if not event_team:
        for i in range(len(classes)):
            print(
                "{} - {:0.2f}".format(
                    classes_inv[i + 1], results["mAP_per_class"][i] * 100
                )
            )
    else:
        for i in range(len(classes) // 2):
            print(
                "{} - {:0.2f}".format(
                    classes_inv[i * 2 + 1].split("-")[0],
                    results["mAP_per_class"][i] * 100,
                )
            )
    print("--------------------------------------------------")
    if "mAP_no_team" in results.keys():
        print(
            "mAP without considering the team - {:0.2f}".format(
                results["mAP_no_team"] * 100
            )
        )
        print("mAP per class without considering the team:")
        for i in range(len(classes) // 2):
            print(
                "{} - {:0.2f}".format(
                    classes_inv[i * 2 + 1].split("-")[0],
                    results["mAP_per_class_no_team"][i] * 100,
                )
            )
        print("--------------------------------------------------")
    return


def mAPevaluateTest(
    games,
    SoccerNet_path,
    Predictions_path,
    prediction_file="results_spotting.json",
    printed=False,
    event_team=True,
    metric="at1",
):
    # Compute metric
    detections_numpy = list()
    targets_numpy = list()
    closests_numpy = list()

    # list_games = getListGames(split=split)

    # Update classes to start at 1 for label2vector and pred2vector
    x = TdeedVideoClip.get_labels2int_map(BASLabel)
    classes = {}

    for k, v in x.items():
        classes[k[0].value + "-" + k[1].value] = v

    # We reload predictions & labels for consistency in the framerate
    for game in games:
        if zipfile.is_zipfile(SoccerNet_path):
            labels = LoadJsonFromZip(
                SoccerNet_path, os.path.join(game, "Labels-ball.json")
            )
        else:
            labels = json.load(
                open(os.path.join(SoccerNet_path, game, "Labels-ball.json"))
            )
        num_classes = len(classes)
        # convert labels to vector
        labels = label2vector(
            labels,
            num_classes=num_classes,
            version=2,
            EVENT_DICTIONARY=classes,
            framerate=FPS_SN,
            event_team=event_team,
        )

        if zipfile.is_zipfile(Predictions_path):
            predictions = LoadJsonFromZip(
                Predictions_path, os.path.join(game, prediction_file)
            )
        else:
            predictions = json.load(
                open(os.path.join(Predictions_path, game, prediction_file))
            )
        predictions = predictions2vector(
            predictions,
            num_classes=num_classes,
            version=2,
            EVENT_DICTIONARY=classes,
            framerate=FPS_SN,
            event_team=event_team,
        )

        targets_numpy.append(labels)
        detections_numpy.append(predictions)

        closest_numpy = np.zeros(labels.shape) - 1
        # Get the closest action index
        for c in np.arange(labels.shape[-1]):
            indexes = np.where(labels[:, c] != 0)[0].tolist()
            if len(indexes) == 0:
                continue
            indexes.insert(0, -indexes[0])
            indexes.append(2 * closest_numpy.shape[0])
            for i in np.arange(len(indexes) - 2) + 1:
                start = max(0, (indexes[i - 1] + indexes[i]) // 2)
                stop = min(closest_numpy.shape[0], (indexes[i] + indexes[i + 1]) // 2)
                closest_numpy[start:stop, c] = labels[indexes[i], c]
        closests_numpy.append(closest_numpy)

    results = compute_amAP(
        targets_numpy,
        detections_numpy,
        closests_numpy,
        framerate=FPS_SN,
        metric=metric,
        event_team=event_team,
    )

    if printed:
        print_results(results, classes, metric, event_team=event_team)

    return results


def label2vector(
    labels,
    num_classes=17,
    framerate=2,
    version=2,
    EVENT_DICTIONARY={},
    event_team=False,
):
    vector_size = 120 * 60 * framerate

    label_half1 = np.zeros((vector_size, num_classes))

    for annotation in labels["annotations"]:

        time = annotation["gameTime"]
        event = annotation["label"]

        half = int(time[0])

        minutes = int(time[-5:-3])
        seconds = int(time[-2::])
        # annotation at millisecond precision
        if "position" in annotation:
            frame = int(framerate * (int(annotation["position"]) / 1000))
        # annotation at second precision
        else:
            frame = framerate * (seconds + 60 * minutes)

        if not event_team:
            label = EVENT_DICTIONARY[event] - 1
        else:
            event = event + "-" + annotation["team"]
            label = EVENT_DICTIONARY[event] - 1
        # print(event, label, half)

        value = 1
        if "visibility" in annotation.keys():
            if annotation["visibility"] == "not shown":
                value = -1

        if half == 1:
            frame = min(frame, vector_size - 1)
            label_half1[frame][label] = value

    return label_half1


def predictions2vector(
    predictions,
    num_classes=17,
    version=2,
    framerate=2,
    EVENT_DICTIONARY={},
    event_team=False,
):
    vector_size = 120 * 60 * framerate

    prediction_half1 = np.zeros((vector_size, num_classes)) - 1

    for annotation in predictions["predictions"]:

        time = int(annotation["position"])
        event = annotation["label"]

        frame = int(framerate * (time / 1000))

        if not event_team:
            label = EVENT_DICTIONARY[event] - 1
        else:
            event = event + "-" + annotation["team"]
            label = EVENT_DICTIONARY[event] - 1

        value = annotation["confidence"]

        frame = min(frame, vector_size - 1)
        prediction_half1[frame][label] = value

    return prediction_half1
