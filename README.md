````markdown
# BongoCat AutoClicker

**Author:** [ShiroxLoL](https://github.com/ShiroxLoL)  

---

## 📦 Installation

### Option 1 — Clone via Git (Recommended)

1. **Install [Git](https://git-scm.com/downloads)**  
   Verify the installation:
   ```bash
   git --version
````

2. **Clone the repository:**

   ```bash
   git clone https://github.com/ShiroxLoL/BongoCat-AutoClicker.git
   cd BongoCat-AutoClicker
   ```

3. **Install [Python 3.8+](https://www.python.org/downloads/)**
   Verify the installation:

   ```bash
   python --version
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

### Option 2 — Download ZIP Manually

1. Go to the GitHub page:
   [https://github.com/ShiroxLoL/BongoCat-AutoClicker](https://github.com/ShiroxLoL/BongoCat-AutoClicker)

2. Click the green **“Code”** button → select **“Download ZIP”**.

3. Extract the ZIP file anywhere on your computer.

4. Open a terminal or command prompt in the extracted folder.

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. **Run the script:**

   ```bash
   python autoclicker.py
   ```

2. **Controls:**

   * Press **`p`** → Start or stop the auto-clicker
   * Press **`q`** → Quit the program

3. **Behavior:**

   * Randomized click interval: **0.01 – 0.02 seconds**
   * Each click is held for **0.02 seconds**
   * Status messages appear in the console (Started / Stopped)

---

## ⚙️ Configuration

You can modify timing values in `autoclicker.py` to adjust click speed:

```python
min_interval = 0.01  # Minimum delay between clicks (seconds)
max_interval = 0.02  # Maximum delay between clicks (seconds)
hold_time = 0.02     # Duration each click is held (seconds)
```

Adjust these values cautiously to avoid detection or instability.

---

## 🧩 Requirements

* [Python 3.8+](https://www.python.org/downloads/)
* [pydirectinput==1.0.7](https://pypi.org/project/pydirectinput/)
* [keyboard==0.13.5](https://pypi.org/project/keyboard/)
* [Git](https://git-scm.com/downloads) *(only needed for cloning)*

Install all requirements:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Disclaimer

Use this program **responsibly**.
Automated clicking may violate the Terms of Service of certain software or games.
You are solely responsible for how you use this tool.
The author assumes **no liability** for any misuse or resulting consequences.

---

## 📄 License and Usage Rights

**All Rights Reserved**

You may:

* Download and modify the code for **personal, non-commercial use only**.

You may **not**:

* Redistribute, re-upload, sell, or use this code for **commercial purposes**
  without **explicit written permission** from the author (**ShiroxLoL**).

---

© 2025 [ShiroxLoL](https://github.com/ShiroxLoL) - All Rights Reserved.
