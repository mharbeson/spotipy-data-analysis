# Data Analysis with Spotify API
<p align=center>
<a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
<img src="https://img.shields.io/badge/os-linux-brightgreen">
<img src="https://img.shields.io/badge/os-mac-brightgreen"></a>
<img src="https://img.shields.io/badge/os-windows-brightgreen"></a>
<br>
</p>

This application provides interesting data analysis about a users Spotify listening habits based on liked or :heart:ed tracks. Data is pulled using the Spotify API, manipulated, and presented to the end user.

<h1 align="center">
	Showcase
</h1>

<img src=assets/heatmap.png width="100%">
</p>


## Table of Contents

- [Requirements](#Requirements)
- [Install](#Install)
  - [Linux](#Linux)
  - [Mac](#Mac)
  - [Windows](#Windows)
- [Running](#Running)
- [Notes](#Notes)
- [Project Requirements](#project-requirements)



## Requirements

- Python 3.8.10
- A valid Spotify account with liked songs
- Aquire a Spotify API Client ID and Secret ID from: https://developer.spotify.com/dashboard/applications
- Users must have their email whitelisted to use my API Client ID and Secret ID. If generating a new API Client ID and Secret, users will need to add their own email. 
- Linux users will require python3-tk and python3-gi-cairo. These can be installed by:
```
apt-get install python3-tk python3-gi-cairo
```


## Install

### Linux

- Clone the repository: 
```
git clone https://github.com/mharbeson/spotipy-data-analysis.git
``` 

- Create and activate the virtual environment from the cloned directory:
```
python3 -m venv spotipy-data-analysis
source spotipy-data-analysis/bin/activate
```

- Install requirements:
```
cd spotipy-data-analysis
pip install -r requirements.txt
```

- Add Spotify API Keys to environment file:
```
vim .env
```

```
# .env
SPOTIPY_CLIENT_ID='56eb326*************************'
SPOTIPY_CLIENT_SECRET='cfd2cd*************************'
SPOTIPY_REDIRECT_URI='https://google.com/'
```

- Execute main.py. User will be prompted to paste the redirect URL into the application.
```
python3 main.py
```


### Mac

- Clone the repository: 
```
git clone https://github.com/mharbeson/spotipy-data-analysis.git
``` 

- Create and activate the virtual environment from the cloned directory:
```
python3 -m venv spotipy-data-analysis
source spotipy-data-analysis/bin/activate
```

- Install requirements:
```
cd spotipy-data-analysis
pip install -r requirements.txt
```

- Add Spotify API Keys to environment file:

```
# .env
SPOTIPY_CLIENT_ID='56eb326*************************'
SPOTIPY_CLIENT_SECRET='cfd2cd*************************'
SPOTIPY_REDIRECT_URI='https://google.com/'
```

- Execute main.py. User will be prompted to paste the redirect URL into the application.
```
python3 main.py 
```

### Windows

- Clone the repository: 
```
git clone https://github.com/mharbeson/spotipy-data-analysis.git
``` 

- Create and activate the virtual environment from the cloned directory:
```
python3 -m venv spotipy-data-analysis
source spotipy-data-analysis/bin/activate
```

- Install requirements:
```
cd spotipy-data-analysis
pip install -r requirements.txt
```

- Add Spotify API Keys to environment file:

```
# .env
SPOTIPY_CLIENT_ID='56eb326*************************'
SPOTIPY_CLIENT_SECRET='cfd2cd*************************'
SPOTIPY_REDIRECT_URI='https://google.com/'
```

- Execute main.py. User will be prompted to paste the redirect URL into the application.
```
python3 main.py
```

## Running
- After executing the program, a web browser will open and you will be prompted to login to your Spotify account. This account will be used to retrieve liked songs.


## Notes

- Depending on the number of liked songs in a users library, this application may take 5-10 minutes to process the data. 
- The Spotify API may limit the number of calls allowed by this application. Due to this, I have rate limited the calls to the first 500 tracks. 

## Project Requirements

- Category 1: Python Programming Basics:
    - Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
        - See function trackFeaturesGenerator()
    - Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code.
        - See main.py

- Category 2: Utilize External Data:
    - Connect to an external/3rd party API and read data into your app
        - See main.py

- Category 3: Data Display
    - Visualize data in a graph, chart, or other visual representation of data.
        - See function trackFeatureHeatmap()
    - Display data in tabular form
        - See function releaseYearHistogram()

- Category 4: Best Practices
    - The program should utilize a virtual environment and document library dependencies in a requirements.txt file.
        - See readme for requirements.txt

- Future Stretch Items
    - Add the ability to compare the listening habits of two users