import math

def calculate_visible_area(fov_degrees, earth_diameter=7917):
    """
    Calculate the visible ground area on Earth from the ISS based on the camera's FOV.
    
    Parameters:
    - fov_degrees (float): Field of view in degrees.
    - earth_diameter (float): Diameter of Earth in miles. Default is 7917 miles.
    
    Returns:
    - float: Visible area in square miles.
    """
    # Constants
    R = earth_diameter / 2  # Radius of Earth in miles
    
    # Convert FOV to radians
    theta_rad = math.radians(fov_degrees / 2)
    
    # Calculate the height of the spherical cap
    h = R * (1 - math.cos(theta_rad))
    
    # Calculate the area of the spherical cap
    area = 2 * math.pi * R * h
    
    return area

def calculate_visible_area_alternative(fov_degrees, distance, earth_diameter=7917):
    """
    Alternative method to calculate visible ground area using distance and FOV.
    
    Parameters:
    - fov_degrees (float): Field of view in degrees.
    - distance (float): Distance from ISS to Earth in miles.
    - earth_diameter (float): Diameter of Earth in miles. Default is 7917 miles.
    
    Returns:
    - float: Visible area in square miles.
    """
    # Radius of Earth
    R = earth_diameter / 2  # 3958.5 miles
    
    # Convert FOV to radians
    fov_rad = math.radians(fov_degrees)
    
    # Calculate the angle from ISS to the edge of the FOV
    # Using the formula: sin(theta) = R / (R + d) * tan(FOV/2)
    # However, for simplicity, we use the spherical cap formula as above
    
    # Calculate the height of the spherical cap
    theta_rad = math.radians(fov_degrees / 2)
    h = R * (1 - math.cos(theta_rad))
    
    # Calculate the area of the spherical cap
    area = 2 * math.pi * R * h
    
    return area

def main():
    # Earth's diameter in miles
    earth_diameter = 7917
    
    # ISS parameters
    iss_distance = 200  # Distance from Earth in miles
    iss_camera_narrow_fov = 2.85  # Narrow FOV in degrees
    iss_camera_wide_fov = 92       # Wide FOV in degrees
    
    # Calculate visible areas
    area_narrow = calculate_visible_area(iss_camera_narrow_fov, earth_diameter)
    area_wide = calculate_visible_area(iss_camera_wide_fov, earth_diameter)
    
    print(f"Visible area with Narrow FOV ({iss_camera_narrow_fov}°): {area_narrow:.2f} square miles")
    print(f"Visible area with Wide FOV ({iss_camera_wide_fov}°): {area_wide:.2f} square miles")
    
    # Calculate intermediate intervals
    intervals = 10  # Number of intervals between narrow and wide FOV
    fov_step = (iss_camera_wide_fov - iss_camera_narrow_fov) / intervals
    
    print("\nVisible areas for intermediate FOVs:")
    for i in range(1, intervals):
        current_fov = iss_camera_narrow_fov + fov_step * i
        current_area = calculate_visible_area(current_fov, earth_diameter)
        print(f"FOV: {current_fov:.2f}°, Area: {current_area:.2f} mi²")
input(math.sqrt(24765169.58)*.5
      )
if __name__ == "__main__":
    main()
