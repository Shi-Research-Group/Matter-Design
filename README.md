# MOFLearningTool

*Empowering the Next Generation of Materials Scientists*

## Table of Contents

- [Introduction](#introduction)
- [Motivation](#motivation)
- [Features](#features)
  - [Simple Mode](#simple-mode)
  - [Advanced Mode](#advanced-mode)
  - [Leaderboard](#leaderboard)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [References](#references)
- [Acknowledgements](#acknowledgements)

## Introduction

**MOFLearningTool** is an interactive web application designed as a comprehensive learning tool to educate students and enthusiasts about the design, visualization, and analysis of Metal-Organic Frameworks (MOFs) and other advanced materials. Hosted on [Streamlit](https://streamlit.io/), MOFLearningTool leverages cutting-edge tools and technologies to make materials science accessible, engaging, and empowering, especially for young generations and minority students with limited resources.

## Motivation

The field of materials science plays a crucial role in addressing global challenges, from energy storage and environmental sustainability to healthcare and technology. However, the complexity and specialized knowledge required can be a barrier to entry for many aspiring scientists. **MOFLearningTool** aims to bridge this gap by providing an intuitive platform that allows users to design, visualize, and analyze MOFs from the comfort of their homes. By democratizing access to advanced materials design tools, we aspire to inspire the next generation of scientists to innovate and contribute to technological advancements that can help save our planet.

## Features

### Simple Mode

**Simple Mode** is tailored for beginners and educational purposes, offering a user-friendly interface with straightforward controls to design and visualize MOFs.

- **Predefined Topologies**: Users can select from a curated list of widely studied and commercially relevant MOFs.

- **Detailed Information Display**: For each selected MOF, users can access comprehensive information, including structural details and properties, presented using [PyMOL](https://pymol.org/).

- **3D Visualization**: Interactive 3D models of the selected MOFs allow users to explore their structures and understand their functionalities.

### Advanced Mode

**Advanced Mode** caters to experienced users and researchers, providing advanced tools and functionalities for custom MOF design and in-depth analysis.

- **Custom MOF Design**: Utilizing the [Streamlit-Ketcher](https://pypi.org/project/streamlit-ketcher/) component, users can draw and construct custom MOF molecules directly within the Streamlit application.

- **Molecular to MOF Conversion**: Custom molecular designs can be converted into MOF structures using [PORMAKE](https://github.com/Sangwon91/PORMAKE), enabling seamless translation from molecular components to structured MOFs.

- **Structural Analysis**: The application integrates [ZEO](https://www.zeoplusplus.org/download.html) to analyze MOF structures, providing insights into surface area, pore accessibility, and other critical properties.

- **File Conversion with ASE**: [Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/) is used to convert files from CIF to XYZ formats, facilitating compatibility and ease of analysis.

- **Tutorials and Educational Materials**: Comprehensive tutorials, including video demonstrations and illustrated guides, educate users on constructing and analyzing MOFs.

### Leaderboard

- **MOF Ranking**: A dynamic leaderboard ranks MOFs based on their surface area, encouraging user engagement and fostering a competitive environment for optimizing MOF designs.

- **Community Contributions**: Users can submit their custom-designed MOFs to the leaderboard, which integrates both pre-made and user-generated entries from the global community.

## Technology Stack

**MOFLearningTool** is built using a combination of robust technologies and tools to ensure a seamless and interactive user experience.

- **Backend and Hosting**: [Streamlit](https://streamlit.io/) serves as the core framework for building and hosting the web application.

- **Visualization Tools**:
  - [PyMOL](https://pymol.org/) for detailed 3D molecular visualization.
  - [py3Dmol](https://pypi.org/project/py3Dmol/) integrated via [stmol](https://pypi.org/project/stmol/) for interactive molecular models.

- **Molecule Editor**: [Streamlit-Ketcher](https://pypi.org/project/streamlit-ketcher/) for custom MOF design.

- **Structural Analysis**: [ZEO](https://www.zeoplusplus.org/download.html) for comprehensive structural and surface area analysis of MOFs.

- **Molecular Design Conversion**: [PORMAKE](https://github.com/Sangwon91/PORMAKE) for converting molecular designs into MOF structures.

- **File Conversion**: [Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/) for converting CIF files to XYZ format.

- **Data Management**: [CoRE MOF 2019 Database](https://mof.tech.northwestern.edu/) for accessing a wide range of MOF structures and properties.

- **Frontend Components**: [Dash Bio](https://dash.plotly.com/dash-bio/) for bioinformatics visualizations, integrated within the Streamlit framework.

- **Version Control and Collaboration**: [GitHub](https://github.com/) and [GitHub Codespaces](https://github.com/features/codespaces) for collaborative development and version management.

## Installation

To set up **MOFLearningTool** locally for development or testing purposes, follow the steps below.

### Prerequisites

- **Python 3.8 or higher**: Ensure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).

- **Git**: Install Git for version control. Download it from [here](https://git-scm.com/downloads).

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Shi-Research-Group/MOF_Learning_Tool.git
   cd MOF_Learning_Tool

2. **Create a Virtual Environment**
  
  - **Purpose:** Isolates your project's dependencies from other Python projects on your system, preventing version conflicts and ensuring a consistent development environment.
  
  - **Command:** `python3 -m venv venv` creates a virtual environment named `venv`.

3. **Activate the Virtual Environment**
  
  - **Purpose:** Enables the virtual environment so that any Python packages you install are contained within it.
  
  - **Commands:**
    - **Unix/Linux/macOS:** `source venv/bin/activate`
    - **Windows:** `venv\Scripts\activate`

4. **Install Dependencies**
  
  - **Purpose:** Installs all the necessary Python packages required for your project as specified in `requirements.txt`.
  
  - **Commands:**
    - `pip install --upgrade pip` ensures that you have the latest version of `pip`.
    - `pip install -r requirements.txt` installs all dependencies listed in the `requirements.txt` file.

4. **Run the Application**
  
  - **Purpose:** Launches your Streamlit application so you can interact with it locally.
  
  - **Command:** `streamlit run YOURPATH\streamlit_app.py` starts the application, which should open in your default web browser.

