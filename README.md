# Soundscaping
## Overview

A project dedicated to analyzing music trends & characteristics with the sole purpose of identifying the aspects that contribute to a chart-topping hit song

To get started, visit a consolidated report of my findings at `results.ipynb`

For a deeper dive into the data, with little organization but many thoughts and initial discoveries, visit `exploration.ipynb`

## Sourced Data

**AOTY Top 5000**: Contains 5000 user-rated albums from Album of the Year (AOTY) as of 2024.

*  [AOTY Dataset on Kaggle](https://www.kaggle.com/datasets/tabibyte/aoty-5000-highest-user-rated-albums)

**Spotify Top 100 Dataset**: Contains the top 100 most streamed songs on Spotify as of 2021.

* [Spotify Top 100 Dataset on Kaggle](https://www.kaggle.com/datasets/pavan9065/top-100-most-streamed-songs-on-spotify)

## Usage

1. **Setup**:
   - Install [Python 3.12](https://www.python.org/downloads/) and the required packages:
     ```sh
     pip install -r requirements.txt
     ```

2. **Environment Variables**:
   - Create a `.env` file in the root directory with [Spotify API credentials](https://developer.spotify.com/documentation/web-api):

     ```properties
     SPOTIFY_CLIENT_ID=your_client_id
     SPOTIFY_CLIENT_SECRET=your_client_secret
     ```
## License

This project is licensed under the MIT License. Feel free to use this work in any way for absolutely anything. See the [LICENSE](LICENSE) file for details.