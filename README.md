
# File Orginizer 
<img src="https://media.tenor.com/_clGIY20TSAAAAAS/diy-file-organizer-file-organizer.gif" alt="description" />

The File Organizer is a Python script designed to assist individuals in organizing their files within directories according to their file extensions.

### How it works
- it grabs all files from nested direcotries
- deletes all nested directories
- creates new directories based on file extensions. If a file does not have an extension, it checks whether the file is executable. If it is executable, the file is placed inside the "executable" folder. If it is not executable, the file is placed inside the "files" folder.

### Example
![Screenshot from 2023-05-29 14-45-58](https://github.com/celomary/file_organizer/assets/59455493/5c4c0639-7825-42fa-9b9e-ae1855ffd16b)
![Screenshot from 2023-05-29 14-48-07](https://github.com/celomary/file_organizer/assets/59455493/f4c6487c-a8dd-499f-a672-4a3fb9584f99)


### Usage:
```./main.py directory```
OR 
```python3 main.py directory```

directory: path to the direcotry to apply the script to
