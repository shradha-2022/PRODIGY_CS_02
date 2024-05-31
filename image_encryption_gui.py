import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

# Load the image
def load_image(image_path):
    image = Image.open(image_path)
    return image

# Save the image
def save_image(image, output_path):
    image.save(output_path)

# Encrypt the image by applying a simple operation (e.g., adding a value to each pixel)
def encrypt_image(image, key):
    np_image = np.array(image)
    encrypted_image = (np_image + key) % 256  # Ensure pixel values stay within valid range
    return Image.fromarray(np.uint8(encrypted_image))

# Decrypt the image by reversing the encryption operation
def decrypt_image(encrypted_image, key):
    np_image = np.array(encrypted_image)
    decrypted_image = (np_image - key) % 256  # Ensure pixel values stay within valid range
    return Image.fromarray(np.uint8(decrypted_image))

# GUI Application
class ImageEncryptionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Encryption Tool")

        # Create frames
        self.image_frame = tk.Frame(master)
        self.image_frame.pack(pady=10)
        
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        # Image display
        self.image_label = tk.Label(self.image_frame, text="No Image Loaded")
        self.image_label.pack()

        # Buttons
        self.load_button = tk.Button(self.button_frame, text="Load Image", command=self.load_image, width=15, bg='#f0f0f0')
        self.load_button.grid(row=0, column=0, padx=10, pady=5)

        self.encrypt_button = tk.Button(self.button_frame, text="Encrypt Image", command=self.encrypt_image, width=15, bg='#f0f0f0')
        self.encrypt_button.grid(row=0, column=1, padx=10, pady=5)

        self.decrypt_button = tk.Button(self.button_frame, text="Decrypt Image", command=self.decrypt_image, width=15, bg='#f0f0f0')
        self.decrypt_button.grid(row=1, column=0, padx=10, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save Image", command=self.save_image, width=15, bg='#f0f0f0')
        self.save_button.grid(row=1, column=1, padx=10, pady=5)

        self.image = None
        self.encrypted_image = None
        self.key = 50  # Simple key for encryption/decryption

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = load_image(file_path)
            self.display_image(self.image)

    def display_image(self, image):
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image

    def encrypt_image(self):
        if self.image:
            self.encrypted_image = encrypt_image(self.image, self.key)
            self.display_image(self.encrypted_image)
        else:
            messagebox.showwarning("Warning", "No image loaded")

    def decrypt_image(self):
        if self.encrypted_image:
            decrypted_image = decrypt_image(self.encrypted_image, self.key)
            self.display_image(decrypted_image)
        else:
            messagebox.showwarning("Warning", "No encrypted image available")

    def save_image(self):
        if self.encrypted_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                save_image(self.encrypted_image, file_path)
        else:
            messagebox.showwarning("Warning", "No encrypted image to save")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()
