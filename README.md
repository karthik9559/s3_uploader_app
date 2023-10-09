# S3 Uploader App

## Author

Karthik Tanpure

## Description

This app is basically uploading file to the s3 bucket 

## How to Run

```docker-compose up --build```

**Test Scenarios:**

    - Open the `nginx.conf` file.
    - Comment or uncomment the line `client_max_body_size 200m;`.
    - Restart the Docker container (stop and then run again).

    Experiment with different scenarios to observe the behavior of the application in relation to the maximum upload size.
