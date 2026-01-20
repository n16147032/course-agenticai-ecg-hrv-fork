import matplotlib.pyplot as plt
import numpy as np

def plot_results(original_signal, cleaned_signal, rpeaks, fs, output_path=None, signal_type='ECG'):
    """
    Generate a dashboard figure with:
    1. Raw vs Cleaned segment (Centered for scale)
    2. Tachogram (Peak-to-peak intervals)
    """
    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=False, facecolor='white')
    ax1.set_facecolor('white')
    ax2.set_facecolor('white')
    
    # 1. Prepare segment for visualization (First 10s)
    limit_sec = 10
    limit_samples = min(int(limit_sec * fs), len(original_signal))
    t = np.arange(limit_samples) / fs
    
    # Scale Raw: subtract mean to center it around the cleaned signal (which is usually zero-centered)
    # This allows the y-axis to zoom in on the actual signal fluctuations
    raw_segment = original_signal[:limit_samples]
    raw_centered = raw_segment - np.mean(raw_segment)
    
    clean_segment = cleaned_signal[:limit_samples]
    
    ax1.plot(t, raw_centered, color='lightgray', label='Raw (Centered)', alpha=0.7, linewidth=1)
    ax1.plot(t, clean_segment, color='teal', label='Cleaned', linewidth=1.5)
    
    # Overlay peaks
    peak_indices = rpeaks[rpeaks < limit_samples]
    peak_label = 'R-peaks' if signal_type == 'ECG' else 'Systolic Peaks'
    ax1.scatter(peak_indices / fs, clean_segment[peak_indices], color='red', marker='x', label=peak_label, zorder=3)
    
    ax1.set_title(f"{signal_type} Signal Visualization (First 10s)", fontsize=14, fontweight='bold', color='black')
    ax1.set_xlabel("Time (s)", color='black')
    ax1.set_ylabel("Amplitude (A.U.)", color='black')
    ax1.tick_params(colors='black')
    ax1.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='lightgray')
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # 2. Tachogram (Restricted to same 10s window)
    intervals_ms = np.diff(rpeaks) / fs * 1000
    
    # Filter intervals corresponding to peaks within the limit
    # We use peak_indices from the first plot which are already < limit_samples
    if len(peak_indices) > 1:
        relevant_intervals = np.diff(peak_indices) / fs * 1000
    else:
        relevant_intervals = []

    interval_label = 'RR' if signal_type == 'ECG' else 'PP'
    
    if len(relevant_intervals) > 0:
        ax2.plot(relevant_intervals, marker='o', linestyle='-', color='indigo', markersize=3, linewidth=1, alpha=0.8)
        # Add a horizontal line for the median to show stability
        ax2.axhline(np.median(relevant_intervals), color='red', linestyle='--', alpha=0.5, label='Median')
    else:
        ax2.text(0.5, 0.5, "Not enough peaks in first 10s", ha='center', va='center')
    
    ax2.set_title(f"{interval_label} Tachogram (Interval Stability - First 10s)", fontsize=14, fontweight='bold')
    ax2.set_xlabel("Beat Number")
    ax2.set_ylabel("Interval (ms)")
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    
    plt.tight_layout(pad=3.0)
    
    if output_path:
        plt.savefig(output_path, dpi=120)
        plt.close()
    else:
        return fig
