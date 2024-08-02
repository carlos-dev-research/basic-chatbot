# INSTALLATION
The Code was tested on Windows 10 with Nvidia T600 mobile gpu and 32gb of RAM
If your system has less than 22 GB of RAM, please enable system disk memory pooling for optimal performance or comment whisper object

## Pre requirements
1.- Ollama should be installed in the system
https://ollama.com/download

2.- If you want to use nvidia gpu, necessary drivers must be installed
https://www.nvidia.com/download/index.aspx

3.- Conda or miniconda must be installed in the system
https://docs.anaconda.com/free/miniconda/miniconda-install/

## Installation steps
1.- Create a conda enviroment with python 3.8
conda create -n <env_name> python=3.8

2.- Activate enviroment 
conda activate <env_name>

3.- Install pytorch to run the whisper model, go to the website and follow neccesary step according to your hardware
https://pytorch.org/get-started/locally/

4.- Install dependencies with the following commands
python -m pip install -U pip
pip install transformers
pip install soundfile
pip install librosa
pip install ollama
pip install Flask
conda install -c conda-forge ffmpeg

## Run the localhost
1.- Clone repository and run main.py
git clone https://github.com/carlos-dev-research/basic-chatbot.git
cd clone <repository_main_folder>
python main.py

2.- You can access the chat interface from the localhost:5000 or 127.0.0.1:5000 in the browser
