# Tools-Project-Data-Cleaning

# What is This Project
This project tries to present a program that takes raw S&P 500 stock data (in .csv format) and return a cleaned and corrected version of it for future data analysis. 

# How to Use This Project
First, Open the "Data_Cleaning.ipynb" file, and run cells in the order as they are arranged, then execute main() function. This program will ask you for a file name, and we have included a sample "all_stocks_5yr.csv" in the the repository, or you can use any .csv file with columns ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Name'). The program will automatically find missing data and suspicious values, it will output a file in the end, you can choose the name of the output file. 

You need to install a few modules on your computer before proceed to using this program. 
1. pandas
2. pandas_datareader
   please run the following command prompt: pip install pandas-datareader
   
# Credits
Contributor:
Yuxuan Zheng yz3460
Weichong Ni
Shilan Tu
Mengran Cui
