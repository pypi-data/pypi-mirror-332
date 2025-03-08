import os
from moviepy import VideoFileClip


def compress_gif(output_path, target_size_kb = 500):
    """ Reduce GIF size by lowering quality iteratively. """
    quality = 50 #start with medium quality
    step = 10 # Reduce quality step by step

    while os.path.getsize(output_path) > target_size_kb * 1024 and quality > 10:
        temp_output = output_path.replace(".gif", "_compressed.gif")
        clip = VideoFileClip(output_path).write_gif(temp_output, fps=10, programm="ffmpeg", opt="OptimizeTransparency", quality=quality)
        os.replace(temp_output, output_path)
        quality -= step # reduce quality if needed


def mp4_to_gif(input_path, output_path, duration=None):
    """ Convert MP4 to GIF with user-defined duration (max 5s) and auto-compress to ≤500KB. """
    if not os.path.exists(input_path):
        print("❌ Error : File not found")
        return
    
    clip = VideoFileClip(input_path)

    # Set default duration if None provided
    if duration is None:
        duration = 5
    else:
        duration = min(duration, 5)

    clip = clip.subclipped(0,min(duration,clip.duration))

    clip.write_gif(output_path, fps=10,program="ffmpeg")

    
    # Compress if GIF is too large
    if os.path.getsize(output_path) > 500 * 1024:
        print("📉 Compressing GIF to fit under 500KB...")
        compress_gif(output_path)


    print(f"✅ GIF saved at {output_path} ")

