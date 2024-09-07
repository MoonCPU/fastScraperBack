<h1 align="center" color="red">Web Scraping Financial Indicators Project</h1>


## Overview
This project is a web scraping application designed to extract financial indicators and historical net growth data from Brazilian stock market websites. The application exposes a FastAPI endpoint that provides this data, which can be accessed via specific API endpoints.


## Technologies Used
[![My Skills](https://skillicons.dev/icons?i=python,fastapi,github,githubactions,docker,aws)](https://skillicons.dev)
- Beautiful Soup 4 (Python): Used for web scraping to extract financial indicators such as P/L, P/VP, Dividend Yield, LPA, ROE, and more from the internet.
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python. It serves the scraped data through RESTful endpoints.
- GitHub Actions: For CI/CD, automates the testing, building, and deployment processes. The pipeline ensures that code changes are automatically tested and, if successful, builds and pushes a Docker image to Docker Hub.
- Docker: Containerization of the application to ensure consistent environments and easy deployment.
- AWS Lambda: Hosts the application, allowing it to run serverlessly without managing infrastructure.
- Amazon Route 53: Used to register a domain and manage DNS routing for the application.
- Amazon API Gateway: Provides a RESTful API interface to expose the Lambda function to the internet.

  
## API Endpoints
Access the application using the following endpoints:

- **Indicators**: Fetch financial indicators for a given stock code.
  - **URL**: `https://api.mooncloudops.com/scrape/indicators/{stock_code}`
  - **Method**: GET
  - **Example**: `https://api.mooncloudops.com/scrape/indicators/cmig4`
  - **Returns**: Indicators such as P/L, P/VP, Dividend Yield, LPA, ROE, etc.


- **Net Growth**: Retrieve historical net growth data for a given stock code over the past 10 years.
  - **URL**: `https://api.mooncloudops.com/scrape/netGrowth/{stock_code}`
  - **Method**: GET
  - **Example**: `https://api.mooncloudops.com/scrape/netGrowth/cmig4`
  - **Returns**: Data on net profit, net worth, net revenue, etc.

**Important Note**: 

Please be aware that since the API fetches data from external sources, there may be a delay of up to 3 seconds before data is returned. This delay is due to the time required to retrieve and process the data from the source.

When using the API, ensure you use a valid Brazilian stock code. Examples of valid stock codes include `cmig4`, `kepl3`, `petr4`, etc. Using incorrect or non-existent stock codes will result in errors or empty responses.

  
## Deployment Process

1. CI/CD Pipeline: Set up with GitHub Actions to automate testing, building, and deployment.
2. Docker: Build a Docker image upon successful tests and push to Docker Hub.
3. AWS Lambda: Deploy the Dockerized application as a Lambda function.
4. API Gateway: Configure API Gateway to expose the Lambda function via HTTP endpoints.
5. Route 53: Register a domain and set up DNS routing to the API Gateway.


## Future Enhancements

Terraform Integration: Plan to use Terraform for automating the deployment process to AWS Lambda, streamlining infrastructure management and updates.

