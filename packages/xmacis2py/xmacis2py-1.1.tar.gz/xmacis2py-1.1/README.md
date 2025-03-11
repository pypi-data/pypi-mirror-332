![image](https://github.com/user-attachments/assets/fb5ecdf9-bd51-4243-be7d-92af0952bfd8) ![image](https://github.com/user-attachments/assets/da1b43c0-2b6a-4a5c-9eb4-f08b30cab42b)

<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/version.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/latest_release_date.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/latest_release_relative_date.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/platforms.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/license.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/downloads.svg" /> </a>


# xmACIS2Py
**Creating xmACIS2 Summary Graphics in Python**

### Jupyter Lab Tutorials

1) [Creating 30 and 90 Day Temperature and Precipitation Summaries for Riverside, CA Municipal Airport (KRAL)](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/KRAL.ipynb)
2) [Creating Summaries With Custom Dates Nov 1st - Nov 30th 2024 for Saint Paul, AK (PASN)](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/PASN.ipynb)

### Table Of Contents

1) [plot_temperature_summary(station, product_type)](#plot_temperature_summarystation-product_type)
2) [plot_precipitation_summary(station, product_type)](#plot_precipitation_summarystation-product_type)
3) [References](#references)


#### plot_temperature_summary(station, product_type)

This function plots a graphic showing the Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 
2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
   A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:
1) start_date (String) - Default=None. Enter the start date as a string (i.e. year-month-day/2025-02-22)
2) end_date (String) - Default=None. Enter the end date as a string (i.e. year-month-day/2025-02-22)

#### plot_precipitation_summary(station, product_type)

This function plots a graphic showing the Precipitation Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 
2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
   A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:
1) start_date (String) - Default=None. Enter the start date as a string (i.e. year-month-day/2025-02-22)
2) end_date (String) - Default=None. Enter the end date as a string (i.e. year-month-day/2025-02-22)


#### References


1) xmACIS2: https://www.rcc-acis.org/docs_webservices.html 

2) MetPy: May, R. M., Goebbert, K. H., Thielen, J. E., Leeman, J. R., Camron, M. D., Bruick, Z., Bruning, E. C., Manser, R. P., Arms, S. C., and Marsh, P. T., 2022: MetPy: A Meteorological Python Library for Data Analysis and Visualization. Bull. Amer. Meteor. Soc., 103, E2273-E2284, https://doi.org/10.1175/BAMS-D-21-0125.1.

3) NumPy: Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2. (Publisher link).

4) Pandas:
    author       = {The pandas development team},
    title        = {pandas-dev/pandas: Pandas},
    publisher    = {Zenodo},
    version      = {latest},
    doi          = {10.5281/zenodo.3509134},
    url          = {https://doi.org/10.5281/zenodo.3509134}
}
