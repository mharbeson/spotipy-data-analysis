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



- Execute main.py passing user name as first requirement. (Example user ID provided):
```
python3 main.py 1236194609
```


- 
    - if using Windows PowerShell: `venv\Scripts\Activate.ps1`
    - if using Linux or Mac: `venv/bin/activate`
- Run `pip install -r requirements.txt` to install the required packages.

### Mac

- 

### Windows

-

## Notes

- 
- 

## Project Requirements

-
-



