# ML-Audio — Machine Learning Audio Processing

A collection of audio processing and machine learning projects completed as part of a Machine Learning II course. Topics range from foundational signal processing to practical applications like speech recognition, audio classification, and audiobook generation.

---

## Repository Structure

```
ML-Audio/
├── 01_Feature_Extraction/
│   └── Feature_Extraction_Audio.ipynb
├── 02_Audio_Classification/
│   └── Audio_Classification.ipynb
├── 03_Speaker_Segmentation/
│   └── Speaker_Segmentation.ipynb
├── 04_Speech_To_Text/
│   └── Speech_To_Text.ipynb
├── 05_Text_To_Speech/
│   └── Text_To_Speech.ipynb
├── 06_Audio_Editor/
│   └── Audio_Editor.ipynb
├── 07_AudioBook_Project/
│   ├── AudioBook.ipynb
│   └── AudioBook.py
└── 08_Frequency_Visualizer/
    └── Frequency_Visualizer.py
```

---

## Projects Overview

### 01 — Feature Extraction
**`Feature_Extraction_Audio.ipynb`**

Extracts a comprehensive set of audio features from WAV files using `librosa` and `pyAudioAnalysis`.

Features extracted:
- Short-term Energy
- Spectral Centroid
- Spectral Bandwidth & Rolloff
- Zero-Crossing Rate (ZCR)
- MFCC (13 coefficients)
- Chromagram (12 pitch classes)
- Mid-term feature aggregation
- Spectrogram (STFT)

**Libraries:** `librosa`, `numpy`, `matplotlib`, `sklearn`

---

### 02 — Audio Classification
**`Audio_Classification.ipynb`**

Classifies audio clips into genres/categories using an SVM classifier trained on spectral features extracted with `pyAudioAnalysis`.

Highlights:
- Splits raw WAV files into fixed-length clips for training
- Extracts mid-term features (`spectral_centroid_mean`, `energy_entropy_mean`)
- Trains an SVM with RBF kernel (99%+ training accuracy)
- Visualizes the decision surface
- Predicts on unseen test clips with confidence scores
- Also uses the `pyAudioAnalysis` all-in-one `extract_features_and_train` wrapper

**Libraries:** `pyAudioAnalysis`, `sklearn`, `numpy`, `matplotlib`, `scipy`

---

### 03 — Speaker Segmentation / Diarization
**`Speaker_Segmentation.ipynb`**

Segments an audio recording by speaker using unsupervised K-means clustering on mid-term audio features.

Highlights:
- Loads stereo WAV and converts to mono
- Extracts mid-term features and normalizes them
- Clusters segments into N speaker groups using K-means
- Saves each speaker's audio segments to separate WAV files
- Tested on two different multi-speaker recordings

**Libraries:** `pyAudioAnalysis`, `sklearn`, `numpy`, `scipy`, `IPython`

---

### 04 — Speech To Text
**`Speech_To_Text.ipynb`**

Converts spoken audio to text using the `SpeechRecognition` library with Google's speech recognition API.

Highlights:
- Microphone input support (with graceful fallback)
- Processes WAV audio files
- Configures energy threshold and ambient noise adjustment
- Tested on multiple audio samples of varying lengths

**Libraries:** `speech_recognition`, `IPython`

---

### 05 — Text To Speech
**`Text_To_Speech.ipynb`**

Converts written text to speech using Google Text-to-Speech (`gTTS`).

Highlights:
- Converts English text to MP3 audio
- Supports multiple languages (English and Hindi demonstrated)
- Reads text directly from `.txt` files
- Plays generated audio inline in Jupyter

**Libraries:** `gTTS`, `IPython`

---

### 06 — Audio Editor (Silence Removal)
**`Audio_Editor.ipynb`**

Edits audio by automatically detecting and removing silent/low-energy segments.

Highlights:
- Reads WAV files using both `pydub` and `scipy.io.wavfile`
- Splits the signal into 1-second segments
- Computes per-segment energy
- Removes segments below 50% of the median energy threshold
- Outputs a clean, silence-free audio file

**Libraries:** `pydub`, `scipy`, `numpy`

---

### 07 — Audiobook Project
**`AudioBook.ipynb` / `AudioBook.py`**

An end-to-end project that converts a PDF document into a spoken audiobook.

Pipeline:
1. Extract text from a PDF using `PyPDF2`
2. Clean and prepare the extracted text
3. Convert text to speech using `pyttsx3`
4. Save the result as a `.wav` audio file

**Libraries:** `PyPDF2`, `pyttsx3`

---

### 08 — Real-Time Frequency Visualizer
**`Frequency_Visualizer.py`**

A real-time terminal-based frequency spectrum visualizer that reads live audio from the microphone and displays an FFT bar chart in the terminal.

Highlights:
- Captures live audio via `pyaudio`
- Computes FFT of each audio buffer in real-time
- Renders a terminal frequency bar chart with `termplotlib`
- Run with `python Frequency_Visualizer.py` (press `Ctrl+C` to stop)

**Libraries:** `pyaudio`, `numpy`, `scipy`, `termplotlib`

---

## Setup & Installation

It is recommended to use a dedicated conda or virtual environment.

```bash
# Create a conda environment
conda create -n audio_env python=3.12
conda activate audio_env

# Install core libraries
pip install librosa pyAudioAnalysis SpeechRecognition gTTS pydub PyPDF2 pyttsx3
pip install pyaudio termplotlib numpy scipy matplotlib scikit-learn plotly

# macOS users: install PortAudio for pyaudio
brew install portaudio
```

---

## Key Libraries

| Library | Purpose |
|---|---|
| `librosa` | Audio loading, MFCC, spectrogram, beat tracking |
| `pyAudioAnalysis` | Feature extraction, classification, segmentation |
| `SpeechRecognition` | Speech-to-text via Google API |
| `gTTS` | Text-to-speech using Google TTS |
| `pyttsx3` | Offline text-to-speech engine |
| `pydub` | Audio file I/O and manipulation |
| `PyPDF2` | PDF text extraction |
| `pyaudio` | Real-time microphone input |
| `scikit-learn` | SVM classifier, K-means clustering |

---

## Notes

- Notebooks were developed and tested on **macOS** with Python 3.12.
- Some notebooks require audio sample files (`.wav`) in the same directory. The expected filenames are noted in each notebook's first cell.
- The `Frequency_Visualizer.py` script requires a working microphone and must be run from the terminal (not inside Jupyter).
