import os
import shutil
import tkinter as tk
from tkinter import filedialog

class PhotoSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Selector")
        
        # Sets the size of the main application window.
        self.root.geometry('700x350')  
        self.folder_path = None
        self.ids = []
        self.destination_folder = None
        self.default_entry_text = "Enter comma-separated photo IDs here"

        # Label describing the application.
        self.description_label = tk.Label(root, text="Photo Selector Tool", font=("Arial", 14, "bold"))
        self.description_label.pack(pady=(10, 0))
        self.description_text = tk.Label(root, text="Choose a folder, enter photos IDs, then copy the photos.")
        self.description_text.pack(pady=(0, 20))

        # Button for selecting the photo folder.
        self.folder_button = tk.Button(root, text="Choose Photo Folder", command=self.select_folder)
        self.folder_button.pack(pady=10)

        # Displays the path of the selected folder.
        self.folder_label = tk.Label(root, text="No folder selected.")
        self.folder_label.pack(pady=5)
        
        # Entry widget for users to type in photo IDs.
        self.id_entry = tk.Entry(root, width=50)
        self.id_entry.pack(pady=10)
        self.id_entry.insert(0, self.default_entry_text)
        self.id_entry.bind("<FocusIn>", self.clear_entry)

        # Button to initiate copying of selected photos.
        self.copy_button = tk.Button(root, text="Copy Selected Photos", command=self.copy_selected_photos)
        self.copy_button.pack(pady=10)
        self.status_message = tk.Label(root, text="")
        self.status_message.pack(pady=(5, 10))

        # Button to open the destination folder, disabled by default.
        self.open_button = tk.Button(root, text="Open Copied Files Folder", command=self.open_folder, state=tk.DISABLED)
        self.open_button.pack(pady=10)

    def select_folder(self):
        """Opens a dialog for the user to select a folder, and updates the folder path."""
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.folder_label.config(text=f"Selected folder: {self.folder_path}", fg="green")
        else:
            self.folder_label.config(text="No folder selected.")

    def copy_selected_photos(self):
        """Copies photos with specified IDs from the selected folder to a 'selected_photos' subfolder."""
        if not self.folder_path:
            self.status_message.config(text="Please select a folder before copying photos.", fg="red")
            return
        
        ids_str = self.id_entry.get()
        self.ids = ids_str.strip().split(',')
        
        self.destination_folder = os.path.join(self.folder_path, 'selected_photos')
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)
        
        copied_files = 0
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.ARW') and '(' in filename and ')' in filename:
                photo_id = filename.split('(')[-1].split(')')[0]
                if photo_id in self.ids:
                    source_path = os.path.join(self.folder_path, filename)
                    destination_path = os.path.join(self.destination_folder, filename)
                    shutil.copy(source_path, destination_path)
                    copied_files += 1
        
        if copied_files == 0:
            self.status_message.config(text="No files were copied. Check the IDs or the files in the folder.", fg="red")
        else:
            self.status_message.config(text=f"Copied {copied_files} files to {self.destination_folder}", fg="green")
            self.open_button.config(state=tk.NORMAL)  # Enables the button to open the destination folder

    def open_folder(self):
        """Opens the destination folder using the default file explorer."""
        if self.destination_folder:
            os.startfile(self.destination_folder)
        else:
            messagebox.showerror("Error", "No folder has been set up yet.")

    def clear_entry(self, event):
        """Clears the default Text in the entry widget when it gains focus."""
        if self.id_entry.get() == self.default_entry_text:
            self.id_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoSelectorApp(root)
    root.mainloop()
