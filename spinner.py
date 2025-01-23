# spinner.py
import random

class WheelSpinner:
    def __init__(self, names):
        """
        A wheel spinner for a list of names.
        :param names: List of strings, e.g. ["John Smith", "Jane Doe", ...]
        """
        self.names = names
        self.num_segments = len(names)
        self.arc_extent = 360 / self.num_segments if self.num_segments else 0
        
        # The spinning state
        self.offset_angle = 0.0   # Current rotation angle of the wheel (degrees)
        self.spin_speed = 0.0     # Current speed of rotation (degrees per update)
        self.friction = 0.97      # Slowdown factor per update
        self.spinning = False     # Whether the wheel is currently spinning

        # The pointer angle is fixed at 90 deg (12 o'clock in Tkinter's coordinate system)
        # We just need to figure out which segment lines up with that angle.

    def start_spin(self):
        """
        Start a new spin with some random initial speed.
        """
        if self.num_segments == 0:
            return
        self.spin_speed = random.uniform(20, 30)  # Initial spin speed
        self.spinning = True

    def spin_step(self):
        """
        Advance the wheel by one animation 'tick':
         - offset_angle changes by spin_speed
         - spin_speed is reduced by friction
        """
        if not self.spinning or self.num_segments == 0:
            return

        self.offset_angle += self.spin_speed
        # Keep angle in [0..360) range to avoid large numbers
        self.offset_angle %= 360

        self.spin_speed *= self.friction

        # If speed is below a threshold, consider it stopped
        if abs(self.spin_speed) < 0.2:
            self.spin_speed = 0
            self.spinning = False

    def is_spinning(self):
        """Returns True if the wheel is still spinning."""
        return self.spinning

    def get_segment_index(self, angle):
        """
        Given an angle in [0..360), find which segment (index in [0..num_segments-1])
        that angle belongs to.
        """
        if self.num_segments == 0:
            return -1
        # Each segment covers arc_extent degrees, from i*arc_extent to (i+1)*arc_extent
        # But we’ll do mod 360 just to be safe.
        angle %= 360
        index = int(angle // self.arc_extent)
        # Ensure index does not exceed num_segments-1 due to float rounding
        if index >= self.num_segments:
            index = self.num_segments - 1
        return index

    def get_winner_name(self):
        """
        Identify which name is pointed at by the pointer (which we fix at 90 deg).
        The wheel is offset by offset_angle, so the pointer effectively sees angle
        = (pointerAngle - offset_angle) mod 360 in the wheel's coordinate system.
        """
        if self.num_segments == 0:
            return "No Names"

        pointer_angle = 90.0
        effective_angle = (pointer_angle - self.offset_angle) % 360
        i = self.get_segment_index(effective_angle)
        return self.names[i]
