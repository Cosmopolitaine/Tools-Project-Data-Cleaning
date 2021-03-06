# Capital Markets Data Cleaning and Analytics 

## Group: 
### Name: Coding the Tools  (Section 1)

## What is This Project
This project deals with the daily stock prices of 500 stocks over the horizon of 5 years. We employed Python to perform data cleaning, data analytics, and data visualization. 

### Data Cleaning: 
* Found missing data, wrong data (eg. unreasonable high or low price, too high or too low returns, stocksplits, etc.) after getting a rough view of potential wrong data with pandas. 
* Corrected them with webcrawller or mannually (for sharesplits). The output 'Clean_Data_Out.csv' would be used for later analysis and visualization. 

### Data Analysis:
* Generalized random portfolio using Dow Jones 30 and optimized the efficient frontier in CAPM model.
* Predicted stock price using basic Linear Regression Model upon splitted training and testing data from historical data.

### Data Visualization:
* Plotted histograms and historical stock price data for a rough view before cleaning data.
* plotted random portfolio and generalized the efficient frontier.
* Plotted chosen stock data and comparison of actual and predicted data in Linear Regression part.
                                

## Run Instruction
### 1. Data Cleaning
Open the "Data_Cleaning.ipynb" file, and run cells in the same order as they are arranged, then execute main() function. This program will ask you for a file name, and we have included a sample "all_stocks_5yr.csv" in the the repository, or you can use any .csv file with columns ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Name'). The program will automatically find missing data and correct suspicious values, it will output a file as a result, you then will be asked to type in the name of the output file. 
The other programs will make use of the cleaned data this program creates, so please run this program first. 

### 2. Data Analysis
Source Codes for data analysis are in 'CAPM_Regression_Data_Analysis.ipynb' and 'LinearRegression_Model.ipynb'. They make use of the Output data from data cleaning program. We have included an example of cleaned data 'Clean_Data_Out.csv' which is 'all_stock_5yr.csv' cleaned using the data cleaning program to be used in the data analysis part of the project. 

#### 1 CAPM model
Open 'CAPM_Regression_Data_Analysis.ipynb'.  In the first cell, input 'Clean_Data_Out' and 'Treasury Bill Yield Curve.csv'. Choose the stock you are interested in from the sp 500. Calculate the expected return using CAPM model. After that, generalize a random weight of the portfolio and visualize it. At last, optimize it and generalize efficient frontier using CAPM model. Also visualize the frontier.

#### 2. Stock Price Prediction with Linear Regression Model
Open "LinearRegression_Model.ipynb". In the second cell, input 'Clean_Data_Out' to read this csv file. Choose the stock you are interested in from the sp 500 in this third cell. Then simply run the cells in order and get the final plotting of prediction from this basic model.
   
### Contributors:

#### Yuxuan Zheng (uni = yz3460, username = Cosmopolitaine): 
(1) Responsible for the majority of Data Cleaning Part. 

(2) Cooperated in analyzing missing and abnormal data.

#### Weichong Ni (uni = wn2163, username = Weichong515): 
(1) Cooperated with Shilan Tu in getting a rough view of missing and potential wrong data before Data Cleaning.

(2) Prediction with Linear Regression.

#### Shilan Tu (uni=st3184,username=shyla1107): 
(1) Stock price data cleaning: Analyzed the high and low to find abnomal values; Found abnormal returns and concluded it come from stocksplit. 

(2) Change the mean, variance and covariance into rolling window version in CAPM model. 

(3) Generalized random portfolio then optimized it to find the efficient frontier in CAPM model. 

(4) Visualized the frontier.

#### Mengran Cui (uni = mc4575, username=mcui123): 
(1) Stock price data cleaning. Identify data anomalies, including missing values & suspicoous stock movements. 

(2) Construct CAPM model. Find SP500 and treasury yield data, left merge with existing stock price using dates as identifier.  Calculated Betas using variance and covariance. Convert stock price to returns. Calculated daily CAPM returns for each stock. Compared predicted CAPM return vs. realized return. 
