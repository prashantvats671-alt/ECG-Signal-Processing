import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# Load real ECG data from MIT-BIH database
record = wfdb.rdrecord('100', pn_dir='mitdb', sampto=3600)

# Extract first ECG channel
ecg = record.p_signal[:, 0]
fs = record.fs

# Create time axis
t = np.arange(len(ecg)) / fs

# Design Butterworth bandpass filter
b, a = butter(4, [0.5, 40], btype='bandpass', fs=fs)

# Apply filter
filtered_ecg = filtfilt(b, a, ecg)

# Detect R-peaks
peaks, _ = find_peaks(
    filtered_ecg,
    distance=int(0.25 * fs),
    prominence=0.5
)

# Calculate heart rate
rr_intervals = np.diff(peaks) / fs

if len(rr_intervals) > 0:
    heart_rate = 60 / np.mean(rr_intervals)
else:
    heart_rate = 0

# Display results
print("ECG Sampling Frequency:", fs, "Hz")
print("Detected R-peaks:", len(peaks))
print("Estimated Heart Rate:", round(heart_rate, 2), "BPM")

# Plot ECG
plt.figure(figsize=(14, 6))

plt.plot(t, ecg, label="Original ECG")
plt.plot(t, filtered_ecg, label="Filtered ECG")

plt.scatter(
    t[peaks],
    filtered_ecg[peaks],
    color="red",
    label="Detected R-peaks"
)

plt.title("Real ECG Signal Processing - MIT-BIH")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid()
plt.tight_layout()

plt.savefig("real_ecg_result.png", dpi=300)
plt.show()