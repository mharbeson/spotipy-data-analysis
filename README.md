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
- [Notes](#Notes)
- [Project Requirements](#project-requirements)



## Requirements

- Python 3.8.10
- Aquire a Spotify API Client ID and Secret ID from: https://developer.spotify.com/documentation/web-api/quick-start
- User Spotify ID
    - This can be found either on Spotify's website by logging in, or in the hyperlink to a user's profile.
    <img src=assets/accountoverview.png width="100%">
    - Bold text below is the location of a user's ID in a hyperlink.
    - https://open.spotify.com/user/**1236194609**?si=a152edcdd8c34981

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
vim /etc/environment
```

```
# /etc/environment
SPOTIPY_CLIENT_ID='56eb326*************************'
SPOTIPY_CLIENT_SECRET='cfd2cd*************************'
SPOTIPY_REDIRECT_URI='https://google.com/'
```



- Execute main.py passing user name as first requirement. If not user ID is provided, it will use my personal ID:
```
python3 main.py
```


- 
    - if using Windows PowerShell: `venv\Scripts\Activate.ps1`
    - if using Linux or Mac: `venv/bin/activate`
- Run `pip install -r requirements.txt` to install the required packages.

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

- Add Spotify API Keys to environment variables:

```
export SPOTIPY_CLIENT_ID='56eb326*************************'
export SPOTIPY_CLIENT_SECRET='cfd2cd*************************'
export SPOTIPY_REDIRECT_URI='https://google.com/'
```

- Execute main.py passing user name as first requirement. If not user ID is provided, it will use my personal ID:
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

- Add Spotify API Keys to environment variables:

```
SET SPOTIPY_CLIENT_ID='56eb326*************************'
SET SPOTIPY_CLIENT_SECRET='cfd2cd*************************'
SET SPOTIPY_REDIRECT_URI='https://google.com/'
```

- Execute main.py passing user name as first requirement. If not user ID is provided, it will use my personal ID:
```
python3 main.py
```

## Notes

- Depending on the number of liked songs in a users library, this application may take 5-10 minutes to process the data. 
- 

## Project Requirements

- Category 1: Python Programming Basics:
    - Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
        - see
    - Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code.
        - see

- Category 2: Utilize External Data:
    - Connect to an external/3rd party API and read data into your app
        - see

- Category 3: Data Display
    - Visualize data in a graph, chart, or other visual representation of data.
        - see
    - Display data in tabular form
        - see

- Category 4: Best Practices
    - The program should utilize a virtual environment and document library dependencies in a requirements.txt file.

- Future Stretch Items
    - Add the ability to compare the listening habits of two users