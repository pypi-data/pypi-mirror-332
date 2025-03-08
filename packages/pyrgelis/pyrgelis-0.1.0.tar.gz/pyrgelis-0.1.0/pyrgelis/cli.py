"""
Command-line interface for the PyRgelis package.
"""

import argparse
from .game import RgelisGame

def print_welcome_message():
    """Print the welcome message to the console."""
    print("""
    =====================================================
    Welcome to the Universe of Rgelis!
    =====================================================
    
    Far beyond the known realms of physics and reason, 
    there exists a surreal, dreamlike world where the 
    Rgelis drift eternally. These enigmatic, jellyfish-like 
    beings float through the ethereal currents of their 
    dimension, changing colors as they react to unseen 
    cosmic forces.
    
    Each Rgeli has a personality of its own, propelled by
    whimsical movements and ever-shifting hues. No one truly
    knows their purpose, but some say they are echoes of
    forgotten thoughts, living in an endless dance across
    the fabric of space.
    
    You can summon new Rgelis by clicking on their domain,
    expanding their vibrant, mysterious existence. Observe
    their behavior, watch them change, and immerse yourself
    in the strange beauty of their world.
    
    Controls:
    - Click: Create a new Rgeli at that position
    - Space: Pause/Resume the simulation
    - 'c': Clear all Rgelis
    - 'a': Add 5 random Rgelis
    =====================================================
    """)

def main():
    """Main entry point for the command-line interface."""
    parser = argparse.ArgumentParser(
        description="PyRgelis - A mesmerizing simulation of jellyfish-like creatures."
    )

    parser.add_argument(
        "--count", "-c",
        type=int,
        default=0,  # Changed default to 0
        help="Initial number of Rgelis (default: 0)"
    )

    parser.add_argument(
        "--width", "-w",
        type=float,
        default=10,
        help="Width of the space (default: 10)"
    )

    parser.add_argument(
        "--height", "-H",
        type=float,
        default=10,
        help="Height of the space (default: 10)"
    )

    parser.add_argument(
        "--background", "-b",
        type=str,
        default="black",
        help="Background color (default: black)"
    )

    parser.add_argument(
        "--fps", "-f",
        type=int,
        default=60,
        help="Frames per second for animation smoothness (default: 60)"
    )

    parser.add_argument(
        "--no-welcome",
        action="store_true",
        help="Skip the welcome message"
    )

    args = parser.parse_args()

    if not args.no_welcome:
        print_welcome_message()

    # Create and run the game
    game = RgelisGame(
        num_rgelis=args.count,
        width=args.width,
        height=args.height,
        background_color=args.background,
        fps=args.fps
    )

    game.run()

if __name__ == "__main__":
    main()