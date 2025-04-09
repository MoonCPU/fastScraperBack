<h1 align="center" color="red">Web Scraping Financial Indicators Project</h1>


## Overview
This project is a web scraping application designed to extract financial indicators and historical net growth data from Brazilian stock market websites. The application exposes a FastAPI endpoint that provides this data, which can be accessed via specific API endpoints.


## Technologies Used
[![My Skills](https://skillicons.dev/icons?i=python,fastapi,github,githubactions,docker,aws,terraform)](https://skillicons.dev)
- FastAPI – High-performance web framework used to expose scraped data via RESTful API endpoints.
- Beautiful Soup 4 – Parses HTML from financial websites to extract indicators like P/L, ROE, Dividend Yield, etc.
- Docker – Ensures consistency across local development and deployment environments.
- AWS EC2 – Hosts the Dockerized FastAPI app.
- Terraform – Infrastructure as Code used to provision EC2, networking, Route 53, ACM, and CloudFront.
- GitHub Actions – CI/CD pipeline that:
    - Builds and pushes the Docker image to Docker Hub
    - Provisions AWS infrastructure with Terraform
 
## Deployment Flow
- Push to main branch triggers GitHub Actions:
    - Docker image is built and pushed to Docker Hub.
    - Terraform provisions the AWS infrastructure.
    - The latest Docker image is pulled and run.
- EC2 costs are minimized by destroying the infrastructure when not in use. The same CI/CD flow recreates everything from scratch as needed.


## API Endpoints
Access the application using the following endpoints:

- **Indicators**: Fetch financial indicators for a given stock code.
  - **URL**: `https://api.moondev-cloud.com/scrape/indicators/{stock_code}`
  - **Method**: GET
  - **Example**: `https://api.mooncloudops.com/scrape/indicators/cmig4`
  - **Returns**: Indicators such as P/L, P/VP, Dividend Yield, LPA, ROE, etc.


- **Net Growth**: Retrieve historical net growth data for a given stock code over the past 10 years.
  - **URL**: `https://api.moondev-cloud.com/scrape/netGrowth/{stock_code}`
  - **Method**: GET
  - **Example**: `https://api.mooncloudops.com/scrape/netGrowth/cmig4`
  - **Returns**: Data on net profit, net worth, net revenue, etc.



