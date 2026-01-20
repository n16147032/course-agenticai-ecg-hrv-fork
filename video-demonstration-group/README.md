# Video Demonstration - Group Submission

This folder contains group video demonstrations for the final project presentation.

## Requirements

### Video Specifications

- **Duration:** 10-12 minutes (strict limit)
- **Resolution:** 1080p (1920x1080) minimum, 4K (3840x2160) recommended
- **Frame rate:** 30 fps minimum, 60 fps for screen recordings with motion
- **Audio:** Clear voice narration, consistent volume levels throughout
- **Format:** MP4 (H.264 codec) for upload
- **Platform:** YouTube (Public visibility)
- **Subtitles:** English and Chinese (Traditional) subtitles required

### File Submission

- **YouTube link file:** `YYYY-FamilyName1-FamilyName2-FamilyName3.txt`
- **Naming:** Alphabetical order by family name, ASCII characters only
- **Content:** Single line containing the YouTube URL

**IMPORTANT:** Your video must be set to **Public** so reviewers can access it.

---

## Content Requirements

Your video demonstration should cover:

| Section | Suggested Duration |
|---------|-------------------|
| Title slide | 10 seconds |
| Problem (What?) & Motivation (Why?) | 1-2 minutes |
| System Architecture | 2-3 minutes |
| Live Demo / Working System | 3-4 minutes |
| Results & Evaluation | 2-3 minutes |
| Challenges & Lessons Learned | 1-2 minutes |
| Conclusion | 30 seconds - 1 minute |

**Total:** 10-12 minutes

### What Makes a Good Demo Video

1. **Start with context** - Briefly explain what problem you're solving and why it matters
2. **Show, don't just tell** - Demonstrate your system actually working
3. **Explain as you go** - Narrate what's happening on screen
4. **Highlight key features** - Focus on what makes your solution interesting
5. **Be honest about limitations** - Acknowledge what doesn't work perfectly
6. **End with impact** - Summarize what you achieved and learned

---

## Grading Criteria

The video demonstration is scored based on:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Presentation Delivery & Organization | 20% | Clear structure, good pacing, confident delivery |
| Technical Depth & Soundness | 20% | Engineering design, accurate technical content, demonstrates understanding |
| Evaluation & Validation | 20% | Results, testing, evidence that the system works |
| Contribution & Impact | 10% | Significance of the problem and solution |
| Novelty / Creativity | 10% | Original ideas, creative approaches |
| Team Work | 10% | Evidence of collaboration, balanced contribution |
| Self-Reflection | 10% | Thoughtful self-reflection on limitations and improvement potential |

---

## Video Production Guide for Beginners

This guide focuses on **free tools** that are simple to use, even if you have never recorded or edited a video before.

---

## Recommended Free Tools

### Screen Recording Tools

#### 1. OBS Studio (Open Broadcaster Software)

- **Website:** https://obsproject.com
- **Platforms:** Windows, macOS, Linux
- **Best for:** Professional-quality screen recording, webcam overlay, multiple scenes
- **How to use for recording:**
  1. Download and install from website
  2. Run the Auto-Configuration Wizard on first launch
  3. Add a "Display Capture" source (Settings > Sources > + > Display Capture)
  4. Add an "Audio Input Capture" for your microphone
  5. Click "Start Recording" to begin
  6. Recordings save to your Videos folder by default
- **Tips:**
  - Set output resolution to 1920x1080 or 3840x2160 in Settings > Video
  - Use "Recording" quality preset, not "Streaming"
  - Record in MKV format (safer for long recordings), then remux to MP4

#### 2. ShareX (Windows Only)

- **Website:** https://getsharex.com
- **Platforms:** Windows only
- **Best for:** Quick screen recordings, automatic upload, simple interface
- **How to use for recording:**
  1. Install ShareX
  2. Press Shift+Print Screen to start screen recording
  3. Select the region or window to record
  4. Press the same shortcut to stop
  5. Video automatically saves to Documents/ShareX/Screenshots

#### 3. QuickTime Player (macOS Only)

- **Website:** Built into macOS
- **Platforms:** macOS only
- **Best for:** Simple, no-install screen recording on Mac
- **How to use for recording:**
  1. Open QuickTime Player
  2. File > New Screen Recording
  3. Click the dropdown arrow next to record button to select microphone
  4. Click Record, then click screen to record full screen or drag to select area
  5. Click the stop button in menu bar when done
  6. File > Export As > 1080p or 4K

---

### Video Editing Tools

#### 1. DaVinci Resolve (Recommended)

- **Website:** https://www.blackmagicdesign.com/products/davinciresolve
- **Platforms:** Windows, macOS, Linux
- **Best for:** Professional-grade editing, color correction, audio mixing - all free
- **Key features:**
  - Full editing timeline with unlimited tracks
  - Professional audio tools (Fairlight)
  - Color correction (industry standard)
  - Export directly to YouTube
- **Learning curve:** Medium (powerful but more complex)
- **Tutorial:** https://www.blackmagicdesign.com/products/davinciresolve/training

#### 2. Shotcut

- **Website:** https://shotcut.org
- **Platforms:** Windows, macOS, Linux
- **Best for:** Beginners who want a simpler interface than DaVinci Resolve
- **Key features:**
  - Drag-and-drop interface
  - Wide format support
  - Audio filters and mixing
  - No watermarks, completely free
- **Learning curve:** Easy to medium

#### 3. Kdenlive

