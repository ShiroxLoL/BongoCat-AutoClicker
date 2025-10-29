````markdown
# 🐾 BongoCat AutoClicker

**Author:** [ShiroxLoL](https://github.com/ShiroxLoL)  

---

## 📦 Installation

### 🧠 Option 1 — Clone via Git (Recommended)

1. **Install Git**  
   Download from: [https://git-scm.com/downloads](https://git-scm.com/downloads)  
   Verify installation:
   ```bash
   git --version
````

2. **Clone the repository**

   ```bash
   git clone https://github.com/ShiroxLoL/BongoCat-AutoClicker.git
   cd BongoCat-AutoClicker
   ```

3. **Install Python 3.8+**
   Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   Verify installation:

   ```bash
   python --version
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

### 📁 Option 2 — Download ZIP Manually

1. Go to the project page: [https://github.com/ShiroxLoL/BongoCat-AutoClicker](https://github.com/ShiroxLoL/BongoCat-AutoClicker)
2. Click the green **“Code”** button → select **“Download ZIP”**
3. Extract the ZIP file to any location
4. Open a terminal or command prompt inside the extracted folder
5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. **Run the script**

   ```bash
   python autoclicker.py
   ```

2. **Controls**

   * 🔄 Press **`p`** → Start or stop the auto-clicker
   * ❌ Press **`q`** → Quit the program

3. **Behavior**

   * Randomized interval: **0.01 – 0.02 seconds**
   * Each click is held for **0.02 seconds**
   * Console shows messages when started or stopped

---

## 🧰 Configuration

You can modify timing values directly in `autoclicker.py`:

```python
min_interval = 0.01  # Minimum delay between clicks (seconds)
max_interval = 0.02  # Maximum delay between clicks (seconds)
hold_time = 0.02     # Duration each click is held (seconds)
```

💡 Adjust these values to control click speed and behavior.

---

## 🧩 Requirements

* 🐍 Python 3.8+ → [https://www.python.org/downloads/](https://www.python.org/downloads/)
* ⚙️ pydirectinput==1.0.7 → [https://pypi.org/project/pydirectinput/](https://pypi.org/project/pydirectinput/)
* ⌨️ keyboard==0.13.5 → [https://pypi.org/project/keyboard/](https://pypi.org/project/keyboard/)
* 🔗 Git (only needed for cloning) → [https://git-scm.com/downloads](https://git-scm.com/downloads)

Install all requirements:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Disclaimer

Use this tool **responsibly**.
Automated clicking may violate the Terms of Service of some games or applications.
You are fully responsible for how you use this program.
The author (**ShiroxLoL**) assumes **no liability** for misuse or resulting consequences.

---

## 📜 License and Usage Rights

**All Rights Reserved**

You may:

* ✅ Download and modify the code for **personal, non-commercial use only**

You may **not**:

* ❌ Redistribute, re-upload, sell, or use this code for **commercial purposes**
  without **explicit written permission** from the author (**ShiroxLoL**)

---

© 2025 [ShiroxLoL](https://github.com/ShiroxLoL) - All Rights Reserved.
