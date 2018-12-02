# Tools-Project-Data-Cleaning

# What is This Project
This project deals with the daily stock prices of 500 stocks over the horizon of 5 years. We employed Python to perform (1) data cleaning, (2) CAPM validation, and (3) data analytics and visualization. 

# How to Use This Project
1. Data_Cleaning
Open the "Data_Cleaning.ipynb" file, and run cells in the order as they are arranged, then execute main() function. This program will ask you for a file name, and we have included a sample "all_stocks_5yr.csv" in the the repository, or you can use any .csv file with columns ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Name'). The program will automatically find missing data and suspicious values, it will output a file in the end, you can choose the name of the output file. 

The other programs will make use of the cleaned data this program creates, so please run this program first. 

You need to install a few modules on your computer before proceed to using this program. 
1. pandas
2. pandas_datareader
   please run the following command prompt: pip install pandas-datareader
   
# Credits
Contributors & Work Contributed :

Yuxuan Zheng yz3460

Weichong Ni

Shilan Tu

Mengran Cui (mc4575): (1) Stock price data cleaning. Identify data anomalies, including missing values & suspicoous stock movements. (2) Construct CAPM model. Find SP500 and treasury yield data, left merge with existing stock price using dates as identifier.  Calculated Betas using variance and covariance. Convert stock price to returns. Calculated daily CAPM returns for each stock. Compared predicted CAPM return vs. realized return. 
