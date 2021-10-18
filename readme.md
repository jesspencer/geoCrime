# GEO CRIME
Summary:
- Python code that pulls GeoJSON data from an API and converts it to Shapefile format.
- Learning tool used for geospatial data formats as well as the site used to generate data for testing [geojson](https://geojson.io/)  
- Open Data DC – has an API where GeoJSON data was obtained. [DCGIS](https://opendata.dc.gov/datasets/DCGIS::crime-incidents-in-2011/api)

Note API Data Requested: 
- The Open Data DC site gives the clipboard url for api data from 2011, which is associated with 35 in the url given:: 
 [https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/35/query?where=1%3D1&outFields=*&outSR=4326&f=json](https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/35/query?where=1%3D1&outFields=*&outSR=4326&f=json) 
- The first part directs to the request to the part of the site that responds to API calls::
[https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/](https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/) 
- This project looks at crime incidents reported in the last 30 days, which comes from page 8 for site id instead of page id 35.

## REQUIREMENTS
- python 3.7
- `python pip install pandas`
- `python pip install requests`
- `python pip install fiona`

## RUNNING DOCUMENTATION LOCALLY:
1. Create a VM; here are the steps [Creating_A_VM](https://github.com/jesspencer/Good-Grub/blob/master/Creating_A_VM.md)
2. Run the virtual environment
3. Clone the project https://github.com/jesspencer/geoCrime
4. Start the code to produce .shp file (other files are produced by the code as well but the .shp is resulting file needed)

## RESULTS
- To confirm results of .shp file created one could download QGIS [https://www.qgis.org/en/site/forusers/download.html#](https://www.qgis.org/en/site/forusers/download.html#) to confirm results:
![data_visual_picture](https://github.com/jesspencer/geoCrime/blob/master/qgis_pic.png?raw=true)
- Using the learning tool geojason one can use the .csv file created within the project to confirm results
![data_visual_picture](https://github.com/jesspencer/geoCrime/blob/master/geojason_io_pic.png?raw=true)
