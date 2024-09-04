Eased Workflow
============
[![Linktree](https://img.shields.io/badge/linktree-43E55E?style=flat&logo=linktree&logoColor=white)](https://linktr.ee/fecitekme)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karacaarif/)

This is a repository for easing the workflow of design software via scripting. 

![Eased Workflow](https://github.com/fecitekme/eased-workflow/blob/main/repo/banner.png?raw=true)

# Table of Contents

1. [Buy me a coffee](#buy-me-a-coffee)
2. [Scripts](#scripts)
   - [Blender Isolated Mesh Rendering](#blender-isolated-mesh-rendering)
   - [Adobe Illustrator Translator](#adobe-illustrator-translator)
   - [Adobe Illustrator Reorder Artboards](#adobe-illustrator-reorder-artboards)
3. [Built With](#built-with)
4. [License](#license)

---

## Buy me a coffee

Every software has its flaws, but until they're fixed, I'm here to help rev up your workflow. If these scripts make your life easier, consider buying me a coffee!

<a href="https://www.buymeacoffee.com/fecitekme" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

---

## Scripts

### 📦 Blender Isolated Mesh Rendering

#### Setup & Usage
1. Ready your scene and camera
2. Create collections for your meshes (rendering will be processed using the collections range identified in the script)
3. Modify settings in the script for your need, change the rendering engine, set collections range in the array, enable or disable transparency
4. Run the script

<img src="https://github.com/fecitekme/eased-workflow/blob/main/repo/scripts_usage/Setup%20and%20Usage.gif?raw=true" width="600" alt="Usage">

### 📦 Adobe Illustrator Translator

#### Setup & Usage
1. Extract scripts to CEP/extensions (or anwhere if you need one time use)
2. In Illustrator go to File->Scripts->Other
3. Locate your folder and run 'extract-text.jsx'
4. Save your JSON file to the script folder as 'large_file.jsx'
5. Open Command Prompt
6. Change working directory to script folder's directory
7. Type 'python translator.py' to run Python script, then enter your Google Cloud API and your target language code (e.g. es, en)
8. Your translated file will be placed in script folder.
9. In Illustrator, go to File->Scripts->Other and run 'import-text.jsx' in scripts folder. It will directly replace original text in your artboards.

<img src="https://github.com/fecitekme/eased-workflow/blob/main/repo/scripts_usage/it_usage.gif?raw=true" width="600" alt="Usage">

---

## Built With

Developed primarily using JavaScript and Python, this project leverages versatility and power to streamline workflows and enhance productivity.

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

## License
This project is licensed under the terms of the **MIT** license.
