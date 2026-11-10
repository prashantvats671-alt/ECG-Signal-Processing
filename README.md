# ECG Signal Processing and Heart Rate Detection

## Project Overview
This project focuses on processing real-world ECG signals using Python. It uses the MIT-BIH Arrhythmia Database to analyze ECG signals, filter noise, detect R-peaks, and estimate heart rate.

## Technologies Used
- Python
- NumPy
- SciPy
- Matplotlib
- WFDB

## Key Features
- Real ECG data acquisition.
- ECG signal visualization.
- Butterworth Bandpass Filtering.
- R-Peak Detection.
- Heart Rate Calculation.
- Original vs Filtered ECG comparison.

## Methodology
1. Load ECG recording from MIT-BIH database.
2. Extract the ECG signal.
3. Apply Butterworth Bandpass Filter (0.5–40 Hz).
4. Detect R-peaks using SciPy.
5. Calculate R-R intervals.
6. Estimate heart rate in BPM.
7. Visualize ECG signals.

## Results

- Sampling Frequency: 360 Hz
- Detected R-Peaks: 13
- Estimated Heart Rate: 74.44 BPM

## Project Structure

ECG_Project/
- ecg_analysis.py
- real_ecg_result.png
- README.md

## Installation

Install required libraries:

pip install numpy scipy matplotlib wfdb

## Execution

Run the following command:

python ecg_analysis.py

## Future Scope
- Improved R-peak detection.
- ECG annotation comparison.
- Real-time ECG monitoring.
- Interactive ECG dashboard.

## Disclaimer
This project is developed for educational purposes only and is not intended for clinical diagnosis.