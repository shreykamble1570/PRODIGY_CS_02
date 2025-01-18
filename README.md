# PRODIGY_CS_02
### **Project Overview: Image Encryption Tool**

This project focuses on developing a simple image encryption and decryption tool using pixel manipulation techniques. The tool ensures basic image confidentiality by modifying pixel values based on a user-defined encryption key. It’s a beginner-friendly project showcasing the intersection of programming, image processing, and cybersecurity concepts.

---

### **Task Description**

The task is to:
1. Encrypt an image by manipulating its pixel values through mathematical operations (e.g., addition of a key to RGB values).
2. Decrypt the encrypted image by reversing the operation (e.g., subtracting the same key from RGB values).
3. Provide a user-friendly way to handle the encryption and decryption processes.

---

### **Project Workflow**

#### 1. **Input Image Handling**
The program begins by loading the input image using the Python `Pillow` library. This library allows easy manipulation of image properties like pixels, size, and format.

#### 2. **Encryption**
The encryption function iterates through each pixel of the image. For every pixel, the RGB values (Red, Green, Blue) are read, and a user-defined key is added to them. The results are wrapped using the modulo operator (`% 256`) to ensure that the values stay within the valid range (0-255). The modified pixel values are then saved to a new image file.

#### 3. **Decryption**
The decryption function reverses the encryption operation. It subtracts the key from each pixel's RGB values and again wraps the results using `% 256`. This restores the original pixel values and generates the decrypted image.

#### 4. **User Interaction**
The program accepts the following inputs from the user:
   - The path to the input image.
   - A numeric key for encryption and decryption.
It outputs two images: the encrypted image and the decrypted image.

---

### **Technical Concepts**

1. **Pixel Manipulation:**
   Images are composed of pixels, where each pixel is represented by RGB values. The project leverages the fact that modifying these values alters the image’s appearance.

2. **Encryption/Decryption Logic:**
   A simple mathematical operation (addition and subtraction) is applied to pixel values using a user-defined key. This ensures that without the key, the original image cannot be easily reconstructed.

3. **Data Integrity:**
   The use of `% 256` ensures that the pixel values remain valid for image rendering, avoiding overflow or underflow errors.

---

### **Applications**
While this project is educational, it demonstrates concepts used in real-world applications like:
- Secure transmission of images over the internet.
- Protecting sensitive visual data.
- Learning the basics of encryption, which is applicable in broader cybersecurity contexts.

---

### **Tools Used**
- **Language**: Python
- **Library**: `Pillow` for image processing

---

### **Conclusion**
This project serves as an excellent introduction to both image processing and basic cryptographic techniques. It emphasizes simplicity and effectiveness, making it ideal for beginners in programming or cybersecurity. The completed tool provides a functional and practical solution for encrypting and decrypting images, laying a foundation for more advanced security projects.
