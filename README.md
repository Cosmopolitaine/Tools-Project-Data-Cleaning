# Tools-Project-Data-Cleaning

# What is This Project
This project tries to clean capital market data in .csv form and use the cleaned data to do conduct data analysis. 

# How to Use This Project
1. Data_Cleaning
Open the "Data_Cleaning.ipynb" file, and run cells in the order as they are arranged, then execute main() function. This program will ask you for a file name, and we have included a sample "all_stocks_5yr.csv" in the the repository, or you can use any .csv file with columns ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Name'). The program will automatically find missing data and suspicious values, it will output a file in the end, you can choose the name of the output file. 

The other programs will make use of the cleaned data this program creates, so please run this program first. 

You need to install a few modules on your computer before proceed to using this program. 
1. pandas
2. pandas_datareader
   please run the following command prompt: pip install pandas-datareader
   
# Credits
Contributors:

Yuxuan Zheng yz3460

Weichong Ni

Shilan Tu

Mengran Cui
