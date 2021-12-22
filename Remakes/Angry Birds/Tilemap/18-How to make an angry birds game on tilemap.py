"""
Angry birds(Remake) Tilemap version
"""

"""Instrutions:

1: Click to launch a Angry Bird
2: Take down the pigs with birds
3: Random Bird Launcher
4: Can only launch 5 birds
5: Randomise the box steps
6: Have Fun
7: Made With Tilemap(Inprogress)

"""
# Imports


# Screen setup
import arcade
import random
import math
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Angry Birds"

# Scale
SCALE = 0.5

# Bullet Speed
BULLET_SPEED = 30

# Gravity
GRAVITY = 1500

# Damping - Amount of speed lost per second
DEFAULT_DAMPING = 1.0

# Friction between objects
WALL_FRICTION = 0.7
DYNAMIC_ITEM_FRICTION = 0.6


class Game(arcade.Window):
    """Game"""

    def __init__(self):
        """Init"""

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Our physics enginea
        self.physics_engine = None

        # Lists
        self.wall_list = None
        self.item_list = None

    def setup(self):
        """Setup"""

        arcade.set_background_color(arcade.color.BLUE_YONDER)

        # Player Setup
        self.player = arcade.Sprite("images/ClassicChuck2.png", SCALE)

        # Player Start X and Y
        self.player.center_x = 200
        self.player.center_y = 200

        # Player's change X and Y
        self.player.change_x = 0
        self.player.change_y = 0

        # Angry Bird Count
        self.angry_bird_count = 0

        # Map name
        map_name = "maps/AngryBird_level_1.json"

        # Load in TileMap
        tile_map = arcade.load_tilemap(map_name, SCALE)

        # Pull the sprite layers out of the tile map
        self.wall_list = tile_map.sprite_lists["Platform"]
        self.item_list = tile_map.sprite_lists["Boxes"]

        # --- Pymunk Physics Engine Setup ---

        # The default damping for every object controls the percent of velocity
        # the object will keep each second. A value of 1.0 is no speed loss,
        # 0.9 is 10% per second, 0.1 is 90% per second.
        # For top-down games, this is basically the friction for moving objects.
        # For platformers with gravity, this should probably be set to 1.0.
        # Default value is 1.0 if not specified.
        damping = DEFAULT_DAMPING

        # Set the gravity. (0, 0) is good for outer space and top-down.
        gravity = (0, -GRAVITY)

        # Create the physics engine
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping,
                                                         gravity=gravity)

        # Create the walls.
        # By setting the body type to PymunkPhysicsEngine.STATIC the walls can't
        # move.
        # Movable objects that respond to forces are PymunkPhysicsEngine.DYNAMIC
        # PymunkPhysicsEngine.KINEMATIC objects will move, but are assumed to be
        # repositioned by code and don't respond to physics forces.
        # Dynamic is default.
        self.physics_engine.add_sprite_list(self.wall_list,
                                            friction=WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

        # Create the items
        self.physics_engine.add_sprite_list(self.item_list,
                                            friction=DYNAMIC_ITEM_FRICTION,
                                            collision_type="item")

    def on_update(self, delta_time):
        """Update"""

        pass

    def on_draw(self):
        """Draw"""

        arcade.start_render()

        self.item_list.draw()
        self.wall_list.draw()


if __name__ == "__main__":
    window = Game()
    window.setup()
    arcade.run()
