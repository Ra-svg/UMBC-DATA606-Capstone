
# 1. New York Housing Price Prediction

- **Project Title:** New York Housing Price Prediction
- **Prepared for:** University Of Maryland, Baltimore County(UMBC), **Under:** Professor Dr. Chaojie (Jay) Wang
- Author : -

   - Name: Rahul Kaushik Mallela
   - LinkedIn Profile: https://www.linkedin.com/in/rahulkaushikm/
   - GitHub Profile: https://github.com/Ra-svg
   - Youtube Link: https://youtu.be/Xxf0OZVW4F0
   - Presentation link: 

# Background:

- The dataset comprises of  details listings of 4,801 properties for sale in New York City, including condos, houses, and townhouses. It covers 17 categories, such as broker information, property type, price, bedrooms, bathrooms, square footage, and locations across the city. Prices range widely, with listings like a $195 million condo, showcasing the market's diversity. Latitude and longitude details of the properties enhance the market analysis. This comprehensive dataset is a valuable tool for buyers, investors, offering a clear view of New York's real estate landscape.

# Research Questions:
- **1. What factors most significantly impact house prices in New York?
- **2. Can we accurately predict the price of a house based on its characteristics/features?
# Data :-
- ## Data Size:
- The dataset is approximately 1.33MB
- It consists of 4801 rows with 17 distinct columns

## With the  Data Source: https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market

- ## Data Features:
| Column Name                                        | Data Type    | Definition                                                                                       |
|----------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------|
| BROKERTITLE                                        | category     | The brokerage or agent listing the property, along with some location details                    |                          
| TYPE                                               | category     | The type of property, such as "Condo for sale," "House for sale," or "Townhouse for sale"        |                          
| PRICE                                              | int          | The listing price of the property                                                                |                          
| BEDS                                               | int          | The number of bedrooms                                                                           | 
| BATH                                               | int          | number of bathrooms, which may be a whole number or a decimal to account for partial bathrooms   |                          
| PROPERTYSQFT                                       | float        | The square footage of the property                                                                | 
| ADDRESS                                            | object       | specific address or description of the property location                                         |                          
| STATE                                              | object       | general location, typically including the city and state                                         |                          
| MAIN_ADDRESS                                       | object       | combination of the specific address and the general location                                      | 
| ADMINISTRATIVE_AREA_LEVEL_2, LOCALITY, SUBLOCALITY | object       | Various levels of geographic detail, from broader areas to more specific localities               |
| STREET_NAME                                        | object       | The name of the street where the property is located                                              |
| LONG_NAME                                          | object       | longer or more descriptive name for the location, possibly including the building or complex name |
| FORMATTED_ADDRESS                                  | object       | full address that may include the building name or number, street, city, state, and Zipcode       |
| LATITUDE, LONGITUDE                                | float        | Geographic coordinates of the property                                                            |  

# Features: 
- Here are the some Important Features for the  Machine Learning Models
  - Price
  - Beds
  - Bath
  - PropertySqft
  - State
  - Sublocality

# Exploratory Data Analysis (EDA):

![image](https://github.com/Ra-svg/UMBC-DATA606-Capstone/assets/65843488/94d5e8d3-9c5a-4266-b626-d82a44f8b3b2)

- This bar chart shows the different property types for sale in New York city. "Co-op for sale" and "House for sale" are the most common in the graph, with around 1,400 and 800 listings respectively. Other important types include "Condo for sale" and "Multi-family home for sale." Less common options, like "Foreclosure" and "Land for sale," have fewer listings. This variety highlights the diverse real estate market in New York.

![image](https://github.com/Ra-svg/UMBC-DATA606-Capstone/assets/65843488/5d650c57-582f-4e4c-a806-bdd2696c922f)


This map visualizes the distribution of property prices across New York City. Each dot represents a property listing, with color intensity indicating price ranges. Darker shades denote higher prices, while lighter shades indicate lower prices. The map highlights areas with high property values, offering a clear geographical overview of the real estate market in New York. This visualization helps identify price patterns across the city.

![image](https://github.com/Ra-svg/UMBC-DATA606-Capstone/assets/65843488/f97e7123-6615-4260-bc75-cce23a513641)

This histogram shows the distribution of property prices per square foot in New York City. The majority of properties have prices between $200 and $800 per square foot, with fewer properties priced higher. The right skew of the histogram indicates that while most properties fall within the lower price range, there are some high-value outliers. This visualization helps in understanding the general pricing trend and the spread of property values per square foot.

# Model Training :-
- ## Models For Analysis:
   - Overview of the different regression models evaluated such as 
    - Linear regression
    - Random Search
    - XGBoost
    - Gradient Boosting
    - Lasso
    - Ridge

- ## Training and Development:

- Model training and development process includes, data splitting in which data is divided into training and testing sets (80 percent for training and 20 percent for testing).
- Feature Engineering includes creation of the new feature called "Price per Sqft" which will help into analysis and modeling process, leading to more informed decision making for purchasing the property in the New York.
- Model Evaluation metrics is used to evaluate model performance, such as RMSE and R^2, And atlast, Hyperparameter Tuning to optimize the model parameters. 

![image](https://github.com/Ra-svg/UMBC-DATA606-Capstone/assets/65843488/7d2126d9-65d7-43bd-abd7-81e094adf25e)

# Web App Development: 

![web-1](https://github.com/Ra-svg/UMBC-DATA606-Capstone/assets/65843488/278a7bd7-0c3a-46fe-8ce4-516c2e725c18)

- The web app, built with Streamlit, allows users to predict New York housing prices by entering details like bedrooms, bathrooms, square footage, and location. The app uses a trained machine learning model to generate price estimates instantly. With a simple interface, users can input their data and click "Predict Price" to see the estimated property value. 
- Additionally, the app offers a download link for the model, enabling offline predictions. This tool makes price estimation easy and accessible for buyers, sellers, and real estate professionals.

# Conclusion:

- This project developed a predictive model for estimating New York housing prices, with the XGBoost Regressor model performing best among others. A user-friendly Streamlit web app was created to provide price predictions based on user input. This tool helps buyers, sellers to make well-informed decisions. Future enhancements in the project will include real-time data for even better accuracy for the predicti.

# Reference:
- https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market
