# GEO CRIME
This Python library contains:
- Python code that pulls GeoJSON data from an API and converts it to Shapefile format.
- Learning tool used for geospatial data formats as well as a way to generate geospatial data for testing was [geojson](https://geojson.io/)  
- Open Data DC – has an API where GeoJSON data was obtained. [DCGIS](https://opendata.dc.gov/datasets/DCGIS::crime-incidents-in-2011/api)
.. The site gives the clipboard url for api data from 2011, which is associated with 35 in the url given:
.. url given::
https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/35/query?where=1%3D1&outFields=*&outSR=4326&f=json 

- The first part directs to the request to the part of the site that responds to API calls:
.. first part::
 [https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/](https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/) 
## REQUIREMENTS
- python 3.7
- pandas
- requests
- fiona

## RUNNING DOCUMENTATION LOCALLY:
1. Create a VM; here are the steps [Creating_A_VM](https://github.com/jesspencer/Good-Grub/blob/master/Creating_A_VM.md)
2. Run the virtual environment
3. Clone the project https://github.com/jesspencer/calling_api
4. Start the code to produce the latest Bar Chart visualization from GitHub's API. The results will show as a html in your browser.

## RESULTS
![data_visual_picture](https://github.com/jesspencer/calling_api/blob/master/python_repos.png?raw=true)