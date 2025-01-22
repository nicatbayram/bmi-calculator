### README: BMI Calculator Application

#### Overview
This BMI Calculator is a Python-based desktop application built using the **Tkinter** library. It allows users to calculate their Body Mass Index (BMI) by inputting their height (in cm) and weight (in kg). The application provides a BMI value along with health suggestions based on the BMI category. It also features an interactive and visually appealing user interface.

---

### Features
1. **Interactive Sliders**:
   - Users can adjust their height and weight using sliders, making the application user-friendly.
   
2. **Dynamic Feedback**:
   - Displays BMI value and provides health advice based on the BMI category:
     - **Underweight**: Encouragement to eat more.
     - **Normal**: Confirmation of good health.
     - **Overweight**: Suggestion to exercise more.
     - **Obese**: Suggestion to reduce calorie intake and exercise more.

3. **Resizable Character Image**:
   - The character image dynamically changes height based on the user's input, providing a visual representation of their height.

4. **Modern UI**:
   - Clean and visually appealing design using Tkinter widgets and custom styling.

---

### Prerequisites
1. **Python 3.x** installed on your system.
2. Required Python libraries:
   - `tkinter`
   - `PIL` (Python Imaging Library, specifically `Pillow`)

---

### Installation
1. Clone or download the repository to your local machine.
2. Install required dependencies:
   ```bash
   pip install pillow
   ```
3. Place all images in a folder named `Images` within the same directory as the script. The required image files are:
   - `icon.png` (Application icon)
   - `top.png` (Top banner image)
   - `box.png` (Decorative box image)
   - `scale.png` (Scale image for the slider)
   - `man.png` (Character image)

---

### Usage
1. Run the script using Python:
   ```bash
   python bmi_calculator.py
   ```
2. Adjust the **Height** and **Weight** using the sliders or enter values directly in the input boxes.
3. Click the **View Report** button to calculate BMI and view the health recommendations.

---

### File Structure
```
.
├── bmi_calculator.py   # Main script
├── Images/             # Directory containing required image assets
│   ├── icon.png
│   ├── top.png
│   ├── box.png
│   ├── scale.png
│   └── man.png
└── README.md           # Documentation
```

---

### Known Issues
- Ensure that all image files are present in the correct directory, or the application may not load properly.
- The sliders may occasionally show fractional values, but the BMI calculation uses precise input.

---

### Future Improvements
- Add additional BMI categories for more precise recommendations.
- Integrate multilingual support.
- Allow saving or printing BMI reports.

---

### Author
This application was developed using Python and Tkinter. Contributions are welcome!

## Images

<img width="346" alt="bm1" src="https://github.com/user-attachments/assets/2f5f9122-e91d-47a9-8f86-f19e842de5f9" />
<img width="347" alt="bm2" src="https://github.com/user-attachments/assets/8b027982-c62b-4fdf-a5ec-dd0cca963b11" />
<img width="348" alt="bm3" src="https://github.com/user-attachments/assets/93a9c230-50d7-4708-a16b-12b70e481cb0" />

