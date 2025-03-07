import cv2
import os
import time
import pickle

def convert_video_to_ascii(video_path, scale=0.1, output_file="ascii_video.pkl"):
    """
    Convert a video to a series of ASCII frames and save to a file
    """
    # Define ASCII characters from darkest to brightest
    ascii_chars = " .:-=+*#%@"
    
    # Load video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Calculate ASCII dimensions
    new_width = int(frame_width * scale)
    new_height = int(frame_height * scale * 0.5)  # Adjust for terminal aspect ratio
    
    # Store video metadata and frames
    ascii_video = {
        "fps": fps,
        "width": new_width,
        "height": new_height,
        "frames": []
    }
    
    print(f"Converting video to ASCII: {new_width}x{new_height} at {fps} fps")
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process frame
        resized = cv2.resize(frame, (new_width, new_height))
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        
        # Normalize for better contrast
        min_val, max_val, _, _ = cv2.minMaxLoc(gray)

        if max_val > min_val:
            normalized = (gray - min_val) * 255.0 / (max_val - min_val)
        else:
            normalized = gray
        
        # Convert to ASCII
        ascii_frame = []
        for y in range(new_height):
            ascii_line = ""
            for x in range(new_width):
                pixel_value = normalized[y, x]
                char_idx = min(int(pixel_value * (len(ascii_chars) - 1) / 255), len(ascii_chars) - 1)
                ascii_line += ascii_chars[char_idx]
            ascii_frame.append(ascii_line)
        
        # Add frame to video
        ascii_video["frames"].append(ascii_frame)
        frame_count += 1
        
        # Show progress
        if frame_count % 10 == 0:
            print(f"Processed {frame_count} frames")
    
    # Save ASCII video to file
    print(f"Saving ASCII video with {frame_count} frames to {output_file}")
    with open(output_file, 'wb') as f:
        pickle.dump(ascii_video, f)
    
    cap.release()
    return output_file

def play_ascii_video_console(ascii_file):
    """
    Play a previously saved ASCII video file in the console (no curses)
    """
    # Load the ASCII video
    with open(ascii_file, 'rb') as f:
        ascii_video = pickle.load(f)
    
    fps = ascii_video["fps"]
    frame_time = 1/fps
    
    # Get dimensions
    width = ascii_video["width"]
    height = ascii_video["height"]
    
    # Play each frame
    frame_count = 0
    start_time = time.time()
    
    try:
        for frame in ascii_video["frames"]:
            # Clear the console (cross-platform)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Print the frame
            for line in frame:
                print(line)
            
            # Control frame rate
            frame_count += 1
            elapsed = time.time() - start_time
            sleep_time = max(0, frame_count * frame_time - elapsed)
            time.sleep(sleep_time)
            
    except KeyboardInterrupt:
        print("Playback stopped by user")

def main():
    # Simple menu
    print("ASCII Video Converter")
    print("1. Convert video to ASCII and save")
    print("2. Play ASCII video (if already converted)")
    
    try:
        choice = input("Select an option (1-2): ")
        
        if choice == "1":
            # Get video path from user
            video_path = input("Enter the path to your video file: ")
            
            # Check if the video exists
            if not os.path.isfile(video_path):
                print(f"Error: Video file {video_path} not found")
                return
            
            # Get output file name
            default_output = "ascii_video.pkl"
            output_file = input(f"Enter output file name [{default_output}]: ") or default_output
            
            # Convert the video to ASCII and save
            ascii_file = convert_video_to_ascii(video_path, output_file=output_file)
            if ascii_file:
                print(f"Conversion complete. ASCII video saved to {ascii_file}")
                play_now = input("Play the ASCII video now? (y/n): ")
                if play_now.lower() == 'y':
                    play_ascii_video_console(ascii_file)
        
        elif choice == "2":
            # Play an existing ASCII video file
            default_file = "ascii_video.pkl"
            ascii_file = input(f"Enter ASCII video file name [{default_file}]: ") or default_file
            if os.path.isfile(ascii_file):
                play_ascii_video_console(ascii_file)
            else:
                print(f"Error: ASCII video file {ascii_file} not found")
        
        else:
            print("Invalid option selected")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    