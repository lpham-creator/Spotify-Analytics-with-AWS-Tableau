# Spotify-Analytics-with-AWS-Tableau

## Overview

This project automates a data engineering process using AWS cloud services to manage and analyze Spotify user statistics data. The goal was to create a seamless pipeline that extracts, transforms, and loads (ETL) data into AWS S3, then uses Amazon Athena for querying. The processed data is then visualized using Tableau to create an interactive dashboard.

Kaggle data: https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023
My AWS data for public use: https://spotifyproject-data.s3.us-east-1.amazonaws.com/data-warehouse/
My Tableau Dashboard: https://public.tableau.com/views/SpotifyDashboard_17399384677620/SpotifyDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Technologies Used
- **AWS S3**: Storage of raw and processed data
- **AWS Glue**: Extract, transform, and load (ETL) data processing
- **Amazon Athena**: SQL querying of the data
- **Tableau**: Data visualization and dashboard creation

## Key Features

- **Automated ETL Pipeline**: Utilized AWS Glue to automate data extraction, transformation, and loading (ETL) from raw data into a structured format stored in S3.
- **Data Storage on AWS S3**: Raw and processed Spotify user statistics data is stored securely in S3 buckets.
- **Data Querying with Amazon Athena**: Used Athena to efficiently query the data stored in S3, making it ready for visualization.
- **Interactive Tableau Dashboard**: Connected Tableau to the S3 bucket to visualize user statistics in an interactive, easy-to-understand dashboard, showcasing Spotify user behavior trends over different years.

## Key Learnings

- **AWS Glue**: Gained hands-on experience with AWS Glue, learning how to set up ETL jobs, work with crawlers, and manage schemas for structured data.
- **Data Storage and Querying**: Deepened my understanding of cloud storage solutions (AWS S3) and learned how to perform serverless querying using Amazon Athena.
- **Tableau Integration**: Learned how to connect Tableau to cloud-based data sources, visualize the data, and build user-friendly, interactive dashboards.

## Key Struggles

- **Data Transformation Complexity**: During the ETL process, some of the data transformations required advanced logic, which initially posed challenges in debugging and managing schema changes.
- **Connection Setup Between Tableau and AWS**: Establishing a seamless connection between Tableau and the S3 bucket was tricky due to authentication issues and permissions, requiring multiple iterations of adjustments.

## Future Improvements

- **Optimize ETL Jobs**: Enhance data transformation logic to handle larger datasets more efficiently.
- **Refine Tableau Dashboard**: Add more interactivity and customization options to the dashboard for deeper insights into the data.
- **Automate Data Refresh**: Set up a scheduled refresh for the Tableau dashboard to automatically update when new data is added to the S3 bucket.