- **Website:** https://kdenlive.org
- **Platforms:** Windows, macOS, Linux
- **Best for:** Linux users, those familiar with open-source tools
- **Key features:**
  - Multi-track editing
  - Built-in effects and transitions
  - Automatic audio normalization

---

### Audio Tools

#### 1. Audacity

- **Website:** https://www.audacityteam.org
- **Platforms:** Windows, macOS, Linux
- **Best for:** Audio recording, noise removal, volume normalization
- **Key features:**
  - Record voiceovers separately for better quality
  - Remove background noise (Effect > Noise Reduction)
  - Normalize volume levels (Effect > Normalize)
  - Export in multiple formats

#### 2. VoiceMeeter (Windows)

- **Website:** https://vb-audio.com/Voicemeeter/
- **Platforms:** Windows only
- **Best for:** Real-time audio mixing while recording

---

## Common Video Production Tasks

### Task 1: Recording Your Screen

**Best Tools (ranked):**

| Rank | Tool | Why | How to Do It |
|------|------|-----|--------------|
| 1 | **OBS Studio** | Most flexible, highest quality, works everywhere | Sources > + > Display Capture > Start Recording |
| 2 | **QuickTime** (Mac) / **ShareX** (Win) | Simplest for quick recordings | File > New Screen Recording (Mac) or Shift+PrtScn (Win) |
| 3 | **Built-in OS tools** | Zero setup required | Win+G on Windows 10/11, Cmd+Shift+5 on macOS |

**Tips for good screen recordings:**

- Close unnecessary applications to reduce clutter
- Increase font size in your IDE/terminal (16pt minimum)
- Use a clean desktop background
- Disable notifications before recording
- Record at 1080p or higher

---

### Task 2: Recording Webcam / Face Camera

**Best Tools (ranked):**

| Rank | Tool | Why | How to Do It |
|------|------|-----|--------------|
| 1 | **OBS Studio** | Combine webcam + screen in same recording | Sources > + > Video Capture Device |
| 2 | **QuickTime** (Mac) | Simple webcam recording | File > New Movie Recording |
| 3 | **Windows Camera** | Built-in, no install needed | Search "Camera" in Start menu |

**Tips:**

- Position webcam at eye level
- Face a window or light source (not behind you)
- Use a plain background or blur it
- Look at the camera, not the screen

---

### Task 3: Removing Silent/Dead Sections (Automatic)

This is crucial for keeping viewers engaged. These tools automatically detect and remove silences.

**Best Tools (ranked):**

| Rank | Tool | Why | How to Do It |
|------|------|-----|--------------|
| 1 | **Auto-Editor** | Command-line, very fast, highly accurate | `auto-editor input.mp4 --margin 0.2s` |
| 2 | **DaVinci Resolve** | Built-in silence detection | Edit page > Timeline > Detect Scene Cuts, then manually trim |
| 3 | **Recut** (Mac) | One-click silence removal | Drag video in > adjust threshold > export |

#### Auto-Editor (Recommended for Automatic Cutting)

- **Website:** https://auto-editor.com
- **Install:** `pip install auto-editor` (requires Python)
- **Platforms:** Windows, macOS, Linux
- **How to use:**
  ```bash
  # Basic usage - removes silent parts
  auto-editor your_video.mp4

  # Keep 0.2 seconds of padding around speech
  auto-editor your_video.mp4 --margin 0.2s

  # Adjust silence threshold (lower = more sensitive)
  auto-editor your_video.mp4 --silent-threshold 0.03

  # Export for DaVinci Resolve/Premiere editing
  auto-editor your_video.mp4 --export premiere
  ```
- **Why it's great:** Processes a 10-minute video in under a minute, very accurate

#### Recut (macOS Only)

- **Website:** https://getrecut.com
- **Price:** Free version available (paid version has more features)
- **How to use:**
  1. Drag your video into Recut
  2. Adjust the silence threshold slider
  3. Preview the cuts
  4. Export the trimmed video

---

### Task 4: Normalizing Audio Levels (Automatic)

When combining clips from different recordings, audio levels can vary dramatically. These tools automatically equalize them.

**Best Tools (ranked):**

| Rank | Tool | Why | How to Do It |
|------|------|-----|--------------|
| 1 | **FFmpeg (loudnorm)** | Industry-standard loudness normalization, free | See command below |
| 2 | **DaVinci Resolve Fairlight** | Visual interface, real-time adjustment | Fairlight page > Dynamics > Normalize |
| 3 | **Audacity** | Simple batch processing | Effect > Normalize > -1.0 dB |

#### FFmpeg Loudness Normalization (Recommended)

- **Website:** https://ffmpeg.org
- **Install:**
  - macOS: `brew install ffmpeg`
  - Windows: Download from https://ffmpeg.org/download.html
  - Linux: `sudo apt install ffmpeg`
- **How to use:**
  ```bash
  # Two-pass loudness normalization to broadcast standard (-16 LUFS)
  # Pass 1: Analyze
  ffmpeg -i input.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -

  # Pass 2: Apply (use values from pass 1)
  ffmpeg -i input.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11 -c:v copy output.mp4

  # Simple single-pass (good enough for most cases)
  ffmpeg -i input.mp4 -af loudnorm=I=-16:LRA=11:TP=-1.5 -c:v copy normalized.mp4
  ```

#### DaVinci Resolve Fairlight

