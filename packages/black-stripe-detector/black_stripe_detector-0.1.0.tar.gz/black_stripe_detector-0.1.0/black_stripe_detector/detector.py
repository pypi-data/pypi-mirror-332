import os
from PIL import Image
import numpy as np

def detect_black_stripes(image_path, threshold=10, stripe_threshold=0.99, min_stripe_height=1, debug=True):
    """
    Detects horizontal black stripes in an image that may indicate rendering errors.
    Distinguishes between error stripes and legitimate black backgrounds with objects.
    
    Args:
        image_path: Path to the image to analyze.
        threshold: Value defining how dark a pixel must be to be considered black.
        stripe_threshold: Percentage of black pixels in a row to consider it a stripe.
        min_stripe_height: Minimum number of consecutive black rows to consider a stripe.
        debug: If True, prints diagnostic information during analysis.
    
    Returns:
        bool: True if black stripes likely to be errors are detected, False otherwise.
    """
    try:
        image = Image.open(image_path)
    except IOError:
        print(f"Error opening image: {image_path}")
        return False
    
    image = image.convert("RGB")
    np_image = np.array(image)
    if debug:
        print(f"\nAnalyzing img: {image_path}")
    
    # Get image dimensions
    height, width = np_image.shape[:2]
    
    # Detect black pixels
    black_pixels = np.all(np_image < threshold, axis=2)
    
    # Count black pixels per row
    black_rows = []
    black_percentages_per_row = []
    
    for i, row in enumerate(black_pixels):
        black_percentage = np.sum(row) / len(row)
        black_percentages_per_row.append(black_percentage)
        if black_percentage > stripe_threshold:
            black_rows.append(i)
    
    # If no black rows according to our threshold, no stripes
    if not black_rows:
        if debug:
            print(f"No black rows detected in {image_path}")
        return False
    
    # Count black pixels in the entire image
    total_pixels = height * width
    total_black_pixels = np.sum(black_pixels)
    total_black_percentage = total_black_pixels / total_pixels
    
    if debug:
        print(f"Total black percentage: {total_black_percentage:.2%}")
    
    # Analyze black row distribution
    # Group black rows into stripes
    stripes = []
    if black_rows:
        current_stripe = [black_rows[0]]
        
        for i in range(1, len(black_rows)):
            if black_rows[i] == black_rows[i-1] + 1:
                current_stripe.append(black_rows[i])
            else:
                if len(current_stripe) >= min_stripe_height:
                    stripes.append(current_stripe)
                current_stripe = [black_rows[i]]
        
        # Don't forget the last stripe
        if len(current_stripe) >= min_stripe_height:
            stripes.append(current_stripe)
    
    if debug:
        print(f"Stripes detected: {len(stripes)}")
    
    # LEGITIMATE BLACK BACKGROUND ANALYSIS
    # Check if it's a black background with central objects pattern
    if total_black_percentage > 0.6:  # If the image is mostly black
        # Calculate black distribution by region (top, middle, bottom)
        thirds = height // 3
        top_region = black_percentages_per_row[:thirds]
        middle_region = black_percentages_per_row[thirds:2*thirds]
        bottom_region = black_percentages_per_row[2*thirds:]
        
        avg_top = np.mean(top_region) if top_region else 0
        avg_middle = np.mean(middle_region) if middle_region else 0
        avg_bottom = np.mean(bottom_region) if bottom_region else 0
        
        if debug:
            print(f"Black distribution by region: Top={avg_top:.2%}, Middle={avg_middle:.2%}, Bottom={avg_bottom:.2%}")
        
        # Check if there is more content in the middle region (typical pattern of objects on a black background)
        if avg_middle < min(avg_top, avg_bottom) - 0.05:
            if debug:
                print(f"LEGITIMATE BLACK BACKGROUND: Less black in the central region (objects on background)")
            return False
        
        # Check if it's a pattern of central objects with a uniform black background
        # Calculate the variance of black between rows
        variance = np.var(black_percentages_per_row)
        if debug:
            print(f"Variance between rows: {variance:.4f}")
        
        # If variance is low, it's likely a uniform black background with objects
        # If variance is high, there are likely abrupt stripes (error)
        if variance < 0.05 and total_black_percentage > 0.7:
            if debug:
                print(f"LEGITIMATE BLACK BACKGROUND: Uniform black distribution (low variance)")
            return False
    
    # ERROR DETECTION
    is_error = False
    
    # If we have stripes in specific positions
    if stripes:
        # Check each stripe
        for stripe in stripes:
            stripe_height = len(stripe)
            start_position = stripe[0]
            end_position = stripe[-1]
            
            # Calculate the percentage of the image height occupied by the stripe
            height_percentage = stripe_height / height
            
            if debug:
                print(f"Stripe detected: rows {start_position}-{end_position} ({height_percentage:.2%} of the image)")
            
            # 1. Error detection criterion: perfectly black stripe at the edges
            is_top_edge = start_position < height * 0.1
            is_bottom_edge = end_position > height * 0.9
        

            # 1. Error detection criterion: perfectly black stripe at the edges
            if (is_top_edge or is_bottom_edge) and height_percentage < 0.3 and total_black_percentage < 0.85:
                average_black_in_stripe = np.mean([black_percentages_per_row[i] for i in stripe])
                
                # If the stripe is very black (almost perfect)
                if average_black_in_stripe > 0.99:
                    # Exclude small edge stripes if the image has a black background with central objects pattern
                    if total_black_percentage > 0.3 and total_black_percentage < 0.7:
                        # Check if the image has less black in the central region (objects on black background)
                        thirds = height // 3
                        middle_region = black_percentages_per_row[thirds:2*thirds]
                        avg_middle = np.mean(middle_region) if middle_region else 0
                        
                        if avg_middle < 0.5:  # If the central region has less than 50% black
                            if debug:
                                print(f"LEGITIMATE BLACK BACKGROUND: Edge stripe with central objects. Not considered an error.")
                            is_error = False
                        else:
                            is_error = True
                    else:
                        is_error = True
                    
                    if is_error and debug:
                        print(f"DETECTED RENDERING ERROR: Perfectly black stripe at {'top' if is_top_edge else 'bottom'} edge")
                    break
    
    # 2. Error detection criterion: perfectly black stripes between non-black regions
    if not is_error and len(black_percentages_per_row) > 5:
        # Look for perfectly black stripes (100%) surrounded by non-black content
        for i in range(2, len(black_percentages_per_row) - 2):
            # If a row is completely black but its neighbors are not
            if (black_percentages_per_row[i] > 0.995 and 
                (black_percentages_per_row[i-2] < 0.9 or black_percentages_per_row[i+2] < 0.9)):
                is_error = True
                if debug:
                    print(f"DETECTED RENDERING ERROR: Perfectly black stripe surrounded by content")
                break
    
    # 3. Additional criterion: extremely abrupt transitions typical of rendering errors
    if not is_error and len(black_percentages_per_row) > 3:
        for i in range(1, len(black_percentages_per_row) - 1):
            # Only look for extreme transitions (from almost 0% to almost 100% or vice versa)
            if ((black_percentages_per_row[i] > 0.99 and black_percentages_per_row[i+1] < 0.1) or
                (black_percentages_per_row[i] < 0.1 and black_percentages_per_row[i+1] > 0.99)):
                
                # Ensure we're not in a mostly black image (black background)
                if total_black_percentage < 0.85:
                    is_error = True
                    if debug:
                        print(f"DETECTED RENDERING ERROR: Extremely abrupt transition at row {i}")
                    break
    
    return is_error

def analyze_frames(output_directory, threshold=10, stripe_threshold=0.99, min_stripe_height=1, debug=True):
    """
    Analyzes all frames in a directory to detect those with black stripes.
    
    Returns:
        list: A list of dictionaries containing the file name and full path of corrupted images.
              Example: [{"name": "0.png", "path": "/path/to/0.png"}, ...]
    """
    corrupted_frames = []
    
    for root, dirs, files in os.walk(output_directory):
        for file in files:
            # Check if the file is one of the supported formats
            if file.lower().endswith(("iris", "jpeg", "cineon", "targa", "webp", 
                                      "targa_raw", "jpeg2000", "dpx", "png", 
                                      "bmp", "tiff")):
                file_path = os.path.join(root, file)
                if detect_black_stripes(file_path, threshold, stripe_threshold, min_stripe_height, debug):
                    corrupted_frames.append({"name": file, "path": file_path})
    
    return corrupted_frames