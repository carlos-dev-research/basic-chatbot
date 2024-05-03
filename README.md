# INSTALLATION
The Code was tested on Windows 10 with Nvidia T600 mobile gpu

## Pre requirements
1.- Ollama should be installed in the system
https://ollama.com/download

2.- If you want to use nvidia gpu, necessary drivers must be installed
https://www.nvidia.com/download/index.aspx

3.- Pytorch installation is also necessary to run Speech to Text model
https://pytorch.org/get-started/locally/

4.- Conda or miniconda must be installed in the system
https://docs.anaconda.com/free/miniconda/miniconda-install/

## Installation steps
1.- Create a conda enviroment with python 3.8
conda create -n <envName> python=3.8

2.- Activate enviroment and install dependencies 
python -m pip install -U pip
pip install transformers
pip install soundfile
pip install librosa
pip install ollama
pip install Flask
conda install -c conda-forge ffmpeg

## Run the localhost
1.- Clone repository and run main.py
git clone https://github.com/carlosggl/basic-chatbot.git
cd clone <repository_main_folder>
python main.py

2.- You can access the chat interface from the localhost:5000 or 127.0.0.1:5000 in the browser