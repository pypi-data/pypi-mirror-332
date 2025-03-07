import tkinter as tk
from tkinter import messagebox, ttk
import time
import datetime
import os
import subprocess


class AlarmClock:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Spotify Alarm Clock")
        self.window.geometry("400x500")
        self.window.configure(bg="#2C2F33")  # Dark gray background
        self.window.resizable(False, False)

        # Style configuration
        style = ttk.Style()
        style.theme_use("clam")  # Modern theme
        style.configure("TButton", font=("Helvetica", 12), padding=10, background="#7289DA", foreground="white")
        style.map("TButton", background=[("active", "#99AAB5")])
        style.configure("TLabel", background="#2C2F33", foreground="white", font=("Helvetica", 12))

        # Main frame
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill="both", expand=True)

        # Time label
        self.time_label = ttk.Label(main_frame, text="", font=("Helvetica", 36, "bold"), foreground="#FFFFFF")
        self.time_label.pack(pady=(0, 20))

        # Input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill="x", pady=10)

        # Hour entry
        ttk.Label(input_frame, text="Hour (24h):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.hour_entry = ttk.Entry(input_frame, width=5, font=("Helvetica", 12), justify="center")
        self.hour_entry.grid(row=0, column=1, padx=5, pady=5)

        # Minute entry
        ttk.Label(input_frame, text="Minute:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.minute_entry = ttk.Entry(input_frame, width=5, font=("Helvetica", 12), justify="center")
        self.minute_entry.grid(row=1, column=1, padx=5, pady=5)

        # Spotify URI entry
        ttk.Label(input_frame, text="Spotify URI:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.spotify_uri_entry = ttk.Entry(input_frame, width=30, font=("Helvetica", 12))
        self.spotify_uri_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)

        # Set alarm button
        self.set_button = ttk.Button(button_frame, text="Set Alarm", command=self.set_initial_alarm)
        self.set_button.pack(side="left", padx=10)

        # Stop alarm button
        self.stop_button = ttk.Button(button_frame, text="Stop Alarm", command=self.stop_alarm, state="disabled")
        self.stop_button.pack(side="left", padx=10)

        # Status label
        self.status_label = ttk.Label(main_frame, text="Alarm not set", font=("Helvetica", 12, "italic"),
                                      foreground="#99AAB5")
        self.status_label.pack(pady=10)

        # Decorative separator
        ttk.Separator(main_frame, orient="horizontal").pack(fill="x", pady=20)

        # App title or footer
        ttk.Label(main_frame, text="Spotify Alarm Clock", font=("Helvetica", 14, "bold"), foreground="#7289DA").pack()

        self.alarm_active = False
        self.is_hourly = False
        self.next_alarm_time = None
        self.spotify_uri = None

        self.update_time()
        self.window.mainloop()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)

        if self.alarm_active and datetime.datetime.now() >= self.next_alarm_time:
            self.trigger_alarm()

        self.window.after(1000, self.update_time)

    def set_initial_alarm(self):
        try:
            hour = int(self.hour_entry.get())
            minute = int(self.minute_entry.get())
            spotify_input = self.spotify_uri_entry.get().strip()

            # Convert URL to URI if needed
            if spotify_input.startswith("https://open.spotify.com/track/"):
                track_id = spotify_input.split("/track/")[1].split("?")[0]
                self.spotify_uri = f"spotify:track:{track_id}"
            elif spotify_input.startswith("spotify:track:"):
                self.spotify_uri = spotify_input
            else:
                raise ValueError("Please enter a valid Spotify track URL or URI")

            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError

            now = datetime.datetime.now()
            self.next_alarm_time = datetime.datetime(now.year, now.month, now.day, hour, minute)

            if self.next_alarm_time <= now:
                self.next_alarm_time += datetime.timedelta(days=1)

            self.alarm_active = True
            self.set_button.config(state="disabled")
            self.stop_button.config(state="normal")
            self.status_label.config(text=f"Alarm set for {hour:02d}:{minute:02d} with Spotify")

        except ValueError as e:
            messagebox.showerror("Error",
                                 "Please enter valid time (Hour: 0-23, Minute: 0-59) and a Spotify track URL or URI")

    def stop_alarm(self):
        self.alarm_active = False
        self.is_hourly = False
        self.next_alarm_time = None
        self.set_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.status_label.config(text="Alarm stopped")
        subprocess.run(['osascript', '-e', 'tell application "Spotify" to pause'])  # Stop Spotify playback

    def set_next_hourly_alarm(self):
        self.next_alarm_time += datetime.timedelta(hours=1)
        self.status_label.config(text=f"Next hourly alarm at {self.next_alarm_time.strftime('%H:%M')}")

    def trigger_alarm(self):
        # Play Spotify URI using AppleScript with proper quoting
        applescript = f'tell application "Spotify" to play track "{self.spotify_uri}"'
        try:
            subprocess.run(['osascript', '-e', applescript], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to play Spotify track: {e}")
            return

        messagebox.showinfo("Alarm", f"Alarm triggered at {datetime.datetime.now().strftime('%H:%M')}")

        if not self.is_hourly:
            response = messagebox.askyesno("Hourly Alarm", "Would you like this alarm to repeat hourly?")
            if response:
                self.is_hourly = True
                self.set_next_hourly_alarm()
            else:
                self.stop_alarm()
        elif self.is_hourly and self.alarm_active:
            self.set_next_hourly_alarm()


def main():
    """Entry point for the command-line script."""
    app = AlarmClock()
    app.run()

if __name__ == "__main__":
    main()