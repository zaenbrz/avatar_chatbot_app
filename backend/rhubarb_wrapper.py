import subprocess
import os
import uuid

UPLOAD_DIR = "uploads"

def convert_to_wav(input_file: str) -> str:
    """Convert audio file (e.g., MP3) to WAV for Rhubarb using FFmpeg."""
    output_file = f"{os.path.splitext(input_file)[0]}_converted.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-i", input_file, "-ar", "44100", "-ac", "1", output_file],
        check=True
    )
    return output_file

def run_rhubarb(audio_path: str, output_dir: str = UPLOAD_DIR) -> str:
    """Run Rhubarb on an audio file and return path to output JSON."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert to wav if not already
    if not audio_path.lower().endswith(".wav"):
        audio_path = convert_to_wav(audio_path)

    # Unique filename for JSON
    output_file = os.path.join(output_dir, f"{uuid.uuid4().hex}.json")

    try:
        subprocess.run(
            ["rhubarb", "-f", "json", "-o", output_file, audio_path],
            check=True
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Rhubarb failed: {e}")

    return output_file
