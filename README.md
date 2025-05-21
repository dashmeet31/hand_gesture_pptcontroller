# 👋 Gesture Controlled Presentation using Python

This project allows you to control your PowerPoint or any slideshow presentation using hand gestures detected through a webcam. It's built using **OpenCV**, **MediaPipe**, and **PyAutoGUI**.

## 📽️ Demo

> Control your slides with simple hand gestures — swipe right or left with your index and middle fingers to move between slides!

## 🧠 How It Works

* The program uses your **webcam** to detect your hand in real-time.
* It identifies the positions of your **index and middle fingers** using **MediaPipe** hand tracking.
* If the index and middle fingers are spread apart significantly, it detects the direction of movement and simulates:

  * **Right arrow key** (➡️) for next slide.
  * **Left arrow key** (⬅️) for previous slide.

## 🛠️ Technologies Used

| Library   | Purpose                           |
| --------- | --------------------------------- |
| OpenCV    | Video capturing and display       |
| MediaPipe | Real-time hand landmark detection |
| PyAutoGUI | Simulate keyboard presses         |
| Time      | Gesture cooldown timing mechanism |

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed (3.7+ recommended).

### Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

### Run the Project

```bash
python gesture_presentation.py
```

### Controls

| Gesture                                                 | Action           |
| ------------------------------------------------------- | ---------------- |
| Move **index finger** to the **right** of middle finger | Next slide       |
| Move **index finger** to the **left** of middle finger  | Previous slide   |
| Press **q** key                                         | Quit the program |

> ✅ To avoid accidental repeated gestures, a **1-second cooldown** is added after every gesture detection.

## 📌 Notes

* Works best in a **well-lit environment**.
* Only detects **one hand** at a time (`max_num_hands=1`).
* You may need to adjust the threshold (`abs(index_x - middle_x) > 40`) based on your webcam resolution and distance.

## 📷 Screenshots

| Hand Landmarks                                    | Next Slide                                   | Previous Slide                               |
| ------------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| ![landmarks](https://via.placeholder.com/200x120) | ![next](https://via.placeholder.com/200x120) | ![prev](https://via.placeholder.com/200x120) |

## 👨‍💻 Author

**Dashmeet Singh**

