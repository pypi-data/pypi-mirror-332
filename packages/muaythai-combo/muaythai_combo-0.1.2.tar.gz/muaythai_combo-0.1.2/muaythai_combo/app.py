import tkinter as tk
import random

# List of Muay Thai combinations.
COMBINATIONS = [
    "Jab, cross",
    "Jab, cross, jab, cross",
    "Jab, cross, hook",
    "Jab, cross, hook, cross",
    "Jab, jab, cross",
    "Jab, cross, lead body hook",
    "Fake jab, cross, lead hook",
    "Lead up elbow, rear side elbow",
    "Lead side elbow, rear up elbow",
    "Jab, lead up elbow, rear side elbow",
    "Jab, cross, lead side elbow, rear up elbow ",
    "Jab, cross, lead side elbow, rear up elbow ",
    "Jab, cross, hook, rear swing kick",
    "Jab, rear swing kick",
    "Jab, cross, switch lead kick",
    "Cross, switch lead kick",
    "Cross, hook, rear swing kick",
    "Hook, cross, lead swing kick",
    "Jab, jab, cross, swing kick",
    "Jab, lead uppercut, cross, switch kick",
    "Jab, body cross, lead hook, low kick",
    "Lead teep, rear swing kick, rear swing kick",
    "Rear swing kick, lead teep",
    "Cross, switch kick, switch kick",
    "Jab, rear low kick",
    "Jab, cross, hook, low kick",
    "Cross, hook, low kick",
    "Jab-hook, low kick",
    "Rear upper, hook, low kick",
    "Jab, lead teep, jab, fake lead teep, elbow",
    "Jab, rear swing kick, lead teep",
    "Teep, fake teep, rear swing kick",
    "Jab, lead teep, rear face teep",
    "Swing kick, fake swing kick, rear teep",
    "Cross, rear knee",
    "Jab, switch knee",
    "Jab, cross, switch knee",
    "Left hook rear knee",
    "Cross, hook, rear knee",
    "Lead teep, fake lead teep, rear knee",
    "Rear swing kick, cross",
    "Switch kick, cross",
    "Switch kick, cross, hook, low kick",
    "Lead push kick, rear swing kick",
    "Rear push kick, lead swing kick",
]

# New list of single attacks.
SINGLE_ATTACKS = [
    "Jab",
    "Cross",
    "Lead Hook",
    "Rear Hook",
    "Lead Uppercut",
    "Rear Uppercut",
    "Lead body hook",
    "Rear body hook",
    "Rear up elbow",
    "Lead up elbow",
    "Rear side elbow",
    "Lead side elbow",
    "Rear swing kick",
    "Lead swing kick (switch kick)",
    "Rear low kick",
    "Lead low kick",
    "Rear teep",
    "Lead teep",
    "Rear knee",
    "Lead knee (switch knee)",
]


def contains_any(s, words):
    """Check if string s contains any of the words in the list."""
    return any(word in s for word in words)


def no_kick_combos():
    """Exclude combinations with any type of kick or teep."""
    disallowed = ["kick"]
    return [combo for combo in COMBINATIONS if not contains_any(combo.lower(), disallowed)]


def low_kick_only_combos():
    """
    Include combos that contain "low kick" but exclude other kick types.
    """
    disallowed = ["swing kick", "switch kick", "lead kick", "push kick"]
    result = []
    for combo in COMBINATIONS:
        lower = combo.lower()
        if "low kick" in lower and not contains_any(lower, disallowed):
            result.append(combo)
    return result


