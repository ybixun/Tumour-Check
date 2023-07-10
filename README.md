[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Tumour-Check

This small-scale project explores the usage of Convolutional Neural Network (CNN) model in classifying MRI images to determine if the image indicates presence of tumour or no tumour in the brain of patients. Aside from predicting the presence of tumour in patients, it also explores possible ideas of programming architecture and data pipeline in preparation to load MRI images for training the model and predicting the images.

## Introduction/Background

This small-scale project materialised from my random thoughts about healthcare industry, where the processes and systems can be digitalised to improve efficiency. Currently, Singapore healtcare and medical industry is currently facing manpower shortage, with additional burdence of future expected increase in demand for manpower in the near future. With ideas to explore the possibilities of improving the efficiency of systems in healthcare industry to combat the manpower shortage, I decided to program out data pipeline and an MRI image Classification model made using CNN to aid doctors and medical staffs in reducing workflow time or providing opportunities for further manpower optimisation.

## Features

1. Predicting if patient has tumour or no tumour based on MRI Image using a CNN model.

# Usage

The Convolutional Neural Network Model is implemented on Jupyter Notebook, a Flask API on Python script, Dockerfile for containerization and HTML frontend structure located in the 'templates' folder.

## Prerequisites

The following environment and dependencies are required:

- Python 3.10.9
- Docker (via Docker deployment)


## 1. Setup

* Ensure that Python, Jupyter Notebook, Flask, Docker and web browser are installed on your machine.
* Clone the repository to your desired directory on your local machine or download the project files:

```bash
git clone https://github.com/[YourUsername]/[YourRepository].git
```

* Navigate into the directory containing the cloned repository:

```bash
cd [YourRepository]
```

Additionally, a few Python packages are needed. Ensure that'requirements.txt' or 'environment.yml' file should be in the same directory where you are setting up the environment and dependencies. The dependencies can be installed by navigating to the project directory and running the following command:

* Install the required Python packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

If you are using Conda, create a new environment with the dependencies in the environment.yml file:

```bash
conda env create -f environment.yml
```

## 2. Running the CNN Model in Jupyter Notebook

* Start the Jupyter Notebook via Anaconda Software or by starting the Jupyter Notebook Server:

```bash
jupyter notebook
```

* Navigate to the notebook file ('Tumour-Check Project.ipynb') and click on it to open it.
* Run the notebook document step-by-step (one cell a time) by pressing shift + enter, or run all cells at once using Cell -> Run All.

## 3. Dockerization

* Build the Docker image using the Dockerfile. Ensure that when you are executing the following command lines, they are executed in the same directory as the Dockerfile. Replace [image_name] with your preferred name for the Docker image and execute the following in your command prompt:

```bash
docker build -t [image_name] .
```

* After building the image, run it in your command prompt:

```bash
docker run -p 5000:5000 [image_name]
```

Now, the application should be accessible at http://localhost:5000 on your web browser.

## 4. Accessing the HTML Frontend

* Navigate to the 'templates' directory.
* Open the HTML file in your preferred web browser.
* You should now be able to interact with the Flask API via the HTML frontend.
* To use the model, click 'Choose File" and select any image from the "Testing Image" directory.
* After which, click 'Upload' and get the result of the prediction.

# Credits

- Yu Bixun - Initial Work - [ybixun](https://github.com/ybixun)

# License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
This project is licensed under the terms of the [MIT License](LICENSE)