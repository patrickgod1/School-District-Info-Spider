# School-District-Info-Spider

This spider crawls GreatSchools.org for school district information. It can be used to scrape school district information from multiple or all 50 states. The output provides:

1. District Name
2. City
3. County
4. District Website
5. District Phone Number
6. Number of schools in the district
7. Grade Levels

## Getting Started
These instructions will help you get started with using the application.

### Built With
* [Python 3.6.5](https://docs.python.org/3/) - The scripting language used.
* [Scrapy](https://doc.scrapy.org/en/latest/intro/tutorial.html) - Web crawling framework to write spider to scrape site.

### Running the Spider
Run the following command to start the spider:
```
scrapy runspider greatschools_org.py
```
To run the spider and output results in a CSV file:
```
scrapy runspider greatschools_org.py -o output.csv
```

## Screenshot
Below is a screenshot of the resulting CSV file from running the spider on (https://www.greatschools.org/schools/districts/California/CA/)
![californiaschooldistricts](https://user-images.githubusercontent.com/41496510/50580316-ec13fd80-0e01-11e9-9e85-7b3aab3c0a37.png)

## Authors
* **Patrick Yu** - *Initial work* - [patrickgod1](https://github.com/patrickgod1)
