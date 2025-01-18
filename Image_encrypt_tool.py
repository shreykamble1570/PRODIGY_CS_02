from PIL import Image

def encrypt_image(input_path, output_path, key):
    """Encrypt the image by adding the key to pixel values."""
    image = Image.open(input_path)
    encrypted_image = image.copy()
    pixels = encrypted_image.load()

    for i in range(image.size[0]):  # Width
        for j in range(image.size[1]):  # Height
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    encrypted_image.save(output_path)
    print(f"Encrypted image saved at {output_path}")

def decrypt_image(input_path, output_path, key):
    """Decrypt the image by subtracting the key from pixel values."""
    image = Image.open(input_path)
    decrypted_image = image.copy()
    pixels = decrypted_image.load()

    for i in range(image.size[0]):  # Width
        for j in range(image.size[1]):  # Height
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    decrypted_image.save(output_path)
    print(f"Decrypted image saved at {output_path}")

# Example usage
if __name__ == "__main__":
    print("Simple Image Encryption Tool")
    input_image_path = input("Enter the input image path: ")
    key = int(input("Enter the encryption key (integer): "))
    
    # Encrypt the image
    encrypted_path = "encrypted_image.png"
    encrypt_image(input_image_path, encrypted_path, key)
    
    # Decrypt the image
    decrypted_path = "decrypted_image.png"
    decrypt_image(encrypted_path, decrypted_path, key)