1. Switch to the Fairlight page (bottom menu)
2. Select all clips in timeline
3. Right-click > Normalize Audio Levels
4. Choose -16 LUFS for YouTube standard
5. Apply to all clips

#### Audacity Batch Normalization

1. File > Import > Audio (import all clips)
2. Select All (Ctrl+A / Cmd+A)
3. Effect > Normalize
4. Set to -1.0 dB peak
5. Export each track

---

### Task 5: Adding Transitions Between Scenes

Smooth transitions help maintain viewer engagement and signal topic changes.

**Best Tools (ranked):**

| Rank | Tool | Why | How to Do It |
|------|------|-----|--------------|
| 1 | **DaVinci Resolve** | Professional transitions, easy drag-and-drop | Effects Library > Video Transitions > drag to cut point |
| 2 | **Shotcut** | Simple interface, good selection | Open Other > Transition, drag between clips |
| 3 | **Kdenlive** | Many built-in transitions | Right-click between clips > Add Transition |

#### Recommended Transitions for Technical Presentations

| Transition | When to Use | Duration |
|------------|-------------|----------|
| **Cross Dissolve** | Between related topics | 0.5-1 second |
| **Dip to Black** | Between major sections | 1 second |
| **Cut** (no transition) | Within same topic, fast-paced demos | Instant |
| **Wipe** | Avoid - looks dated | N/A |

#### DaVinci Resolve Transitions

1. Go to Edit page
2. Open Effects Library (top left)
3. Navigate to Toolbox > Video Transitions
4. Drag "Cross Dissolve" to the cut point between two clips
5. Adjust duration by dragging edges of transition

**Tip:** Don't overuse transitions. For technical presentations, simple cuts and occasional dissolves work best.

---

### Task 6: Adding Text/Titles

**Best Tools (ranked):**

| Rank | Tool | Why | How to Do It |
|------|------|-----|--------------|
| 1 | **DaVinci Resolve** | Professional titles, templates | Effects > Titles > drag to timeline |
| 2 | **Shotcut** | Simple text overlay | Open Other > Text, add to track above video |
| 3 | **Canva (online)** | Easy design, export as video/image | Create design > Animate > Download as MP4 |

---

### Task 7: Exporting for YouTube

**Recommended Export Settings:**

| Setting | Value |
|---------|-------|
| Container | MP4 |
| Video Codec | H.264 |
| Resolution | 1920x1080 (1080p) or 3840x2160 (4K) |
| Frame Rate | Match source (30 or 60 fps) |
| Bitrate | 8-12 Mbps for 1080p, 35-45 Mbps for 4K |
| Audio Codec | AAC |
| Audio Bitrate | 320 kbps |
| Audio Sample Rate | 48 kHz |

#### DaVinci Resolve Export

1. Go to Deliver page (bottom right)
2. Select "YouTube" preset
3. Choose 1080p or 4K resolution
4. Click "Add to Render Queue"
5. Click "Render All"

#### Shotcut Export

1. File > Export Video
2. Select "YouTube" preset
3. Click Export File

---

### Task 8: Generating Subtitles (English and Chinese)

Subtitles improve accessibility and help viewers follow technical content. You must provide both English and Chinese (Traditional) subtitles.

#### Subtitle File Format for YouTube

YouTube accepts several subtitle formats. **SRT (SubRip)** is recommended for its simplicity and wide compatibility.

**SRT Format Example:**
```srt
1
00:00:00,000 --> 00:00:03,500
Hello, welcome to our project demonstration.

2
00:00:03,500 --> 00:00:07,200
Today we will show you our ECG analysis system.

3
00:00:07,200 --> 00:00:12,000
Let's start with the problem we're trying to solve.
```

**Format Rules:**

- Sequence number (1, 2, 3...)
- Timestamp format: `HH:MM:SS,mmm --> HH:MM:SS,mmm` (comma before milliseconds)
- Subtitle text (can be multiple lines)
- Blank line between entries
- Save with `.srt` extension and UTF-8 encoding (important for Chinese characters)

**File Naming for YouTube:**

- English: `video_name.en.srt`
- Chinese Traditional: `video_name.zh-TW.srt`

---

#### Best Tools for Automatic Subtitle Generation

| Rank | Tool | Languages | How to Do It |
|------|------|-----------|--------------|
| 1 | **Whisper (OpenAI)** | 99 languages including English & Chinese | Command-line, highest accuracy |
| 2 | **YouTube Auto-Captions** | Many languages | Built-in, then download and edit |
| 3 | **macOS Dictation / Windows Speech** | English, Chinese | Built-in OS tools |

---

#### Tool 1: Whisper by OpenAI (Recommended)

The most accurate free transcription tool available. Works offline after installation.

- **Website:** https://github.com/openai/whisper
- **Install:** `uv pip install openai-whisper` (requires Python 3.8+)
- **Platforms:** Windows, macOS, Linux

**Generate English Subtitles:**
```bash
# Basic usage - auto-detects language
whisper your_video.mp4 --output_format srt

# Force English transcription
whisper your_video.mp4 --language en --output_format srt

# Use larger model for better accuracy (slower)
whisper your_video.mp4 --model medium --language en --output_format srt
```

**Generate Chinese Subtitles:**
```bash
# Transcribe Chinese audio
whisper your_video.mp4 --language zh --output_format srt

# Translate English audio to Chinese (requires translation model)
whisper your_video.mp4 --task translate --language zh --output_format srt
```

