def process_interactions(self):
    """Process interactions between Rgelis."""
    interaction_count = 0
    interaction_positions = []

    # Check each pair of Rgelis
    for i, rgeli1 in enumerate(self.rgelis):
        for rgeli2 in self.rgelis[i + 1:]:
            if rgeli1.interact(rgeli2):
                interaction_count += 1
                # Record the midpoint of the interaction for visual effect
                mid_point = (rgeli1.position + rgeli2.position) / 2
                interaction_positions.append((mid_point, rgeli1.color, rgeli2.color))

    # Increase score based on interactions
    if interaction_count > 0:
        # Add points for interactions
        self.score += interaction_count

        # Visualize all interactions with more noticeable effects
        for pos, color1, color2 in interaction_positions:
            # Create a star-like interaction marker
            size = 0.2  # Larger size for visibility

            # Create a more noticeable interaction marker - small star/burst
            angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)
            for idx, angle in enumerate(angles):
                # Alternate colors between the two interacting Rgelis
                marker_color = color1 if idx % 2 == 0 else color2

                # Calculate point on star
                x = pos[0] + np.cos(angle) * size
                y = pos[1] + np.sin(angle) * size

                # Draw a small line from center to point
                line = plt.Line2D([pos[0], x], [pos[1], y],
                                  color=marker_color, linewidth=1.5, alpha=0.7,
                                  solid_capstyle='round')
                self.ax.add_line(line)
            """
RgelisGame class module - manages the simulation of multiple Rgelis.
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse
import random
from .rgeli import Rgeli


class RgelisGame:
    """
    Manages a simulation of multiple Rgelis floating in their own dimension.
    """

    def __init__(self, num_rgelis=0, width=10, height=10, background_color='black', fps=60):
        """
        Initialize the Rgelis game/simulation.

        Args:
            num_rgelis (int): Initial number of Rgelis
            width (float): Width of the space
            height (float): Height of the space
            background_color (str): Background color of the simulation
            fps (int): Frames per second for animation smoothness
        """
        self.width = width
        self.height = height
        self.bounds = (width, height)
        self.num_rgelis = num_rgelis
        self.background_color = background_color
        self.score = 0
        self.is_running = False
        self.fps = fps
        self.frame_interval = 1000 // fps  # Convert fps to milliseconds

        # Initialize Rgelis with random positions
        self.rgelis = [
            Rgeli(
                np.random.rand() * width,
                np.random.rand() * height,
                random.choice(Rgeli.COLORS),
                np.random.randint(50, 150)
            )
            for _ in range(num_rgelis)
        ]

        # Set up the plotting environment
        self.setup_plot()

    def setup_plot(self):
        """Set up the matplotlib figure and axes for visualization."""
        # Create figure with better DPI for smoother rendering and maximized window
        plt.rcParams['figure.figsize'] = [12, 8]
        plt.rcParams['figure.autolayout'] = True

        self.fig = plt.figure(figsize=(12, 8), dpi=120)
        # Set up to use the full screen
        mng = plt.get_current_fig_manager()
        try:
            mng.window.showMaximized()
        except:
            try:
                mng.resize(*mng.window.maxsize())
            except:
                try:
                    mng.frame.Maximize(True)
                except:
                    pass

        self.ax = self.fig.add_subplot(111)

        # Simple black background
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')

        # Create the scatter plot of Rgelis - use empty arrays if no Rgelis
        if len(self.rgelis) > 0:
            positions = [r.position for r in self.rgelis]
            colors = [r.color for r in self.rgelis]
            sizes = [r.size for r in self.rgelis]
        else:
            # Empty arrays for no Rgelis
            positions = []
            colors = []
            sizes = []

        self.scat = self.ax.scatter(
            # Extract x and y coordinates from positions
            [p[0] for p in positions] if positions else [],
            [p[1] for p in positions] if positions else [],
            c=colors,
            s=sizes,
            alpha=1.0,  # Fully opaque - no transparency
            edgecolors='white',
            linewidths=0.5,
            zorder=10
        )

        # NO glow effects - they create large transparent circles
        self.glow_effects = []

        # Set up score display
        self.score_text = self.ax.text(
            0.02, 0.98, f"Rgelis: {len(self.rgelis)}   Score: {self.score}",
            transform=self.ax.transAxes,
            color='yellow', fontsize=14, verticalalignment='top',
            fontweight='bold', family='monospace',
            bbox=dict(facecolor='black', alpha=1.0, pad=5, edgecolor=None),
            zorder=20
        )

        # Add click event handler
        self.fig.canvas.mpl_connect("button_press_event", self.on_click)

        # Add key press event handler for pausing/resuming
        self.fig.canvas.mpl_connect("key_press_event", self.on_key_press)

        # Configure axes
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_aspect('equal')

        # Add a title with instruction to click
        self.ax.set_title("Universe of Rgelis - Click to add Rgelis", color='white', fontsize=16)

        # Add a subtle glow effect as circles below the Rgelis
        self.glow_effects = []
        for r in self.rgelis:
            # Much smaller glow radius
            glow = plt.Circle(r.position, r.size / 150, color=r.color, alpha=0.3)
            self.ax.add_patch(glow)
            self.glow_effects.append(glow)

        # Set up score display with nicer font
        self.score_text = self.ax.text(
            0.02, 0.98, f"Rgelis: {len(self.rgelis)} | Score: {self.score}",
            transform=self.ax.transAxes,
            color='yellow', fontsize=14, verticalalignment='top',
            fontweight='bold', family='monospace',
            bbox=dict(facecolor='black', alpha=0.5, pad=5),
            zorder=20  # Make sure it's on top
        )

        # Add click event handler
        self.fig.canvas.mpl_connect("button_press_event", self.on_click)

        # Add key press event handler for pausing/resuming
        self.fig.canvas.mpl_connect("key_press_event", self.on_key_press)

        # Configure axes
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_aspect('equal')

        # Add a title with better styling
        self.ax.set_title("Universe of Rgelis", color='white', fontsize=18,
                          fontweight='bold', fontfamily='serif')

        # Add subtle gradient background for depth
        gradient = np.linspace(0, 1, 100)
        gradient = np.vstack((gradient, gradient))
        self.ax.imshow(gradient, aspect='auto', extent=[0, self.width, 0, self.height],
                       cmap=plt.cm.Blues, alpha=0.15, origin='lower')

        # Create the scatter plot of Rgelis with more appealing visual properties
        self.scat = self.ax.scatter(
            [r.position[0] for r in self.rgelis],
            [r.position[1] for r in self.rgelis],
            c=[r.color for r in self.rgelis],
            s=[r.size for r in self.rgelis],
            alpha=0.85,  # More vibrant colors
            edgecolors='white',
            linewidths=0.7,  # Slightly thicker outlines
            zorder=10  # Ensure Rgelis are above background
        )

        # Add a subtle glow effect as circles below the Rgelis
        self.glow_effects = []
        for r in self.rgelis:
            glow = plt.Circle(r.position, r.size / 50, color=r.color, alpha=0.2)
            self.ax.add_patch(glow)
            self.glow_effects.append(glow)

            # Set up score display with nicer font
        self.score_text = self.ax.text(
            0.02, 0.98, f"Rgelis: {len(self.rgelis)}   Score: {self.score}",
            transform=self.ax.transAxes,
            color='yellow', fontsize=14, verticalalignment='top',
            fontweight='bold', family='monospace',
            bbox=dict(facecolor='black', alpha=1.0, pad=5, edgecolor=None),
            zorder=20  # Make sure it's on top
        )

        # Add click event handler
        self.fig.canvas.mpl_connect("button_press_event", self.on_click)

        # Add key press event handler for pausing/resuming
        self.fig.canvas.mpl_connect("key_press_event", self.on_key_press)

        # Configure axes
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_aspect('equal')

        # Add a title with better styling
        self.ax.set_title("Universe of Rgelis", color='white', fontsize=18,
                          fontweight='bold', fontfamily='serif')

    def update_positions(self):
        """Update the positions and states of all Rgelis."""
        if not self.is_running:
            return

        # Skip updates if no Rgelis
        if not self.rgelis:
            return

        # Update each Rgeli - simple movement
        for rgeli in self.rgelis:
            rgeli.update_position(self.bounds)

        # Update the scatter plot with new positions
        self.scat.set_offsets([r.position for r in self.rgelis])

        # Color changes happen less frequently
        if random.random() < 0.1:  # 10% chance each frame
            for rgeli in self.rgelis:
                rgeli.change_color()
            # Update colors
            self.scat.set_color([r.color for r in self.rgelis])

        # Process interactions - check for score increases
        interaction_count = self.process_interactions()

        # Set exact sizes - no variation to avoid growth
        self.scat.set_sizes([r.size for r in self.rgelis])

        # Add new trails instead of glows - create a trail effect that follows each Rgeli
        trail_length = 5  # Number of trail segments

        for i, r in enumerate(self.rgelis):
            # Only create a trail for larger Rgelis to reduce visual clutter
            if r.size > 30 and random.random() < 0.2:  # Randomly create trails for 20% of eligible Rgelis
                # Create a very small trail dot
                trail = plt.Circle(r.position, r.size / 200, color=r.color, alpha=0.8)
                self.ax.add_patch(trail)
                self.glow_effects.append(trail)

        # Twinkle the stars in the background
        if hasattr(self, 'stars') and random.random() < 0.1:
            alpha_values = np.random.rand(100) * 0.3 + 0.1
            self.stars.set_alpha(alpha_values)

        # Update score display with more emphasis on the score
        current_score_text = f"Rgelis: {len(self.rgelis)}   Score: {self.score}"
        self.score_text.set_text(current_score_text)

    def process_interactions(self):
        """
        Process interactions between Rgelis.

        Returns:
            int: Number of interactions detected
        """
        interaction_count = 0

        # Skip if no Rgelis or only one Rgeli
        if len(self.rgelis) < 2:
            return 0

        # Check each pair of Rgelis using a simpler distance check
        for i, rgeli1 in enumerate(self.rgelis):
            for rgeli2 in self.rgelis[i + 1:]:
                # Simple distance check
                distance = np.linalg.norm(rgeli1.position - rgeli2.position)
                if distance < 0.5:  # Simple interaction threshold
                    interaction_count += 1

                    # Basic interaction - adjust velocities
                    direction = (rgeli1.position - rgeli2.position) / max(distance, 0.1)
                    rgeli1.velocity += direction * 0.1
                    rgeli2.velocity -= direction * 0.1

                    # Same color attracts, different colors repel
                    if rgeli1.color == rgeli2.color:
                        rgeli1.velocity -= direction * 0.05
                        rgeli2.velocity += direction * 0.05

        # Update score
        self.score += interaction_count

        # Update score display
        if interaction_count > 0:
            self.score_text.set_text(f"Rgelis: {len(self.rgelis)}   Score: {self.score}")

            # Small chance to spawn a new Rgeli
            if random.random() < 0.05:
                self.spawn_random_rgeli()

        return interaction_count

    def spawn_random_rgeli(self):
        """Spawn a new Rgeli at a random position."""
        new_rgeli = Rgeli(
            np.random.rand() * self.width,
            np.random.rand() * self.height,
            random.choice(Rgeli.COLORS),
            np.random.randint(15, 40)  # Smaller sizes
        )

        # Give it a strong initial velocity
        new_rgeli.velocity = (np.random.rand(2) - 0.5) * 0.5

        self.rgelis.append(new_rgeli)
        print(f"New Rgeli spawned! Total: {len(self.rgelis)}")

    def on_click(self, event):
        """Handle mouse click events to add new Rgelis."""
        if event.xdata is not None and event.ydata is not None:
            # Check if within bounds
            if 0 <= event.xdata <= self.width and 0 <= event.ydata <= self.height:
                # Add a new Rgeli at the click position
                size = np.random.randint(20, 60)  # Smaller size
                self.rgelis.append(
                    Rgeli(
                        event.xdata,
                        event.ydata,
                        random.choice(Rgeli.COLORS),
                        size
                    )
                )
                # Update score for adding a new Rgeli
                self.score += 10
                print(f"Added new Rgeli by clicking! +10 points. New score: {self.score}")

                # Update score display immediately
                if hasattr(self, 'score_text'):
                    self.score_text.set_text(f"Rgelis: {len(self.rgelis)}   Score: {self.score}")

    def on_key_press(self, event):
        """Handle keyboard events."""
        if event.key == ' ':  # Space bar
            # Toggle pause/resume
            self.is_running = not self.is_running
            pause_status = "Paused" if not self.is_running else "Running"
            self.ax.set_title(f"Universe of Rgelis - {pause_status}", color='white', fontsize=18,
                              fontweight='bold', fontfamily='serif')
        elif event.key == 'c':  # Clear all
            # Clear all Rgelis
            self.rgelis = []
            self.score = 0

            # Force redraw of the scatter plot with empty data
            self.scat.set_offsets(np.zeros((0, 2)))  # Use empty numpy array of correct shape
            self.scat.set_sizes([])
            self.scat.set_color([])

            # Clear all glow effects
            for glow in self.glow_effects:
                try:
                    glow.remove()
                except:
                    pass
            self.glow_effects = []

            # Update score display
            if hasattr(self, 'score_text'):
                self.score_text.set_text(f"Rgelis: 0   Score: 0")

            print("Cleared all Rgelis and reset score to 0")

        elif event.key == 'a':  # Add 5 random Rgelis
            for _ in range(5):
                self.spawn_random_rgeli()
            print(f"Added 5 random Rgelis. Total: {len(self.rgelis)}")

    def animate(self, frame):
        """Animation function for matplotlib's FuncAnimation."""
        # Update all positions and effects
        self.update_positions()

        # Force a redraw of text elements
        if hasattr(self, 'score_text'):
            self.score_text.set_text(f"Rgelis: {len(self.rgelis)} | Score: {self.score}")

        # For non-blitting animation, we don't need to return anything
        # This ensures the entire figure is redrawn properly
        return []

    def run(self):
        """Run the simulation."""
        # Force running state
        self.is_running = True

        # Very basic animation setup - focus on reliability
        self.ani = animation.FuncAnimation(
            self.fig,
            self.animate_frame,  # Use a proper method instead of lambda
            interval=50,  # 20 fps - reliable refresh rate
            blit=False,  # Don't use blitting - more reliable
            cache_frame_data=False  # Explicitly disable caching to avoid warning
        )

        # Add controls text
        plt.figtext(0.5, 0.01,
                    "Controls: Click to add Rgeli | Space to pause | 'c' to clear | 'a' to add 5 random Rgelis",
                    ha="center", color="white", fontsize=10)

        plt.show()

    def animate_frame(self, frame):
        """Animation function that safely handles the empty initial state."""
        try:
            # Only update positions if there are Rgelis
            if self.rgelis:
                self.update_positions()
        except Exception as e:
            print(f"Error in animation: {e}")

        # Return empty list for non-blitting animation
        return []