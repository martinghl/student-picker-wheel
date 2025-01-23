import tkinter as tk
from tkinter import font
import random
import math
from spinner import WheelSpinner

class WheelOfFortuneGUI:
    def __init__(self, names):
        """
        Create a modernized wheel-of-fortune style GUI for name selection.
        :param names: List of strings with each student's full name.
        """
        self.names = names
        self.spinner = WheelSpinner(self.names)

        # Create the main application window
        self.root = tk.Tk()
        self.root.title("🎡 Spinning Wheel - Student Picker")
        self.root.geometry("700x700")
        self.root.config(bg="#F7F9FC")

        # Title label with a modern font
        title_font = font.Font(family="Verdana", size=20, weight="bold")
        self.title_label = tk.Label(
            self.root,
            text="🎡 Student Picker",
            bg="#F7F9FC",
            fg="#2C3E50",
            font=title_font
        )
        self.title_label.pack(pady=20)

        # Create a canvas for the spinning wheel
        self.canvas_size = 600
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, height=self.canvas_size, bg="#F7F9FC", highlightthickness=0)
        self.canvas.pack(pady=10)

        # Modern Spin button
        self.spin_button = tk.Button(
            self.root,
            text="🎲 SPIN",
            command=self.start_spin,
            font=("Verdana", 14, "bold"),
            fg="white",
            bg="#3498DB",
            activebackground="#2980B9",
            activeforeground="white",
            width=12,
            relief="groove"
        )
        self.spin_button.pack(pady=20)

        # Winner label
        self.winner_label = tk.Label(
            self.root,
            text="",
            bg="#F7F9FC",
            fg="#34495E",
            font=("Verdana", 14, "bold")
        )
        self.winner_label.pack(pady=10)

        # Precompute pastel colors for segments
        self.colors = self._generate_colors(len(self.names))

        # Start the animation loop for the wheel
        self.update_wheel()

    def _generate_colors(self, n):
        """Generate n random pastel colors."""
        colors = []
        for _ in range(n):
            r = random.randint(100, 255)
            g = random.randint(100, 255)
            b = random.randint(100, 255)
            colors.append(f"#{r:02x}{g:02x}{b:02x}")
        return colors

    def start_spin(self):
        """Start the spinner."""
        self.winner_label.config(text="🎯 Spinning...")
        self.spinner.start_spin()

    def update_wheel(self):
        """The main animation loop for updating the wheel display."""
        self.spinner.spin_step()
        self.canvas.delete("all")
        self.draw_wheel()
        self.draw_pointer()

        # If the spinner has stopped, display the winner
        if not self.spinner.is_spinning():
            winner = self.spinner.get_winner_name()
            if winner != "No Names":
                self.winner_label.config(text=f"🏆 Winner: {winner}")

        self.root.after(16, self.update_wheel)

    def draw_wheel(self):
        """Draw the spinning wheel with names and colors."""
        if not self.names:
            return

        cx, cy = self.canvas_size // 2, self.canvas_size // 2
        radius = self.canvas_size // 2 - 20
        arc_extent = self.spinner.arc_extent
        offset = self.spinner.offset_angle

        for i, name in enumerate(self.names):
            start_angle = offset + i * arc_extent
            color = self.colors[i]
            self.canvas.create_arc(
                cx - radius, cy - radius,
                cx + radius, cy + radius,
                start=start_angle,
                extent=arc_extent,
                fill=color,
                outline="white",
                width=3
            )

            mid_angle = math.radians(start_angle + arc_extent / 2)
            text_radius = radius * 0.75
            text_x = cx + text_radius * math.cos(mid_angle)
            text_y = cy - text_radius * math.sin(mid_angle)

            self.canvas.create_text(
                text_x, text_y,
                text=name,
                fill="#2C3E50",
                font=("Verdana", 10, "bold")
            )

    def draw_pointer(self):
        """Draw a sleek pointer at the top of the wheel."""
        cx = cy = self.canvas_size // 2
        pointer_length = 40
        self.canvas.create_polygon(
            cx, cy - (self.canvas_size // 2) + 10,
            cx - 15, cy - (self.canvas_size // 2) + pointer_length,
            cx + 15, cy - (self.canvas_size // 2) + pointer_length,
            fill="#E74C3C",
            outline="black"
        )

    def run(self):
        """Run the Tkinter event loop."""
        self.root.mainloop()
