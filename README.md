# Web Scraping Real Estate Data from Dynamic Website
Data is one of the most valuable assets a business can possess and sits at the core of data science and data analysis. Web scraping is a data acquisition technique 
that has become a hot topic among those with rising demands for big data. In this project, we create a web scraper to extract data from a dynamic webpage, which is 
a page that displays different content for different users while retaining the same layout and design - data on the webpage can be mutable or changeable. 

## Installation & Usage
- Clone this repository to your computer
- [Create and actiavate a virtual environment](https://docs.python.org/3/library/venv.html) 
- Install the requirements with the following command: `pip install -r requirements.txt` 
- Navigate to the spider directory `cd web-scraping-real-estate-data/bradvisors` from your terminal
- Run the following command to execute the scraper: `scrapy crawl bradvisors -o data.csv`
  - The scraper will crawl the first 5 pages of [Boston Realty Advisors](https://bradvisors.com/listings/) listings
  - The `-o data.csv` command will create a CSV file in the root directory of the scrapy project. 
  
## Extending This Project 
Here are some ideas to extend this work: 
- Extract more data from each property (i.e. Broker name and details) 
- Data analysis using listings

## Articles About this Project
- Data Acquisition: Scraping Real-Estate Data with Scrapy (Coming soon)
