"""
Rgeli class module - defines the behavior of individual Rgelis.
"""

import numpy as np
import random

class Rgeli:
    """
    Represents a single Rgeli entity in the simulation.

    A Rgeli is a jellyfish-like creature that drifts through space,
    changes colors, and reacts to cosmic forces.
    """

    COLORS = ['cyan', 'magenta', 'yellow', 'lime', 'orange', 'red', 'purple', 'blue', 'green']

    def __init__(self, x, y, color=None, size=None):
        """
        Initialize a new Rgeli at the given position.

        Args:
            x (float): Initial x-coordinate
            y (float): Initial y-coordinate
            color (str, optional): Initial color. Defaults to random.
            size (int, optional): Size of the Rgeli. Defaults to random.
        """
        self.position = np.array([x, y])
        self.velocity = (np.random.rand(2) - 0.5) * 0.3  # Increased initial velocity
        self.color = color if color else random.choice(self.COLORS)
        # Small sizes for better visuals - no large transparent circles
        self.size = size if size else np.random.randint(15, 40)
        self.age = 0
        self.personality = random.random()  # Influences behavior

    def update_position(self, bounds=(10, 10)):
        """
        Update the Rgeli's position based on its velocity and a smooth drift pattern.

        Args:
            bounds (tuple): The (width, height) boundaries of the space
        """
        # Ensure we have some movement
        if np.linalg.norm(self.velocity) < 0.05:
            # If velocity is too low, give it a kick
            self.velocity = (np.random.rand(2) - 0.5) * 0.3

        # Apply velocity directly - simple movement
        self.position += self.velocity

        # Add small random jitter for more natural movement
        self.position += (np.random.rand(2) - 0.5) * 0.1

        # Occasionally change direction
        if random.random() < 0.05:
            self.velocity += (np.random.rand(2) - 0.5) * 0.2

        # Limit velocity for controlled movement
        speed = np.linalg.norm(self.velocity)
        if speed > 0.4:  # Higher max speed
            self.velocity = (self.velocity / speed) * 0.4

        # Wrap around the boundaries
        for i in range(2):
            if self.position[i] < 0:
                self.position[i] += bounds[i]
            elif self.position[i] > bounds[i]:
                self.position[i] -= bounds[i]

        # Age the Rgeli
        self.age += 1

    def change_color(self, color_change_probability=0.1):
        """
        Randomly change the Rgeli's color with the given probability.

        Args:
            color_change_probability (float): Probability of changing color (0-1)
        """
        if random.random() < color_change_probability:
            # Avoid choosing the same color
            new_colors = [c for c in self.COLORS if c != self.color]
            self.color = random.choice(new_colors)

    def interact(self, other_rgeli, distance_threshold=2.0):
        """
        Interact with another Rgeli if close enough.

        Args:
            other_rgeli (Rgeli): Another Rgeli to interact with
            distance_threshold (float): Maximum distance for interaction

        Returns:
            bool: True if interaction occurred, False otherwise
        """
        # Calculate Euclidean distance between the Rgelis
        distance = np.linalg.norm(self.position - other_rgeli.position)

        # Scale threshold by the size of the Rgelis (larger Rgelis interact from further away)
        size_factor = (self.size + other_rgeli.size) / 200  # Normalize sizes
        actual_threshold = distance_threshold * size_factor

        if distance < actual_threshold:
            # Visual effect: make both Rgelis pulse with a brighter color briefly
            # This is handled in the velocity adjustment

            # Adjust velocities based on interaction - attraction or repulsion
            interaction_strength = 0.08  # Increased for more visible effect

            # Direction from other Rgeli to this one
            direction = (self.position - other_rgeli.position) / max(distance, 0.1)

            # Apply a slight attraction or repulsion based on colors
            if self.color == other_rgeli.color:
                # Same color: slight attraction
                self.velocity -= direction * interaction_strength * 0.5
            else:
                # Different color: slight repulsion
                self.velocity += direction * interaction_strength

            # Limit velocity magnitude
            speed = np.linalg.norm(self.velocity)
            if speed > 0.5:
                self.velocity = (self.velocity / speed) * 0.5

            return True  # Interaction occurred

        return False  # No interaction