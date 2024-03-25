# Doing a quick check about how streamlit works 


## Demo app about Mortgage Repayments Calculator
Streamlt it's a great tool to create web apps with python, it's very easy to use and it's very powerful.
I do this project to learn how to use it and to create a simple app that can help me to understand how to use it.
A simple mortgage repayments calculator, where you can input the amount of the loan, the interest rate, and the number of years to repay the loan, and it will calculate the monthly repayments.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://louire0mortgagerepayments.streamlit.app/?embed_options=light_theme)


## Problems I faced
- Omg requirements.txt not working well on my macbook pro m2, some dependencies are not installing correctly cause of the architecture of the m2 chip. And had problems with the installation of the deployment in Streamlit sharing. 

### To try this project in your own machine :
```bash
# using pip
pip install -r requirements.txt

# using Conda
 $ conda create --name <env_name> --file requirements.txt
 # or
 $ conda install --file requirements.txt

# run 
 $ streamlit run app.py

```