class MuayThaiApp:
    def __init__(self, master):
        self.master = master
        master.title("Muay Thai Combo Generator")

        # Variable for mode selection: "all", "no_kicks", "low_kicks_only", or "random_single"
        self.mode = tk.StringVar(value="all")

        # Label for displaying the combo.
        self.combo_label = tk.Label(
            master, text="", font=("Helvetica", 24, "bold"), wraplength=600
        )
        self.combo_label.pack(pady=20)

        # Frame for radio buttons (mode selection).
        mode_frame = tk.Frame(master)
        tk.Radiobutton(
            mode_frame, text="All", variable=self.mode, value="all"
        ).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(
            mode_frame, text="No kicks", variable=self.mode, value="no_kicks"
        ).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(
            mode_frame,
            text="Low kicks only",
            variable=self.mode,
            value="low_kicks_only",
        ).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(
            mode_frame,
            text="Random Single",
            variable=self.mode,
            value="random_single",
        ).pack(side=tk.LEFT, padx=5)
        mode_frame.pack()

        # Frame for auto-generation controls.
        control_frame = tk.Frame(master)
        tk.Label(
            control_frame, text="Number of combos (0 = infinite):"
        ).grid(row=0, column=0, padx=5, sticky=tk.E)
        self.num_entry = tk.Entry(control_frame, width=5)
        self.num_entry.insert(0, "0")
        self.num_entry.grid(row=0, column=1, padx=5)
        tk.Label(
            control_frame, text="Interval (seconds):"
        ).grid(row=0, column=2, padx=5, sticky=tk.E)
        self.interval_entry = tk.Entry(control_frame, width=5)
        self.interval_entry.insert(0, "3")
        self.interval_entry.grid(row=0, column=3, padx=5)
        control_frame.pack(pady=10)

        # Frame for maximum number of single attacks (only used in Random Single mode).
        single_frame = tk.Frame(master)
        tk.Label(single_frame, text="Max single attacks:").pack(
            side=tk.LEFT, padx=5
        )
        self.max_attack_entry = tk.Entry(single_frame, width=5)
        self.max_attack_entry.insert(0, "3")
        self.max_attack_entry.pack(side=tk.LEFT, padx=5)
        single_frame.pack(pady=10)

        # Buttons for manual and auto update.
        btn_frame = tk.Frame(master)
        tk.Button(
            btn_frame, text="New Combo", command=self.update_combo
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            btn_frame,
            text="Start Auto Generation",
            command=self.start_auto,
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            btn_frame,
            text="Stop Auto Generation",
            command=self.stop_auto,
        ).pack(side=tk.LEFT, padx=5)
        btn_frame.pack(pady=10)

        self.after_id = None
        self.auto_count = 0
        self.max_count = 0

        # Initial update.
        self.update_combo()

    def generate_single_combo(self):
        """Generate a random combo of single attacks."""
        try:
            max_attacks = int(self.max_attack_entry.get())
            max_attacks = max(1, max_attacks)
        except ValueError:
            max_attacks = 3
        n = random.randint(1, max_attacks)
        return ", ".join(random.choice(SINGLE_ATTACKS) for _ in range(n))

    def get_combos(self):
        """Get the list of combinations based on the selected mode."""
        mode = self.mode.get()
        if mode == "no_kicks":
            combos = no_kick_combos()
        elif mode == "low_kicks_only":
            combos = low_kick_only_combos()
        else:
            combos = COMBINATIONS
        return combos

    def update_combo(self):
        """Update the displayed combo."""
        if self.mode.get() == "random_single":
            combo = self.generate_single_combo()
        else:
            combos = self.get_combos()
            if combos:
                combo = random.choice(combos)
            else:
                combo = "No available combinations for this mode."
        self.combo_label.config(text=combo)

    def auto_update(self):
        """Automatically update combos based on the interval."""
        if self.max_count > 0:
            if self.auto_count >= self.max_count:
                self.after_id = None
                return
            self.auto_count += 1

        self.update_combo()
        try:
            interval = float(self.interval_entry.get()) * 1000  # Convert seconds to ms.
        except ValueError:
            interval = 3000
        self.after_id = self.master.after(int(interval), self.auto_update)

    def start_auto(self):
        """Start the automatic combo update."""
        try:
            num = int(self.num_entry.get())
        except ValueError:
            num = 0
        self.max_count = num if num > 0 else 0
        self.auto_count = 0
        if self.after_id:
            self.master.after_cancel(self.after_id)
        self.auto_update()

    def stop_auto(self):
        """Stop the automatic combo update."""
        if self.after_id:
            self.master.after_cancel(self.after_id)
            self.after_id = None


def main():
    """Initialize and run the Muay Thai combo generator application."""
    root = tk.Tk()
    app = MuayThaiApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
