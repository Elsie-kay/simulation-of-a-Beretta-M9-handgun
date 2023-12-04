import numpy as np
import matplotlib.pyplot as plt

def simulate_bullet_trajectory(angle, muzzle_velocity=380, gravity=9.81, time_step=0.01):
    """
    Simulate the bullet trajectory of a Beretta M9 handgun.
    
    Parameters:
    angle (float): Angle of fire in degrees.
    muzzle_velocity (float): Muzzle velocity of the bullet in meters per second (default: 380 m/s).
    gravity (float): Acceleration due to gravity in m/s^2 (default: 9.81 m/s^2).
    time_step (float): Time step for the simulation in seconds (default: 0.01 s).
    
    Returns:
    (tuple): Tuple containing:
        - times (np.array): Array of time points.
        - x_positions (np.array): Array of x positions (horizontal).
        - y_positions (np.array): Array of y positions (vertical).
    """
    # Convert angle to radians
    angle_rad = np.radians(angle)

    # Initial velocity components in x and y directions
    v_x = muzzle_velocity * np.cos(angle_rad)  # Horizontal component
    v_y = muzzle_velocity * np.sin(angle_rad)  # Vertical component

    # Time of flight calculation
    time_of_flight = 2 * v_y / gravity  # Time until bullet falls back to initial height

    # Generating time points for the simulation
    times = np.arange(0, time_of_flight, time_step)

    # Calculating x and y positions over time
    x_positions = v_x * times  # Horizontal position
    y_positions = v_y * times - 0.5 * gravity * times**2  # Vertical position

    return times, x_positions, y_positions

# Example simulation with a firing angle of 45 degrees
angle = 45
times, x_positions, y_positions = simulate_bullet_trajectory(angle)

# Plotting the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x_positions, y_positions)
plt.title("Bullet Trajectory of Beretta M9 Handgun")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()
