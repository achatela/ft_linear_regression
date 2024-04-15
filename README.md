# Car Price Prediction Using Linear Regression

## Overview
This repository contains the implementation of a basic machine learning model to predict the price of a car based on its mileage using linear regression. The project demonstrates the use of gradient descent to train the model. This educational project is designed to introduce the basic concepts of machine learning and linear regression.

## Environment Setup
To set up the Python environment and install the necessary libraries, follow these steps:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Project Structure
- `linear_regression.py`: The main script that contains functions for estimating car prices, training the model using gradient descent, and optionally plotting the regression line or calculating the model's precision.
- `data.csv`: A sample dataset containing car prices and mileage.
- `thetas.txt`: A text file where the trained model parameters (theta0 and theta1) are saved.
- `requirements.txt`: A list of Python libraries required for the project.

## Usage
Run linear_regression.py to train the model and predict prices. The script offers several options:

- `-b`: Plots the data points from `data.csv`.
- `-s`: Plots the data points and the regression line based on the current model parameters.
- `-p`: Outputs the mean absolute error of the model to evaluate its precision.

To predict the price of a car for a specific mileage, use the following command:

```bash
python3 mileage.py # You will be prompted to enter the mileage of the car
```