import cv2
import mediapipe as mp
import time
import webbrowser
from colorama import Fore, Back, Style, init
import csv

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the camera
cap = cv2.VideoCapture(0)

# Start time
start_time = time.time()
palm_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Check if the palm is detected (using the wrist landmark)
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            if wrist:
                palm_detected = True
                break

    # Check if 5 seconds have passed
    if time.time() - start_time > 5:
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Check if the palm was detected within 5 seconds
if palm_detected:
    print("HELLO , BOSS!")

else:
    print(Style.RESET_ALL + "Identification failed")
    print("Informing Boss...")

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

if palm_detected:
    print(Fore.RED +"---------------AI bots Availbale---------------")
    print(Style.RESET_ALL + "1. Veronica [Education specialist bot]")
    print("2. Edith [Navigation specialist bot]")
    print("3. Friday [My personal assistant]")

    while (True):
        choice = input("Select a bot: ")
        if (choice.lower() == "veronica"):
            print("Hello , BOSS ! \nI am 'Veronica' your educational bot.")
            def search_and_open(query):
                url = "https://www.w3schools.com/" + query
                webbrowser.open(url)
            query = input("Enter topic to learn today: ")
            search_and_open(query)

        # Edith
        elif (choice.lower() == "edith"):
            print("Hello , BOSS ! \nI am 'Edith' your navigational bot.")
            def open_google_maps_search(place):
                base_url = "https://www.google.com/maps/search/"
                query = f"{place}/@current+location"
                webbrowser.open(base_url + query)
            location = input("Enter place to go: ")
            open_google_maps_search(location)

        # Friday
        elif (choice.lower() == "friday"):
            print("Hello , BOSS ! \nI am 'Friday' your personal assistant.")
            def get_password(social_media_name):
                with open('social_media_passwords.csv', mode='r') as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        if row['social_media'].lower() == social_media_name.lower():
                            return row['password']
                    return "Social media name not found."
            print("Get your's personal passwords...")
            social_media_name = input("Enter the social media name: ")
            password = get_password(social_media_name)
            print(f"The password for {social_media_name} is: {password}")

        else:
            print(choice, " bot not available.")

        # Break condition
        ch = input("Want to continue Y/N: ")
        if (ch.lower() == 'y'):
            continue
        else:
            break