**Model Sizes (accuracy vs speed tradeoff):**

| Model | Size | English Accuracy | Speed |
|-------|------|------------------|-------|
| tiny | 39 MB | Good | Very fast |
| base | 74 MB | Better | Fast |
| small | 244 MB | Good | Medium |
| medium | 769 MB | Very good | Slow |
│ large-v3-turbo │ 809 MB │ Near Best | Medium │
| large | 1550 MB | Best | Very slow |

**Recommendation:** Use `large-v3-turbo` or `medium` for good balance of accuracy and speed.

**Output:** Creates `your_video.srt` in the same directory with proper timestamps.

##### macOS Apple Silicon: Use MLX-Optimized Whisper (Faster)

macOS users with Apple Silicon (M1/M2/M3/M4) should use MLX-optimized versions instead of standard Whisper. MLX is Apple's machine learning framework that runs natively on the Metal GPU, providing 2-5x faster transcription.

**mlx-whisper (Recommended for macOS):**

- **Website:** https://github.com/ml-explore/mlx-examples/tree/main/whisper
- **Install:** `uv pip install mlx-whisper`
- **Platforms:** macOS (Apple Silicon only)
- **Requirements:** macOS 13.5+, Apple Silicon (M1/M2/M3/M4), Python 3.8+
- **Why use it:** Native Metal GPU acceleration, 2-5x faster than standard Whisper, lower memory usage

```bash
# Generate English subtitles
mlx_whisper your_video.mp4 --model large-v3-turbo --language en --output-format srt

# Generate Chinese subtitles
mlx_whisper your_video.mp4 --model large-v3-turbo --language zh --output-format srt
```

**lightning-whisper-mlx (Fastest for long files):**

- **Website:** https://github.com/mustafaaljadery/lightning-whisper-mlx
- **Install:** `uv pip install lightning-whisper-mlx`
- **Platforms:** macOS (Apple Silicon only)
- **Requirements:** macOS 14.0+, Apple Silicon, Python 3.12+
- **Why use it:** Batch processing optimization, 30-40% faster than mlx-whisper for long videos

```python
from lightning_whisper_mlx import LightningWhisperMLX

whisper = LightningWhisperMLX(model="large-v3-turbo", batch_size=12)
result = whisper.transcribe("your_video.mp4")
print(result["text"])
```

**mlx-whisper vs lightning-whisper-mlx:**

| Aspect | mlx-whisper | lightning-whisper-mlx |
|--------|-------------|----------------------|
| Processing | Sequential | Parallel (batched) |
| Memory usage | Lower | Higher (scales with batch_size) |
| Best for | Single videos | Batch processing many files |

Lightning-whisper-mlx processes multiple audio segments in parallel, which requires more memory but increases throughput. **Accuracy is identical** - both use the same Whisper model weights. For a single 10-12 minute video, mlx-whisper is sufficient and simpler. Use lightning-whisper-mlx when processing many videos or if you have 32GB+ RAM and want maximum speed.

**Note:** For Intel Macs, use the standard `openai-whisper` package instead.

---

#### Tool 2: YouTube Auto-Captions (Built-in)

YouTube can automatically generate captions, which you can then download and edit.

**How to use:**

1. Upload your video to YouTube
2. Wait for automatic captions to be generated (can take several hours)
3. Go to YouTube Studio > Subtitles
4. Click on your video
5. Click the three dots next to "English (auto-generated)"
6. Select "Download" > ".srt"
7. Edit the downloaded file to fix errors
8. Upload the corrected version

**For Chinese subtitles via YouTube:**

1. In YouTube Studio > Subtitles, click "Add Language"
2. Select "Chinese (Traditional)"
3. Click "Add" next to Subtitles
4. Choose "Auto-translate" (translates from English captions)
5. Download, review, and correct the translation
6. Upload the corrected version

**Limitation:** Auto-translate quality varies; manual review is essential.

---

#### Tool 3: Built-in OS Dictation Tools

For recording narration with real-time transcription.

##### macOS: Built-in Dictation + Live Captions

**Dictation (for creating transcript while recording):**

1. System Settings > Keyboard > Dictation > Enable
2. Download "Enhanced Dictation" for offline use
3. In any text editor, press Fn twice to start dictation
4. Speak your narration while it transcribes
5. Manually add timestamps later

**Live Captions (macOS Sonoma 14+):**

1. System Settings > Accessibility > Live Captions > Enable
2. Generates real-time captions for any audio
3. Copy text from Live Captions window

**Supported languages:** English, Cantonese, Mandarin (Simplified/Traditional), and others

##### Windows: Voice Typing + Live Captions

**Voice Typing:**

1. Press Win + H to activate Voice Typing
2. Speak your narration in any text field
3. Supports English and Chinese input

**Live Captions (Windows 11):**

1. Settings > Accessibility > Captions > Live Captions
2. Turn on Live Captions
3. Transcribes any audio playing on your computer
4. Copy transcription text

**Supported languages:** English (more languages being added)

##### Linux: Built-in Speech Recognition

**GNOME (Fedora, Ubuntu with GNOME):**

1. Settings > Accessibility > Typing
2. Enable "Screen Reader" (Orca includes speech capabilities)
3. Limited built-in options; Whisper recommended instead

**Alternative - Nerd Dictation:**

- **Website:** https://github.com/ideasman42/nerd-dictation
- Uses Vosk for offline speech recognition
- Supports multiple languages

---

