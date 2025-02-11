# C02 Emission Prediction

This project uses the ‘scikit-learn’ library to train a machine learning model using linear regression to predict CO2 emissions based on engine size, with a simple interface created using Streamlit for user interaction.

## Requirements

- **Python**: >= 3.11
- **Poetry**: [Install](https://python-poetry.org/docs/#installation)

## Installation

Install dependencies using Poetry:

```shell
poetry install
```

## How to run the project

1. Activate the virtual environment
```shell
Invoke-Expression(poetry env activate)
```

3. Train the model using the following command:

```shell
python src/train.py
```

3. Start the Streamlit app using the following command:

```shell
streamlit run src/main.py
```
