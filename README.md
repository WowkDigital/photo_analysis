# photo_analysis

# [ARW to JPEG Converter](https://github.com/WowkDigital/photo_analysis/blob/main/arw_to_jpg.py)

This Python script converts ARW files to JPEG format using the camera's white balance settings. It is designed to process all ARW files in a specified directory, adjusting the JPEG quality to ensure that each image file does not exceed a specified size limit.

## Features

- Converts all ARW files in a specified directory.
- Uses camera white balance for natural color reproduction.
- Adjusts JPEG quality to meet size constraints.

## Requirements

- Python 3.6+
- rawpy
- Pillow

# Photo Selector Application

The Photo Selector Application is a simple graphical user interface (GUI) tool created using Python's `tkinter` library. It allows users to select a folder, specify photo IDs, and copy those specific photos to a new subfolder within the selected directory.

## Features

- **Folder Selection**: Users can select the folder where their photos are stored.
- **ID Input**: Users can manually enter the IDs of the photos they wish to copy.
- **Photo Copying**: Copies specified photos based on their IDs to a new subfolder.
- **Open Destination Folder**: Users can open the folder where the selected photos have been copied.
