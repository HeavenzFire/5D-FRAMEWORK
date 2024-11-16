import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, colorchooser
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw, ImageFont
import tensorflow as tf
import numpy as np
import os

# Global variable to store the current image
current_image = None
current_image_path = None

# Function to open an image file
def open_image():
    global current_image, current_image_path
    file_path = filedialog.askopenfilename()
    if file_path:
        current_image_path = file_path
        current_image = Image.open(file_path)
        current_image.show()

# Function to save the current image
def save_image():
    global current_image
    if current_image:
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if save_path:
            current_image.save(save_path)
            messagebox.showinfo("Image Saved", f"Image saved successfully at {save_path}")
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to resize the image
def resize_image():
    global current_image
    if current_image:
        width = simpledialog.askinteger("Input", "Enter new width:")
        height = simpledialog.askinteger("Input", "Enter new height:")
        if width and height:
            current_image = current_image.resize((width, height))
            current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to crop the image
def crop_image():
    global current_image
    if current_image:
        left = simpledialog.askinteger("Input", "Enter left coordinate:")
        top = simpledialog.askinteger("Input", "Enter top coordinate:")
        right = simpledialog.askinteger("Input", "Enter right coordinate:")
        bottom = simpledialog.askinteger("Input", "Enter bottom coordinate:")
        if None not in (left, top, right, bottom):
            current_image = current_image.crop((left, top, right, bottom))
            current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to rotate the image
def rotate_image():
    global current_image
    if current_image:
        angle = simpledialog.askfloat("Input", "Enter rotation angle:")
        if angle is not None:
            current_image = current_image.rotate(angle, expand=True)
            current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to adjust brightness
def adjust_brightness():
    global current_image
    if current_image:
        factor = simpledialog.askfloat("Input", "Enter brightness factor (0.0 - 2.0):")
        if factor is not None:
            enhancer = ImageEnhance.Brightness(current_image)
            current_image = enhancer.enhance(factor)
            current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to adjust contrast
def adjust_contrast():
    global current_image
    if current_image:
        factor = simpledialog.askfloat("Input", "Enter contrast factor (0.0 - 2.0):")
        if factor is not None:
            enhancer = ImageEnhance.Contrast(current_image)
            current_image = enhancer.enhance(factor)
            current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to apply filters
def apply_filter():
    global current_image
    if current_image:
        filter_options = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EMBOSS", "SHARPEN", "SMOOTH"]
        choice = simpledialog.askstring("Input", f"Choose filter: {', '.join(filter_options)}")
        if choice in filter_options:
            current_image = current_image.filter(getattr(ImageFilter, choice))
            current_image.show()
        else:
            messagebox.showwarning("Invalid Choice", "Please select a valid filter.")
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to add text to the image
def add_text():
    global current_image
    if current_image:
        text = simpledialog.askstring("Input", "Enter text to add:")
        if text:
            draw = ImageDraw.Draw(current_image)
            font_size = simpledialog.askinteger("Input", "Enter font size:", initialvalue=20)
            color = colorchooser.askcolor(title="Choose text color")[1]
            font = ImageFont.truetype("arial.ttf", font_size)
            position = (10, 10)  # Default position
            draw.text(position, text, fill=color, font=font)
            current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to apply AI-based enhancements
def ai_enhance_image():
    global current_image
    if current_image:
        img_array = np.array(current_image) / 255.0

        # Placeholder for an actual AI enhancement model
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=img_array.shape),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
            tf.keras.layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')
        ])

        # Simulate enhancement (this won't actually change the image without training)
        enhanced_img_array = model.predict(np.expand_dims(img_array, axis=0))[0]
        enhanced_img = Image.fromarray((enhanced_img_array * 255).astype(np.uint8))
        current_image = enhanced_img
        current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to remove background
def remove_background():
    global current_image
    if current_image:
        img_array = np.array(current_image)
        # Placeholder for an actual background removal algorithm
        mask = np.full(img_array.shape[:2], 255, dtype=np.uint8)
        img_array[mask == 0] = [255, 255, 255]
        bg_removed_img = Image.fromarray(img_array)
        current_image = bg_removed_img
        current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to generate image from text prompt
def generate_image_from_text():
    prompt = simpledialog.askstring("Input", "Enter your text prompt:")
    if prompt:
        # Placeholder for an actual generative AI model
        generated_img_array = np.random.rand(256, 256, 3) * 255
        generated_img = Image.fromarray(generated_img_array.astype(np.uint8))
        generated_img.show()
    else:
        messagebox.showwarning("No Prompt", "Please enter a text prompt.")

# Function to apply custom filter (curves)
def apply_custom_filter():
    global current_image
    if current_image:
        # Placeholder for custom filter logic
        current_image = ImageOps.autocontrast(current_image)
        current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Function to adjust saturation
def adjust_saturation():
    global current_image
    if current_image:
        factor = simpledialog.askfloat("Input", "Enter saturation factor (0.0 - 2.0):")
        if factor is not None:
            enhancer = ImageEnhance.Color(current_image)
            current_image = enhancer.enhance(factor)
            current_image.show()
    else:
        messagebox.showwarning("No Image", "Please open an image first.")

# Create the main window
root = tk.Tk()
root.title("Advanced AI-Powered Photo Editor")
root.geometry("400x650")

# Create a frame for the buttons
frame = tk.Frame(root)
frame.pack(pady=20)

# Create buttons for each function
open_button = tk.Button(frame, text="Open Image", command=open_image, width=30)
save_button = tk.Button(frame, text="Save Image", command=save_image, width=30)
resize_button = tk.Button(frame, text="Resize Image", command=resize_image, width=30)
crop_button = tk.Button(frame, text="Crop Image", command=crop_image, width=30)
rotate_button = tk.Button(frame, text="Rotate Image", command=rotate_image, width=30)
brightness_button = tk.Button(frame, text="Adjust Brightness", command=adjust_brightness, width=30)
contrast_button = tk.Button(frame, text="Adjust Contrast", command=adjust_contrast, width=30)
saturation_button = tk.Button(frame, text="Adjust Saturation", command=adjust_saturation, width=30)
filter_button = tk.Button(frame, text="Apply Filter", command=apply_filter, width=30)
custom_filter_button = tk.Button(frame, text="Apply Custom Filter", command=apply_custom_filter, width=30)
text_button = tk.Button(frame, text="Add Text", command=add_text, width=30)
ai_enhance_button = tk.Button(frame, text="AI Enhance Image", command=ai_enhance_image, width=30)
bg_remove_button = tk.Button(frame, text="Remove Background", command=remove_background, width=30)
generate_image_button = tk.Button(frame, text="Generate Image from Text", command=generate_image_from_text, width=30)

# Pack the buttons into the frame
buttons = [
    open_button, save_button, resize_button, crop_button, rotate_button,
    brightness_button, contrast_button, saturation_button, filter_button,
    custom_filter_button, text_button, ai_enhance_button,
    bg_remove_button, generate_image_button
]

for idx, btn in enumerate(buttons):
    btn.grid(row=idx, column=0, pady=5)

# Run the application
root.mainloop()
