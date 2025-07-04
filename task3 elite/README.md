# 🎨 Neural Style Transfer: Artistic Image Styling

This project implements a basic **Neural Style Transfer** system using a pre-trained VGG19 model from PyTorch. It applies the **artistic style of one image** (like Van Gogh's *Starry Night*) to the **content of another image** (like a photograph), creating a stylized output.

---

## ✅ Features

- 🧠 Uses a pre-trained VGG19 model (from `torchvision.models`)
- 🎨 Transfers visual style from one image onto the structure of another
- 🖼️ Saves and displays the final stylized image
- 🔁 Option to adjust style/content weights and number of training steps

---

## 🖼️ Example Workflow

Content Image (e.g., Eiffel Tower) + Style Image (e.g., Starry Night)
→ Stylized Output (Eiffel Tower painted in Van Gogh style)


---

## 📁 Project Structure<br/>

neural_style_transfer/<br/>
│<br/>
├── neural_style_transfer.py # Main script<br/>
├── content.jpg # Your input content image<br/>
├── style.jpg # Your input style image<br/>
├── final.jpg # Final result<br/>
├── requirements.txt # Python dependencies<br/>
└── README.md # Documentation<br/>

---

## ⚙️ Setup Instructions

### 1. Create a virtual environment (recommended)

```bash
python -m venv style_env
```
### 2. Activate the environment
Windows:
```
style_env\Scripts\activate
```
macOS/Linux:
```
source style_env/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### ▶️ How to Run the Script
Place your content image as content.jpg

Place your style image as style.jpg

### Run the script:
```
python neural_style_transfer.py
```
Output will be saved as final.jpg and optionally displayed using matplotlib.

###  How It Works
Loads a pre-trained VGG19 model

Computes content loss and style loss between generated image and targets

Uses gradient descent (Adam) to optimize the generated image

After multiple iterations, outputs a stylized result that mixes both content and style

### ⚙️ Customization Options
## In the script, you can adjust:

style_weight = 1e6 – Controls how strong the style is

content_weight = 1 – Controls how much structure is retained

epochs = 500 – Number of training steps

max_size = 400 – Resize image for faster training

###  Requirements
See requirements.txt, which includes:
```
torch>=2.0.0
torchvision>=0.15.0
Pillow>=9.4.0
matplotlib>=3.7.0
```
Install with:
```
pip install -r requirements.txt
```
### 📌 Notes
First run may take a while as VGG19 weights are downloaded (~550MB).

Works best with reasonably sized images (max_size = 300–400).

Final image is saved as final.jpg.
