# Eye Tracking Calibration Dataset

- [Eye Tracking Calibration Dataset](#eye-tracking-calibration-dataset)
  - [Overview](#overview)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Dataset Contents](#dataset-contents)
  - [Methodology](#methodology)
  - [Potential Use Cases](#potential-use-cases)
  - [Acknowledgments](#acknowledgments)

## Overview

This dataset is a comprehensive collection of eye-tracking calibration data gathered from multiple participants. It is designed to support research and development in fields such as gaze estimation, eye-tracking systems, human-computer interaction, and computer vision. The dataset includes raw images, facial landmarks, and calibration metadata, making it a versatile resource for training machine learning models and conducting gaze analysis studies.

## Installation

`pip install eye-tracking-collector`

## Usage

`eye-tracking-collector collect --upload --api-key=<XXXXX>`


## Dataset Contents

1. Metadata (JSON):
   1. dataset.json:
        1. Landmark coordinates for each frame.
        2. Calibration dot positions and corresponding distances.
        3. Estimated distance of face from camera.
        4. Dot position ( place where eyes are looking at)
   1. screen_details.json:
        1. Screen and window size information to aid in experimental replication.

## Methodology

```math
R = 50, 70 cm \\
N = 10
```

1. Collection Process:
   1. Participants focused on points in a 5x5 grid displayed on a screen.
   2. Eye alignment, eyes position on screen and distance R were continuously monitored during data collection.
   3. N samples were recorded for each calibration point.
2. Participant Diversity:
   1. Data was collected from individuals of various age groups to ensure broad applicability.

## Potential Use Cases

1. Training gaze estimation models for real-time applications.
1. Developing assistive technologies for people with mobility impairments.
1. Conducting behavioral studies using gaze patterns.
1. Advancing research in cognitive science, computer vision, and HCI.

## Acknowledgments

This dataset was collected using a Python-based tool that leverages:

1. MediaPipe FaceMesh for landmark detection.
1. OpenCV for camera integration and visualization.

We thank all participants who contributed their data to make this dataset a valuable resource for the research community.
