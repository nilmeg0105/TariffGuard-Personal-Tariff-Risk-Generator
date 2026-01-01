# Project Title
**ScrapeX – Job & Internship Market Intelligence Platform**

## Problem Statement
Job seekers and students often rely on fragmented job portals to understand current hiring trends, required skills, and location-based opportunities. Manually collecting and analyzing such data is time-consuming, error-prone, and does not scale.

ScrapeX addresses this problem by automatically extracting job and internship listings from multiple public job sources, processing the data into structured formats, and presenting actionable insights through an intuitive web interface and Excel-based analytics dashboard.

## Objectives
- Automate extraction of job and internship data from public job listing websites.
- Support both static and dynamically rendered web pages.
- Enable non-technical users to trigger scraping and view results via UI and Excel.
- Provide clean, structured, and analyzable datasets for market intelligence.

## Core Features

### 1. Intelligent Web Scraping Engine
- Static page scraping using BeautifulSoup
- Dynamic page scraping using Selenium (headless browser)
- Pagination and infinite scroll handling
- Error handling and logging

### 2. Auto Page-Type Detection (Advanced Feature)
- Automatically determine whether a webpage is static or JavaScript-rendered
- Dynamically switch between BeautifulSoup and Selenium

### 3. Web-Based User Interface
- Input job role, location, and target website URL
- Select scraping mode (Auto / Static / Dynamic)
- Preview extracted data before export
- Download results in Excel, CSV, or JSON format

### 4. Data Cleaning & Processing
- Removal of duplicate listings
- Normalization of skills, locations, and experience fields
- Handling missing or inconsistent data
- Timestamped dataset generation

### 5. Excel + VBA Automation
- Excel macro-enabled dashboard (.xlsm)
- One-click “Refresh Job Data” button
- Automated pivot tables and charts:
  - In-demand skills analysis
  - Location-wise job distribution
  - Internship vs full-time ratio
- Sheet separation for raw data and processed data

## Target Users
- Students preparing for placements
- Job seekers and career analysts
- Academic researchers studying employment trends

## Technology Stack
- **Backend:** Python, Flask
- **Web Scraping:** BeautifulSoup, Selenium
- **Frontend:** HTML, CSS, JavaScript
- **Data Processing:** Pandas
- **Automation & Analytics:** Excel VBA
- **Output Formats:** Excel, CSV, JSON

## Expected Outcomes
- A fully functional end-to-end job market intelligence system
- A reusable scraping framework adaptable to multiple websites
- A professional-grade Excel analytics dashboard
- A resume-worthy full-stack automation project with real-world applicability

## Ethical Considerations
- Scraping limited to publicly accessible data
- Respect for robots.txt and reasonable request delays
- No authentication bypass or private data collection

## Project Deliverables
- Source code repository with documentation
- Web-based scraping interface
- Excel VBA-enabled analytics dashboard
- Sample datasets and logs