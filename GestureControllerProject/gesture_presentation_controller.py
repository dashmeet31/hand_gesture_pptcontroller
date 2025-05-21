import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands and drawing utils
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Initialize pyautogui FAILSAFE off for edge gestures
pyautogui.FAILSAFE = False

# Set up webcam
cap = cv2.VideoCapture(0)

# Configure hand detection
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
prev_action_time = 0  # cooldown timer

while True:
    success, img = cap.read()
    if not success:
        break

    # Flip the image for natural (mirror) interaction
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect hands
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks on the image
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            # Detect index and middle finger horizontal positions
            if len(lm_list) >= 12:
                index_x = lm_list[8][0]
                middle_x = lm_list[12][0]
                current_time = time.time()

                if abs(index_x - middle_x) > 40 and current_time - prev_action_time > 1:
                    if index_x > middle_x:
                        pyautogui.press("right")
                        cv2.putText(img, "Next Slide", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                    1.2, (0, 255, 0), 3)
                    else:
                        pyautogui.press("left")
                        cv2.putText(img, "Previous Slide", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                    1.2, (0, 255, 0), 3)
                    prev_action_time = current_time

    # Display the image
    cv2.imshow("Gesture Controlled Presentation", img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
