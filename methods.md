# About Martha's Vineyard Coastal Observatory

The Martha's Vineyard Coastal Observatory (MVCO) Air-Sea Interaction Tower (ASIT) is located at 41.325 N, 70.567 W. See https://mvco.whoi.edu/about/ for more site information. Samples were collected in the vicinity of the tower. Early in the time series, samples were also collected from along- and cross-shore transects nearby. 

Starting in 2003, a monthly water sample has been collected at MVCO. The sample is typically collected using a CTD rosette or bucket during a day trip on a coastal vessel such as the R/V Tioga. Starting in February 2018, 4 of the monthly MVCO water samples per year were collected as part of a larger field sampling campaign during Northeast U.S. Shelf Long-Term Ecological Research project (NES-LTER) quarterly seasonal transect research cruises. 

Transect cruise samples can be differentiated from standard coastal day trips using the event number and event number Niskin parameters because they do not contain 'MVCO', but rather the cruise ID unique to that ship and cruise number. NES-LTER transect cruises always occur on a larger ship than is typical for monthly sample collection, however, the same MVCO time series CTD rosette collection, sampling protocol, and analysis methods have been used. 

# CTD Rosette Bottle and Bucket Sampling  

Samples were collected from the water column at multiple depths using Niskin bottles on a CTD rosette system. Some samples were collected at the surface with a bucket. In the event\_number\_niskin field of the data table, MVCO event number or transect cruise identifier is combined with a suffix indicating a bucket sample (_00), Niskin bottle number (e.g. _01), or, in limited cases, collaborating institution (_UNH). The depth for bucket samples is 0 m; some surface Niskin samples also have depth recorded as 0 m. 

# Nutrient Filtering Protocol

Prior to 2018, and for bucket samples: Wearing nitrile gloves, collect water from the Niskin or bucket with a clean bottle that is rinsed 3 times with the sample water. Rinse the full length of a B-D 60 ml LUER-LOKTM syringe with a small volume of sample water 3 times. Completely fill syringe with sample water and force 60 ml through a EMD Millipore sterile Sterivex 0.22 um filter. Then refill the syringe.

2018 to present: Wearing nitrile gloves, connect AcroPak 200 Capsule with Super Membrane 0.2 um filter with barb and tubing to Niskin spigot and fill with water. Rinse filter with 3 times the volume of the filter. Then refill the filter.

All samples: Then, without touching filter to sample vial (acid-washed scintillation vial 20 ml), rinse sample vial with 5 ml of filtered sample water 3 times. For each rinse, replace the cap and shake vigorously. Filter 17 ml of sample directly into the sample vial and replace the cap and proceed to the next sample. Store samples in a -20 deg C freezer and keep frozen until analysis. If applicable, flush AcroPak filter with milli-Q water and refrigerate for using on next cast (AcroPak filter may process up to 20 liters).

# WHOI Nutrient Facility Sample Analysis

Samples are stored at -20 deg C until submitted to the Woods Hole Oceanographic Institution's Nutrient Analytical Facility (https://web.whoi.edu/nutrient/) which operates a four-channel segmented flow SEAL AA3 HR Autoanalyzer. Prior to 2013, the facility utilized a Lachat Quickchem 8000 automated flow-through analyzer. Methods for both instruments were exactly the same. Duplicates and spiked additions are run for quality control. Standards are made daily and Certified Reference material is run daily to ensure the standards and/or reagents are good. If the samples fall outside of the duplicate or spike addition quality control they are rerun until they fall within quality control parameters. Precision is 0.001 micromoles per liter. The detection limit for all nutrient types prior to April 2012 was <0.05 micromolar. From April 2012 to present, the micromolar detection limit is on a per nutrient basis as the following: ammonium <0.015, silicate <0.03, phosphate <0.009, and nitrate plus nitrite <0.04. 

# Data Cleaning

All Below Detection Limit values were set to zero. Event numbers with no nutrient samples were omitted. Data assembly, cleaning, and metadata assembly were performed in R Markdown. Further documentation can be found on GitHub, at https://github.com/WHOIGit/nes-lter-nutrient-mvco. 

# Quality Assurance

We assured that the geographic and temporal coverage of the clean data table were within expected ranges. We confirmed that values matched the previous version of this data package. For each nutrient we checked differences between replicates, visually inspected plotted values, and performed a range check. We provided an IODE quality flag for the phosphate data to identify a small number of samples with possible contamination (quality flag 3 for questionable). For transect cruises in version 4, phosphate quality is unevaluated (quality flag 2). All other samples are considered good quality.  

# Related Packages

Dissolved inorganic nutrient data for NES-LTER transect cruises, which cover a larger geographic area of the same region, are in the following package:

Sosik, H.M., E. Crockford, and E. Peacock. 2021. Dissolved inorganic nutrients from NES-LTER Transect cruises, including 4 macro-nutrients from water column bottle samples, ongoing since 2017 ver 2. Environmental Data Initiative. https://doi.org/10.6073/pasta/ec6e5c76c7ad4e0da0a8d1cec84fa3f5 (Accessed 2024-04-16).

