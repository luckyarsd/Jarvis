import tkinter as tk
from tkinter import simpledialog, messagebox
import cv2
import mediapipe as mp
import time
import webbrowser
import csv
from PIL import Image, ImageTk

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the camera
cap = cv2.VideoCapture(0)

class PalmDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Edith [AI assistant]")
        self.root.geometry("800x600")

        self.video_label = tk.Label(root)
        self.video_label.pack()

        self.start_button = tk.Button(root, text="Start Detection", command=self.start_detection)
        self.start_button.pack(pady=50)

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_app)
        self.quit_button.pack(pady=50)

        self.status_label = tk.Label(root, text="Status: Waiting for detection")
        self.status_label.pack(pady=50)

        self.palm_detected = False
        self.start_time = time.time()
        self.update_frame()

    def update_frame(self):
        ret, frame = cap.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                    if wrist:
                        self.palm_detected = True
                        break

            # Convert frame to ImageTk format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img_tk = ImageTk.PhotoImage(image=img)

            self.video_label.img_tk = img_tk
            self.video_label.configure(image=img_tk)

            if time.time() - self.start_time > 5:
                self.handle_detection()
            else:
                self.root.after(10, self.update_frame)  # Update every 10 ms

    def handle_detection(self):
        if self.palm_detected:
            self.status_label.config(text="Status: Welcome Boss! Choose a bot.")
            self.show_bot_options()
        else:
            self.status_label.config(text="Status: Identification Failed. Try again.")
            cap.release()
            cv2.destroyAllWindows()

    def show_bot_options(self):
        choice = simpledialog.askstring("Bot Selection", "Bots [Veronica, Jarvis, Friday]:")

        if choice:
            if choice.lower() == "veronica":
                self.handle_veronica()
            elif choice.lower() == "jarvis":
                self.handle_edith()
            elif choice.lower() == "friday":
                self.handle_friday()
            else:
                messagebox.showinfo("Info", f"{choice} bot not available.")

    def handle_veronica(self):
        query = simpledialog.askstring("Veronica", "What do you want to learn today , Boss :")
        if query:
            url = f"https://www.w3schools.com/{query}"
            webbrowser.open(url)

    def handle_edith(self):
        location = simpledialog.askstring("Edith", "where you want to go , Boss :")
        if location:
            base_url = "https://www.google.com/maps/search/"
            query = f"{location}/@current+location"
            webbrowser.open(base_url + query)

    def handle_friday(self):
        social_media_name = simpledialog.askstring("Friday", "Which social media's password you want , Boss : ")
        if social_media_name:
            password = self.get_password(social_media_name)
            messagebox.showinfo("Friday", f"Password for {social_media_name} is: {password}")

    def get_password(self, social_media_name):
        try:
            with open('social_media_passwords.csv', mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if row['social_media'].lower() == social_media_name.lower():
                        return row['password']
                return "Social media name not found."
        except FileNotFoundError:
            return "Password file not found."

    def start_detection(self):
        self.start_time = time.time()
        self.palm_detected = False
        self.update_frame()

    def quit_app(self):
        cap.release()
        cv2.destroyAllWindows()
        self.root.destroy()

# Initialize and run the application
root = tk.Tk()
app = PalmDetectionApp(root)
root.mainloop()
