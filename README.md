# Content

There are 4000 images of two of the popular cars (Swift and Wagonr) in India of make Maruti Suzuki with 2000 pictures belonging to each model. The data is divided into training set with 2400 images , validation set with 800 images and test set with 800 images. The data was randomized before splitting into training, test and validation set.

The purpose of this model to make clasiffier for those two car brands in order to classify them correctly.

# About files

- data and data_images - our data
- Modelling.ipynb - notebook for loading data, EDA, modelling, results, exporting final model, etc
- df.csv - final dataframe for modelling
- End_user.ipyng - notebook which shows how model is working by uploading images
- ./static - model 
- ./app - end user app with fastapi
- requirements.txt - all needed librarys for End_user.ipyng and fastapi app

# How to use fastapi app
1. create new env
2. install requirements file
3. write down in terminal uvicorn app.controller:app --reload
4. write down in browser http://127.0.0.1:8000/docs and press predict, try out, choose image and excecute. Below you will see predicted class: Swift or Wagonr.

