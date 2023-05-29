
# File Orginizer 
<img src="https://media.tenor.com/_clGIY20TSAAAAAS/diy-file-organizer-file-organizer.gif" alt="description" />

The File Organizer is a Python script designed to assist individuals in organizing their files within directories according to their file extensions.

### How it works
- it grabs all files from nested direcotries
- deletes all nested directories
- creates new directories based on file extensions. If a file does not have an extension, it checks whether the file is executable. If it is executable, the file is placed inside the "executable" folder. If it is not executable, the file is placed inside the "files" folder.


### Usage:
```./main.py directory```
OR 
```python3 main.py directory```

directory: path to the direcotry to apply the script to