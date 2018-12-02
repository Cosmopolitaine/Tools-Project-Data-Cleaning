# Capital Markets Data Cleaning and Analytics 

## What is This Project
This project deals with the daily stock prices of 500 stocks over the horizon of 5 years. We employed Python to perform data cleaning, data analytics and visualization. 

Data Cleaning: 
Found missing data, wrong data (eg. unreasonable high or low price, too high or too low returns, stocksplits, etc.) after getting a rough view of potential wrong data with pandas. Then corrected them with webcrawller or mannually (for sharesplits). The output 'Clean_Data_Out.csv' would be used for later analysis and visualization. 

Data Analysis:
(1)
(2) 
(3) Predicted stock price using basic Linear Regression Model upon splitted training and testing data from historical data.

Data Visualization:
(1) Plotted histograms and historical stock price data for a rough view before cleaning data.
(2) 
(3) Plotted chosen stock data and comparison of actual and predicted data in Linear Regression part.
                                

## How to Use This Project
### 1. Data Cleaning
Open the "Data_Cleaning.ipynb" file, and run cells in the same order as they are arranged, then execute main() function. This program will ask you for a file name, and we have included a sample "all_stocks_5yr.csv" in the the repository, or you can use any .csv file with columns ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Name'). The program will automatically find missing data and suspicious values, it will output a file in the end, you can choose the name of the output file. 
The other programs will make use of the cleaned data this program creates, so please run this program first. 

### 2. Data Analysis
Source Codes for data analysis are in 'CAPM_Regression_Data_Analysis.ipynb' and 'LinearRegression_Model.ipynb'. They make use of the Output data from data cleaning program. We have included an example of cleaned data 'Clean_Data_Out.csv' which is 'all_stock_5yr.csv' cleaned using the data cleaning program to be used in the data analysis part of the project. 



### 4. Stock Price Prediction with Linear Regression Model
Open "LinearRegression_Model.ipynb". In the second cell, input 'Clean_Data_Out' to read this csv file. Choose the stock you are interested in from the sp 500 in this third cell. Then simply run the cells in order and get the final plotting of prediction from this basic model.
   
## Group: Coding the Tools

## Credits
### Contributors:

Yuxuan Zheng (uni = yz3460, username = Cosmopolitaine): Data Cleaning Program.

Weichong Ni (uni = wn2163, username = Weichong515): (1) Part of Data Cleaning (Cooperated with Shilan Tu in getting view of missing and potential wrong data, combined the two parts of data cleaning).  (2) Prediction with Linear Regression.

Shilan Tu

Mengran Cui (uni = mc4575): (1) Stock price data cleaning. Identify data anomalies, including missing values & suspicoous stock movements. (2) Construct CAPM model. Find SP500 and treasury yield data, left merge with existing stock price using dates as identifier.  Calculated Betas using variance and covariance. Convert stock price to returns. Calculated daily CAPM returns for each stock. Compared predicted CAPM return vs. realized return. 