#### Synchronizing Subtitles with Video

If your subtitles are out of sync, use these tools to adjust timing:

**FFmpeg (shift all subtitles):**
```bash
# Delay subtitles by 2.5 seconds
ffmpeg -i subtitles.srt -ss 2.5 delayed_subtitles.srt

# Advance subtitles by 1 second
ffmpeg -itsoffset -1 -i subtitles.srt -c copy advanced_subtitles.srt
```

**Subtitle Edit (GUI tool):**

- **Website:** https://www.nikse.dk/subtitleedit
- **Platforms:** Windows (native), macOS/Linux (via Mono)
- **Features:**
  - Visual waveform sync
  - Auto-sync to audio
  - Batch timing adjustments
  - Multiple format conversion

**How to sync with Subtitle Edit:**

1. Open your video and subtitle file
2. Tools > Adjust durations
3. Or manually drag subtitle entries to match audio
4. Save as SRT

**Aegisub (Advanced):**

- **Website:** https://aegisub.org
- **Platforms:** Windows, macOS, Linux
- **Best for:** Precise timing, karaoke-style subtitles
- **How to sync:**
  1. Load video and subtitle
  2. Use Audio > Timing Post-Processor for automatic adjustment
  3. Or click on waveform to set start/end times manually

---

#### Uploading Subtitles to YouTube

1. Go to **YouTube Studio** (studio.youtube.com)
2. Select your video from **Content**
3. Click **Subtitles** in the left menu
4. Click **Add Language** and select the language
5. Click **Add** next to "Subtitles"
6. Choose **Upload file**
7. Select **With timing** (for SRT files)
8. Upload your `.srt` file
9. Review the subtitles in the editor
10. Click **Publish**

**Repeat for each language** (English and Chinese Traditional).

---

#### Subtitle Generation Workflow (Recommended)

**For English subtitles:**

1. Install Whisper: `pip install openai-whisper`
2. Generate subtitles: `whisper your_video.mp4 --language en --model small --output_format srt`
3. Review and edit the generated `your_video.srt` file for errors
4. Rename to `your_video.en.srt`
5. Upload to YouTube

**For Chinese subtitles:**

*Option A: If you narrated in Chinese:*
```bash
whisper your_video.mp4 --language zh --model small --output_format srt
```

*Option B: Translate English subtitles to Chinese:*
1. Use the English SRT file
2. Copy text to Google Translate or DeepL
3. Manually create Chinese SRT with same timestamps
4. Or use online SRT translator tools

*Option C: Use YouTube's auto-translate:*
1. Upload English subtitles first
2. In YouTube Studio, add Chinese language
3. Use "Auto-translate" from English
4. Download, review, correct, and re-upload

---

## AI-Powered Video Editing Automation

This section describes how to use AI CLI tools (Claude Code, Gemini CLI, Codex CLI, Antigravity) to automate video post-production after you have recorded your video sequences and placed them in a folder.

The manual workflow described earlier in this document is sufficient and recommended for most students. This section is added for exploring cutting-edge AI agent capabilities, since this is the Agentic AI course.

---

### Overview: What AI CLI Tools Can Control

AI CLI tools like Claude Code, Gemini CLI, and Codex CLI can orchestrate command-line video tools by:
1. Understanding your natural language instructions
2. Generating and executing shell commands (FFmpeg, auto-editor, Whisper, etc.)
3. Analyzing output and making decisions
4. Iterating until the task is complete

These tools act as an intelligent layer that controls the underlying video processing software.

---

### Available AI CLI Tools for Automation

