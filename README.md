# Capital Markets Data Cleaning and Analytics 

## What is This Project
This project deals with the daily stock prices of 500 stocks over the horizon of 5 years. We employed Python to perform data cleaning, data analytics and visualization. 

## How to Use This Project
### 1. Data_Cleaning
Open the "Data_Cleaning.ipynb" file, and run cells in the same order as they are arranged, then execute main() function. This program will ask you for a file name, and we have included a sample "all_stocks_5yr.csv" in the the repository, or you can use any .csv file with columns ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Name'). The program will automatically find missing data and suspicious values, it will output a file in the end, you can choose the name of the output file. 
The other programs will make use of the cleaned data this program creates, so please run this program first. 

### 2. Data Analysis
Source Codes for data analysis are in 'CAPM_Regression_Data_Analysis.ipynb' and 'LinearRegression_Model.ipynb'. They make use of the Output data from data cleaning program. We have included an example of cleaned data 'Clean_Data_Out.csv' which is 'all_stock_5yr.csv' cleaned using the data cleaning program to be used in the data analysis part of the project. 

### Required Modules and Packages: 
1. pandas
2. pandas_datareader
3. matplotlib.pyplot

   
## Credits
### Contributors:

Yuxuan Zheng (yz3460, username = Cosmopolitaine): Data Cleaning Program.

Weichong Ni

Shilan Tu

Mengran Cui (mc4575): (1) Stock price data cleaning. Identify data anomalies, including missing values & suspicoous stock movements. (2) Construct CAPM model. Find SP500 and treasury yield data, left merge with existing stock price using dates as identifier.  Calculated Betas using variance and covariance. Convert stock price to returns. Calculated daily CAPM returns for each stock. Compared predicted CAPM return vs. realized return. 
