# Employee Review App

This is an MVP of a webapp that takes text of an employee review of a company as input and outputs a classification of a 1, 2, 3, 4, or 5-star review, as well as the probability of belonging to that class. The [app is hosted here](https://employee-review-app.herokuapp.com/). 

The app is built with Python and Flask, and deployed on Heroku. 

Publicly available dataset of employee reviews of companies [downloaded from Kaggle](https://www.kaggle.com/petersunga/google-amazon-facebook-employee-reviews). 

### Motivation

Playing around with loading/using ML models within apps, and learning how to deploy an app on Heroku. 

## Technologies 

Full list of requirements used to build the model and app is in the requirements.txt file. Importantly, this uses:
- Python 3.6.8 
- Flask 1.0.2
- gunicorn 19.9.0

## Launch 

To use interactively on the web, access the app [here](https://employee-review-app.herokuapp.com/). To run locally, clone this repo.
- Install requirements 
- Get the data: [download from Kaggle](https://www.kaggle.com/petersunga/google-amazon-facebook-employee-reviews)
- Build, run, and save the model: `predicting_reviews_first_pass.ipynb`, which imports `utils.py`, outputs `nb_model.pkl` and `tfidf_vec.pkl` to the models folder. 
- Build the Flask app: `app.py`, which pulls in the `.pkl` files and renders the html in the templates folder. 
- Deploy locally by running `python app.py` and accessing [localhost:5000]. 