| Tool | Developer | Best For | Cost |
|------|-----------|----------|------|
| [Claude Code](https://claude.com/product/claude-code) | Anthropic | Complex multi-step workflows, code generation | Subscription |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google | Large context (1M tokens), visual analysis | Free tier (60 req/min) |
| [Codex CLI](https://github.com/openai/codex) | OpenAI | Code-focused automation, sandboxed execution | API costs |
| [Antigravity](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/) | Google | Multi-agent orchestration, browser + terminal | Free preview |

---

### What CAN Be Automated (Proven Capabilities)

These tasks can be reliably automated with AI CLI tools controlling command-line video tools:

#### 1. Silence/Dead Section Removal
```bash
# AI agents can run auto-editor with appropriate parameters
auto-editor input.mp4 --margin 0.3s --silent-threshold 0.04
```
**Status:** Fully automatable. AI can analyze the output and adjust parameters if needed.

#### 2. Audio Normalization
```bash
# AI agents can construct and run FFmpeg loudnorm commands
ffmpeg -i input.mp4 -af loudnorm=I=-16:LRA=11:TP=-1.5 -c:v copy output.mp4
```
**Status:** Fully automatable. AI can run two-pass normalization for optimal results.

#### 3. Subtitle Generation
```bash
# AI agents can run Whisper and handle output
whisper video.mp4 --language en --model small --output_format srt
whisper video.mp4 --language zh --model small --output_format srt
```
**Status:** Fully automatable. AI can review transcripts and suggest corrections.

#### 4. Video Concatenation
```bash
# AI agents can create concat files and merge videos
ffmpeg -f concat -safe 0 -i filelist.txt -c copy merged.mp4
```
**Status:** Fully automatable. AI can generate the file list from folder contents.

#### 5. Format Conversion and Export
```bash
# AI agents can convert to YouTube-optimal format
ffmpeg -i input.mp4 -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 320k output.mp4
```
**Status:** Fully automatable.

#### 6. Adding Intro/Outro Sequences
**Status:** Automatable if you provide template files. AI can splice them with your content.

---

### Specialized Video Editing Tools with AI Integration

#### ButterCut (Claude Code Integration)

- **Website:** https://github.com/barefootford/buttercut
- **What it does:** Analyzes footage, creates transcripts with WhisperX, generates rough cuts
- **Output:** FCPXML/xmeml files importable into Final Cut Pro, Premiere, DaVinci Resolve
- **How it works:**
  1. Claude Code checks your system and installs dependencies (Ruby, Python, FFmpeg, WhisperX)
  2. Transcribes audio with word-level timestamps
  3. Analyzes visual content across footage
  4. Generates editorial suggestions based on your preferences
  5. Exports timeline for your video editor

**Use case:** Rapid rough-cut generation for documentary-style content.

#### FFmpeg MCP Server (Model Context Protocol)

- **Website:** https://github.com/Kush36Agrawal/Video_Editor_MCP
- **What it does:** Allows AI agents to control FFmpeg with natural language
- **Setup for Claude Code:**
  ```bash
  claude mcp add-json "video-editor" '{"command":"uv","args":["run","video-editor"]}'
  ```
- **How it works:** You say "Trim input.mp4 to the first 30 seconds" and the MCP server translates to `ffmpeg -i input.mp4 -t 30 -c copy output.mp4`

**Use case:** Natural language video manipulation without memorizing FFmpeg syntax.

---

### What is UNCERTAIN (Experimental/Inconsistent)

These capabilities exist but may produce inconsistent results:

#### 1. Automatic Scene Detection and Smart Cutting

- **What it is:** AI detecting "good" vs "bad" takes, finding natural cut points
- **Status:** Works sometimes, but quality varies significantly
- **Tools:** ButterCut attempts this with transcript + visual analysis
- **Limitation:** AI may not understand your specific narrative intent
- **Recommendation:** Review all AI-suggested cuts manually

#### 2. Automatic Transition Selection

- **What it is:** AI choosing appropriate transitions between scenes
- **Status:** Technically possible, but results often feel generic
- **Limitation:** Transitions are creative decisions that benefit from human judgment
- **Recommendation:** Let AI do cuts, add transitions manually

#### 3. Pacing and Timing Adjustments

- **What it is:** AI adjusting clip durations for better flow
- **Status:** Experimental. Tools like ButterCut can suggest timings
- **Limitation:** Pacing is subjective and context-dependent
- **Recommendation:** Use AI suggestions as starting point, refine manually

#### 4. Multi-Language Subtitle Translation Quality

- **What it is:** Translating English subtitles to Chinese automatically
- **Status:** Works but often requires manual correction
- **Tools:** Whisper for transcription, then AI-assisted translation
- **Recommendation:** Always review translated subtitles for technical accuracy

#### 5. Automatic B-Roll Selection

- **What it is:** AI choosing supplementary footage to overlay on narration
- **Status:** Requires sophisticated setup; not turnkey
- **Limitation:** AI needs a curated library and understanding of your content

---

### What CANNOT Be Automated (Human Judgment Required)

These tasks fundamentally require human creative decision-making:

#### 1. Storytelling and Narrative Arc

- AI processes data (duration, audio levels, timestamps) but doesn't understand emotional impact
- AI knows where a cut *could* happen, not where it *should* happen for your story
- **You must:** Define the narrative structure, key messages, and emotional beats

#### 2. Brand Voice and Presentation Style

- AI cannot intuit your team's personality or the impression you want to make
- Technical presentations require human judgment on what to emphasize
- **You must:** Decide tone, emphasis, and what makes your project unique

#### 3. Technical Accuracy Verification

- AI can transcribe but may mishear technical terms (ECG, HRV, specific function names)
- AI cannot verify that your demo actually works correctly
- **You must:** Review all transcripts for technical accuracy

#### 4. Cultural Context and Audience Awareness

- AI may miss cultural references or assume wrong audience knowledge level
- Translation quality for domain-specific content is unreliable
- **You must:** Review content for appropriateness to your audience

#### 5. Quality Control and Final Approval

- AI produces "good enough" results but may miss subtle issues
- Awkward transitions, mismatched audio, and off-brand visuals slip through
- **You must:** Watch the final video completely before submission

#### 6. Creative Decisions Under Constraints

- AI cannot balance "show the cool feature" vs "stay under 12 minutes"
- Prioritization requires understanding project goals
- **You must:** Make final decisions on what to include/exclude

---

### Example: Automated Post-Production Pipeline

Here's an example of what an AI CLI tool could automate after you record your videos:

```
📁 project_video/
├── 01_intro.mp4           # Your recorded intro
├── 02_architecture.mp4    # System overview recording
├── 03_demo.mp4            # Live demo recording
├── 04_results.mp4         # Results walkthrough
└── 05_conclusion.mp4      # Conclusion recording
```

**Prompt to Claude Code or Gemini CLI:**

```
I have 5 video clips in ./project_video/ that need to be combined into a
final presentation video. Please:

1. Remove silences from each clip using auto-editor (keep 0.3s margin)
2. Normalize audio levels to -16 LUFS across all clips
3. Concatenate clips in numerical order
4. Generate English subtitles using Whisper (small model)
5. Generate Chinese subtitles using Whisper
6. Export final video as 1080p MP4 suitable for YouTube

Put output files in ./output/ folder.
```

**What the AI agent would do:**

1. List files in the directory to understand the inputs
2. Run auto-editor on each clip:
   ```bash
   auto-editor 01_intro.mp4 --margin 0.3s -o 01_intro_cut.mp4
   # ... repeat for each file
   ```
3. Normalize each clip:
   ```bash
   ffmpeg -i 01_intro_cut.mp4 -af loudnorm=I=-16:LRA=11:TP=-1.5 -c:v copy 01_intro_norm.mp4
   ```
4. Create concat file and merge:
   ```bash
   ffmpeg -f concat -safe 0 -i concat_list.txt -c copy merged.mp4
   ```
5. Generate subtitles:
   ```bash
   whisper merged.mp4 --language en --model small --output_format srt
   whisper merged.mp4 --language zh --model small --output_format srt
   ```
6. Final export with YouTube-optimized settings

**Human steps still required:**

- Review and correct subtitle transcripts
- Watch final video for quality issues
- Upload to YouTube and configure settings
- Verify video plays correctly

---

### Tool-Specific Setup Instructions

Assumes that Claude Code/Gemini CLI/Codex CLI are installed.

#### Video Editing Tool Setup
```bash
# Ensure video tools are installed
brew install ffmpeg          # macOS
pip install auto-editor openai-whisper
```

Then describe your video editing task in natural language.

#### Antigravity (Google IDE)
1. Download from https://antigravityide.org
2. Open your project folder
3. Use the Agent panel to describe video processing tasks
4. Antigravity can orchestrate terminal commands with permission controls

**Security features:**
- Granular permission system for terminal commands
- Allow/deny lists for specific operations
- Secure mode limits agent capabilities

---

### Hybrid Workflow: AI + Human

The most effective approach combines AI automation for repetitive tasks with human oversight for creative decisions:

| Phase | AI Does | Human Does |
|-------|---------|------------|
| **Pre-processing** | Remove silences, normalize audio | Review settings, spot-check results |
| **Assembly** | Concatenate clips, basic ordering | Define sequence, narrative flow |
| **Subtitles** | Generate transcripts | Correct errors, verify technical terms |
| **Export** | Apply encoding settings | Final quality check |
| **Upload** | N/A | Configure YouTube, set visibility |

---

### Limitations and Risks

#### Technical Limitations

- AI CLI tools require stable internet for API calls
- Processing time depends on video length and hardware
- Some tools require significant disk space for models (Whisper large: 1.5GB)

#### Quality Risks

- Auto-generated subtitles contain errors (especially technical terms)
- Silence removal may cut important pauses
- Audio normalization may not handle music/speech mix well

#### Security Considerations

- AI agents executing shell commands can be risky
- Always review commands before execution (don't use full-auto mode blindly)
- Keep sensitive files outside the working directory

---

### Recommended Approach Including AI CLI Tools

For your course project video:

1. **Record manually** using OBS or similar (as described earlier)
2. **Use AI CLI tools** for post-processing if comfortable:
   - Silence removal with auto-editor
   - Audio normalization with FFmpeg
   - Subtitle generation with Whisper
3. **Always review** AI-generated content manually
4. **Don't rely on AI** for creative decisions about narrative and pacing
5. **Test your final video** before submitting

The goal is to save time on repetitive tasks while maintaining quality through human oversight.

---

## Quick Start Manual Workflow (Recommended)

For students new to video production, follow this workflow:

### Step 1: Plan Your Video

- Write a script or outline
- Prepare your demo environment
- Test that everything works before recording

### Step 2: Record

1. Install **OBS Studio**
2. Set up display capture + microphone
3. Record in one take if possible, or record sections separately
4. Save as MKV, then remux to MP4 (File > Remux Recordings in OBS)

### Step 3: Remove Silences

1. Install Auto-Editor: `pip install auto-editor`
2. Run: `auto-editor your_recording.mp4 --margin 0.3s`
3. Output is automatically saved as `your_recording_ALTERED.mp4`

### Step 4: Normalize Audio

```bash
ffmpeg -i your_recording_ALTERED.mp4 -af loudnorm=I=-16:LRA=11:TP=-1.5 -c:v copy final.mp4
```

### Step 5: Add Titles (Optional)

1. Open **DaVinci Resolve** or **Shotcut**
2. Import your video
3. Add title at beginning and section headers
4. Export with YouTube preset

### Step 6: Generate Subtitles

1. Install Whisper: `pip install openai-whisper`
2. Generate English subtitles:
   ```bash
   whisper final.mp4 --language en --model small --output_format srt
   ```
3. Rename output to `final.en.srt`
4. Generate or translate Chinese subtitles (see Task 8 for options)
5. Save as `final.zh-TW.srt`
6. Review both files for accuracy

### Step 7: Upload to YouTube

1. Go to https://studio.youtube.com
2. Click "Create" > "Upload videos"
3. Upload your final MP4
4. Set visibility to **Public**
5. Go to Subtitles section and upload both SRT files
6. Copy the video URL

### Step 8: Submit

Create your submission file with the YouTube URL.

---

## YouTube Upload Instructions

### Creating Your YouTube Video

1. **Sign in** to YouTube with your Google account
2. Click the **Create** button (camera icon with +) in the top right
3. Select **Upload videos**
4. Drag and drop your video file or click to browse
5. Fill in the details:
   - **Title:** `[Agentic AI] Project Name - Group Members`
   - **Description:** Brief project summary (use AI to generate based on slides)
   - **Thumbnail:** Upload a custom thumbnail (optional but recommended)
6. Set **Audience:** "No, it's not made for kids"
7. Click **Next** through the screens until you reach **Visibility**
8. Select **Public** (anyone can find and watch your video)
9. Click **Publish**
10. **Upload subtitles:** Go to your video > Subtitles > Add language > Upload your `.srt` files
11. Copy the video URL

### Video URL Format

Your YouTube URL will look like:
```
https://www.youtube.com/watch?v=XXXXXXXXXXX
```
or
```
https://youtu.be/XXXXXXXXXXX
```

Both formats are acceptable for submission.

---

## Submission Instructions

### Create Your Submission File

1. Create a new text file named: `YYYY-FamilyName1-FamilyName2-FamilyName3.txt`
   - Replace `YYYY` with the current year (e.g., 2026)
   - List family names in alphabetical order
   - Use ASCII characters only (no Chinese characters in filename)

2. Add your YouTube URL as the only content:
   ```
   https://www.youtube.com/watch?v=your_video_id
   ```

3. Commit and push to this repository

### Example Submission

Filename: `2026-Chen-Lin-Wang.txt`

Content:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

---

## Submission Checklist

Before submitting, verify:

- [ ] Video is 10-12 minutes long
- [ ] Video resolution is 1080p or higher
- [ ] Audio is clear and audible throughout
- [ ] Audio levels are consistent (no sudden volume changes)
- [ ] Video demonstrates your project working
- [ ] All group members are credited
- [ ] Video is uploaded to YouTube
- [ ] **Video visibility is set to Public**
- [ ] English subtitles uploaded to YouTube
- [ ] Chinese (Traditional) subtitles uploaded to YouTube
- [ ] Submission file is named correctly: `YYYY-Name1-Name2-Name3.txt`
- [ ] Submission file contains only the YouTube URL
- [ ] YouTube URL is accessible (test in incognito/private browser window)


---

## Troubleshooting

### "Video is too large to upload"

- YouTube accepts files up to 256 GB or 12 hours
- If your file is very large, re-export with lower bitrate (8 Mbps for 1080p)

### "Audio is out of sync"

- Record using Variable Frame Rate (VFR) can cause this
- Use OBS with "Constant Frame Rate" enabled in settings
- Or convert with: `ffmpeg -i input.mp4 -c:v copy -af aresample=async=1 output.mp4`

### "Video looks blurry on YouTube"

- YouTube takes time to process HD/4K versions (up to several hours)
- Upload at least a few hours before the deadline
- Make sure you exported at 1080p or higher

### "Recording has no audio"

- Check OBS audio settings: Settings > Audio > select correct microphone
- Make sure microphone is not muted in system settings
- Test with Audio Mixer in OBS before recording

### "Video file is too long/short"

- Aim for 10 minutes; going over up to 12 minutes is better than cutting important content
- Use Auto-Editor to remove dead air and get closer to target duration

---

## Tips for Professional Video Quality

### Preparation

- Clear your desktop of personal files/icons
- Use a clean, professional IDE theme (dark themes work well)
- Increase terminal/code font size to at least 16pt
- Close unnecessary browser tabs and applications
- Silence phone notifications

### Recording

- Record in a quiet environment
- Use a headset microphone for clearer audio than laptop mic
- Record a 30-second test first to check audio/video quality
- Keep water nearby for your voice

### Presentation

- Speak clearly and at a moderate pace
- Pause briefly when transitioning between topics
- Point out important elements on screen ("Notice here that...")
- Show enthusiasm for your project

### Post-Production

- Watch your video once before submitting
- Check that all text on screen is readable
- Verify audio levels don't clip or distort
- Ensure the video starts and ends cleanly (no awkward cuts)

---

### Further Reading and Resources

**AI CLI Tools:**
- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [Google Antigravity](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/)

**Video Automation Projects:**
- [ButterCut - Edit Video with Claude Code](https://github.com/barefootford/buttercut)
- [FFmpeg MCP Server](https://github.com/Kush36Agrawal/Video_Editor_MCP)
- [Claude Code FFmpeg Guide](https://claude-blog.setec.rs/blog/claude-code-ffmpeg-video-audio-processing/)

**Hybrid Workflows:**
- [Creating Marketing Videos with Veo3 + Claude Code + FFmpeg](https://medium.com/@dreamferus/create-marketing-videos-with-veo3-claude-code-codex-cli-ffmpeg-5ec685bdbad7)
- [Hybrid AI Workflows: Spawning Gemini from Claude Code](https://paddo.dev/blog/gemini-claude-code-hybrid-workflow)
- [Claude Code Tips (40+ techniques)](https://github.com/ykdojo/claude-code-tips)

**FFmpeg and Whisper:**
- [FFmpeg 8.0 Native Whisper Integration](https://www.phoronix.com/news/FFmpeg-Lands-Whisper)
- [Auto-Editor Documentation](https://auto-editor.com)
- [Whisper GitHub](https://github.com/openai/whisper)

**AI Video Editing Landscape:**
- [AI Video Editing in 2026: Best Tools & Workflows](https://cutback.video/blog/ai-video-editing-in-2026-best-tools-workflows-automation-explained)
- [Why AI Cannot Replace Human Video Editors](https://www.podcastvideos.com/articles/ai-vs-human-video-editing/)


