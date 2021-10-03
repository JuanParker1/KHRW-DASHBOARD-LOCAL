import pandas as pd
import numpy as np
import geopandas as gpd
import jalali
import statistics
import plotly.graph_objects as go
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import voronoi_diagram as svd
from shapely.wkt import loads as load_wkt
from datetime import datetime



# Modify Date And Water Table
# Date Type: 
#   1.Gregorian (Text): 2000-11-1
#   2.Persian (Text): 1399-1-1
# Date & Value:
#   Column of Pandas Dataframe
def convert_to_day_15(info, date, value, date_type="persian"):
    """[summary]

    Args:
        info ([type]): [description]
        date ([type]): [description]
        value ([type]): [description]
        date_type (str, optional): [description]. Defaults to "persian".

    Returns:
        [type]: [description]
    """
    df = info.copy()
    if date_type == "gregorian":
        df["DATE_GREGORIAN"] = date.apply(pd.to_datetime)
        df["DATE_PERSIAN"] = list(
            map(
                lambda i: jalali.Gregorian(i.date()).persian_string(),
                df["DATE_GREGORIAN"]
            )
        )
    elif date_type == "persian":
        df["DATE_PERSIAN"] = date
        df["DATE_GREGORIAN"] = list(
            map(
                lambda i: jalali.Persian(i).gregorian_string(),
                df["DATE_PERSIAN"]
            )
        )
        df["DATE_GREGORIAN"] = df["DATE_GREGORIAN"].apply(pd.to_datetime)    
    else:
        pass
    df["VALUE"] = value        
    df["DELTA_DAY"] = df["DATE_GREGORIAN"].diff().dt.days
    df["DATE_PERSIAN_NEW"] = list(
        map(
            lambda i: f"{int(i.split('-')[0])}-{int(i.split('-')[1])}-{15}",
            df["DATE_PERSIAN"]
        )
    )
    df["DATE_GREGORIAN_NEW"] = list(
        map(
            lambda i: jalali.Persian(i).gregorian_string(),
            df["DATE_PERSIAN_NEW"]
        )
    )
    df["DATE_GREGORIAN_NEW"] = df["DATE_GREGORIAN_NEW"].apply(pd.to_datetime)
    df["VALUE_NEW"] = df["VALUE"]
    A = []
    A.append(df["VALUE"][0])
    for i in range(1, len(df)):
        if int(df["DATE_PERSIAN"][i].split('-')[2]) >= 15:
            NEW_VALUE = df["VALUE"][i-1] + ((((df["DATE_GREGORIAN_NEW"][i] - df["DATE_GREGORIAN"][i-1]).days) / ((df["DATE_GREGORIAN"][i] - df["DATE_GREGORIAN"][i-1]).days)) * (df["VALUE"][i] - df["VALUE"][i-1]))
            A.append(NEW_VALUE)
        else:
            NEW_VALUE = df["VALUE"][i] + ((((df["DATE_GREGORIAN_NEW"][i] - df["DATE_GREGORIAN"][i]).days) / ((df["DATE_GREGORIAN"][i+1] - df["DATE_GREGORIAN"][i]).days)) * (df["VALUE"][i+1] - df["VALUE"][i]))
            A.append(NEW_VALUE)
    df["VALUE_NEW"] = A
    return df


def create_date_day15(min, max):
    """[summary]

    Args:
        min ([type]): [description]
        max ([type]): [description]

    Returns:
        [type]: [description]
    """
    result = []
    min_list = list(map(lambda x: int(x), min.split("-")))
    max_list = list(map(lambda x: int(x), max.split("-")))
    for y in range(min_list[0], max_list[0] + 1):
        for m in range(1, 13):
            result.append(f"{y}-{m}-15")

    result = pd.DataFrame(
        {"DATE_PERSIAN" : result}
    )
    result['DATE_GREGORIAN'] = result.apply(
        lambda x: jalali.Persian(x["DATE_PERSIAN"]).gregorian_string(), 
        axis=1
    )
    result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)
    result = result[result["DATE_GREGORIAN"] >= pd.to_datetime(jalali.Persian(min).gregorian_string())]
    result = result[result["DATE_GREGORIAN"] <= pd.to_datetime(jalali.Persian(max).gregorian_string())]
    result["DATE_GREGORIAN"] = result["DATE_GREGORIAN"].apply(pd.to_datetime)  
    return result


def dropHolesBase(plg):

	'''

	BASIC FUNCTION TO REMOVE / DROP / FILL THE HOLES.

	PARAMETERS:

		plg: plg WHO HAS HOLES / EMPTIES.
			Type: shapely.geometry.MultiPolygon OR shapely.geometry.Polygon

	RETURNS:
		A shapely.geometry.MultiPolygon OR shapely.geometry.Polygon object
	

	'''

	if isinstance(plg, MultiPolygon):

		return MultiPolygon(Polygon(p.exterior) for p in plg)

	elif isinstance(plg, Polygon):

		return Polygon(plg.exterior)


def dropHoles(gdf):

	'''

	REMOVE / DROP / FILL THE HOLES / EMPTIES FOR ITERMS IN GeoDataFrame.
	
	PARAMETERS:
		gdf:
			Type: geopandas.GeoDataFrame

	RETURNS:
		gdf_nohole: GeoDataFrame WITHOUT HOLES
			Type: geopandas.GeoDataFrame
	
	'''

	gdf_nohole = gpd.GeoDataFrame()

	for g in gdf['geometry']:

		geo = gpd.GeoDataFrame(geometry=gpd.GeoSeries(dropHolesBase(g)))

		gdf_nohole=gdf_nohole.append(geo,ignore_index=True)

	gdf_nohole.rename(columns={gdf_nohole.columns[0]:'geometry'}, inplace=True)

	gdf_nohole.crs = gdf.crs

	gdf.rename(columns={'geometry': 'geometry_old'}, inplace=True)

	gdf["geometry_new"] = gdf_nohole

	gdf.rename(columns={'geometry_new': 'geometry'}, inplace=True)

	gdf.drop(['geometry_old'], axis=1, inplace=True)

	return gdf


def thiessen_polygons(gdf, mask):

	'''

	CREATE VORONOI DIAGRAM / THIESSEN POLYGONS:

	PARAMETERS:

		gdf: POINTS / POLYGONS TO BE USED TO CREATE VORONOI DIAGRAM / THIESSEN POLYGONS.
            Type: geopandas.GeoDataFrame

		mask: POLYGON VECTOR USED TO CLIP THE CREATED VORONOI DIAGRAM / THIESSEN POLYGONS.
			Type: GeoDataFrame, GeoSeries, (Multi)Polygon

	RETURNS:

		gdf_vd: THIESSEN POLYGONS
			Type: geopandas.geodataframe.GeoDataFrame
	
	'''
	
	gdf.reset_index(drop=True)

	# CONVERT TO shapely.geometry.MultiPolygon
	smp = gdf.unary_union

	# CREATE PRIMARY VORONOI DIAGRAM BY INVOKING shapely.ops.voronoi_diagram
	poly = load_wkt('POLYGON ((42 24, 64 24, 64 42, 42 42, 42 24))')
	smp_vd = svd(smp, envelope=poly)

	# CONVERT TO GeoSeries AND explode TO SINGLE POLYGONS
	gs = gpd.GeoSeries([smp_vd]).explode()

	# CONVERT TO GEODATAFRAME
	# NOTE THAT IF GDF WAS shapely.geometry.MultiPolygon, IT HAS NO ATTRIBUTE 'crs'
	gdf_vd_primary = gpd.geodataframe.GeoDataFrame(geometry=gs, crs=gdf.crs)
	
	# RESET INDEX
	gdf_vd_primary.reset_index(drop=True)
	
	# SPATIAL JOIN BY INTERSECTING AND DISSOLVE BY `index_right`
	gdf_temp = (gpd.sjoin(gdf_vd_primary, gdf, how='inner', op='intersects').dissolve(by='index_right').reset_index(drop=True))

	gdf_vd = gpd.clip(gdf_temp, mask)

	gdf_vd = dropHoles(gdf_vd)

	return gdf_vd


# Read Data And GeoInfo
xls = pd.ExcelFile('/home/pooya/w/KHRW-DASHBOARD-LOCAL/Flask/Explore/Data/CSV/HydrographData.xlsx')
Data = pd.read_excel(xls, sheet_name='Data')
GeoInfo = pd.read_excel(xls, sheet_name='GeoInfo')

# GeoInfo
COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
GeoInfo[COLs] = GeoInfo[COLs].apply(lambda x: x.str.rstrip())
GeoInfo[COLs] = GeoInfo[COLs].apply(lambda x: x.str.lstrip())

# Data
COLs = ['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME']
Data[COLs] = Data[COLs].apply(lambda x: x.str.rstrip())
Data[COLs] = Data[COLs].apply(lambda x: x.str.lstrip())

gdf = gpd.read_file("/home/pooya/w/KHRW-DASHBOARD-LOCAL/Flask/Explore/Data/GeoJson/Sarakhs_Points.geojson")
gdf = gdf.set_crs("EPSG:32641", allow_override=True)

mask = gpd.read_file("/home/pooya/w/KHRW-DASHBOARD-LOCAL/Flask/Explore/Data/GeoJson/Sarakhs_Aquifer.geojson")
mask = mask.set_crs("EPSG:32641", allow_override=True)


Data["DATE_GREGORIAN_RAW"] = Data["DATE_GREGORIAN_RAW"].apply(pd.to_datetime)

Data['DATE_CHECK'] = np.where(
    Data["DATE_PERSIAN_RAW"].isna(),
    np.where(
        Data["DATE_GREGORIAN_RAW"].isna(),
        np.NaN,
        "G"
    ),
    "P"  
)

Data['DATE_PERSIAN_RAW'] = Data.apply(
    lambda x: jalali.Gregorian(x["DATE_GREGORIAN_RAW"].date()).persian_string() if x["DATE_CHECK"] == "G" else x["DATE_PERSIAN_RAW"], 
    axis=1
)

Data['DATE_GREGORIAN_RAW'] = Data.apply(
    lambda x: jalali.Persian(x["DATE_PERSIAN_RAW"]).gregorian_string() if x["DATE_CHECK"] == "P" else x["DATE_GREGORIAN_RAW"], 
    axis=1
)

Data["DATE_GREGORIAN_RAW"] = Data["DATE_GREGORIAN_RAW"].apply(pd.to_datetime)


Data.drop(['DATE_CHECK'], axis=1, inplace=True)

Data.sort_values(
    by=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_GREGORIAN_RAW"], 
    inplace=True
)


# Remove NanN Data In Column "WATER_TABLE_RAW"
Data.dropna(
    subset=["WATER_TABLE_RAW"],
    inplace=True
)

Data.reset_index(
    inplace=True,
    drop=True
)

wt_date_converted = convert_to_day_15(
    info=Data[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME"]],
    date=Data["DATE_PERSIAN_RAW"],
    value=Data["WATER_TABLE_RAW"],
    date_type="persian"
)[["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN", "DATE_PERSIAN_NEW", "DATE_GREGORIAN", "DATE_GREGORIAN_NEW", "VALUE_NEW"]]

wt_date_converted.columns = ["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN_RAW", "DATE_PERSIAN", "DATE_GREGORIAN_RAW","DATE_GREGORIAN", "WATER_TABLE"]

Data = Data.merge(
    right=wt_date_converted,
    how="left",
    on=["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", "DATE_PERSIAN_RAW", "DATE_GREGORIAN_RAW"]
)

tmp = pd.DataFrame()

for mn in list(Data["MAHDOUDE_NAME"].unique()):
    for an in list(Data["AQUIFER_NAME"].unique()):
        for ln in list(Data["LOCATION_NAME"].unique()):
            df = Data[(Data["MAHDOUDE_NAME"] == mn) & (Data["AQUIFER_NAME"] == an) & (Data["LOCATION_NAME"] == ln)]
            date = create_date_day15(
                min = df.DATE_PERSIAN.min(),
                max = df.DATE_PERSIAN.max()
            )
            
            df = date.merge(
                df,
                how="left",
                on=["DATE_PERSIAN", "DATE_GREGORIAN"]
            )
            df["WATER_TABLE_LINEAR"] = df["WATER_TABLE"].interpolate(method='linear')
            # df["WATER_TABLE_LINEAR"] = df["WATER_TABLE_LINEAR"].interpolate(method='ffill', limit=3)
            # df["WATER_TABLE_LINEAR"] = df["WATER_TABLE_LINEAR"].interpolate(method='bfill', limit=3)
            df["WATER_TABLE_SPLINE"] = df["WATER_TABLE"].interpolate(method='akima')
            # df["WATER_TABLE_SPLINE"] = df["WATER_TABLE_SPLINE"].interpolate(method='ffill', limit=3)
            # df["WATER_TABLE_SPLINE"] = df["WATER_TABLE_SPLINE"].interpolate(method='bfill', limit=3)
            df["MAHDOUDE_NAME"] = mn
            df["MAHDOUDE_CODE"] = int(df["MAHDOUDE_CODE"].unique()[0])
            df["AQUIFER_NAME"] = an
            df["LOCATION_NAME"] = ln
            df["DATA_STATE"] = df["DATA_STATE"].fillna("M")
            df["STORAGE_COEFFICIENT_LOCATION"] = df["STORAGE_COEFFICIENT_LOCATION"].unique()[0]
            
            df = df[[
                "MAHDOUDE_NAME", "MAHDOUDE_CODE", "AQUIFER_NAME", "LOCATION_NAME",
                "DATE_GREGORIAN", "DATE_PERSIAN",
                "WATER_TABLE", "WATER_TABLE_LINEAR", "WATER_TABLE_SPLINE", "STORAGE_COEFFICIENT_LOCATION", "THISSEN_LOCATION", "THISSEN_AQUIFER",
                "DATA_STATE", "NO_MEASURE_CODE", "INFO",
                "DATE_GREGORIAN_RAW", "DATE_PERSIAN_RAW", "WATER_TABLE_RAW"	
            ]]

            tmp = pd.concat([tmp, df], axis=0)

Data = tmp.copy()

del tmp

import dask.dataframe as dd
import multiprocessing

# SELECT LEVEL
SELECTED_LEVEL = 'LEVEL_SRTM'

# SELECT HEAD
SELECTED_WATER_TABLE_LIST = ["", "_LINEAR", "_SPLINE"]
SELECTED_WATER_TABLE_LIST = [""]

# FILTER DATE
Data = Data[Data["DATE_GREGORIAN"] >= datetime.strptime("2001-10-01", '%Y-%m-%d')]

def f (df_raw):
    
    for SELECTED_WATER_TABLE in SELECTED_WATER_TABLE_LIST:
    
        df = df_raw.dropna(subset=[f"WATER_TABLE{SELECTED_WATER_TABLE}"])
        
        vd_result = gpd.GeoDataFrame()    
        gdf_d = gdf[gdf["LOCATION_NAME"].isin(df["LOCATION_NAME"])]
        
        # TODO: Find Better Way
        for i in range(len(mask)):
            mask_tmp = mask.iloc[[i]]
            gdf_d['CHECK'] = gdf_d['geometry'].apply(lambda x: mask_tmp.contains(x))
            gdf_tmp = gdf_d[gdf_d['CHECK']].reset_index(drop=True)
            
            if len(gdf_tmp) > 0:
                vd = thiessen_polygons(gdf_tmp, mask_tmp)
                vd.set_geometry(col='geometry', inplace=True)
                vd.set_crs("EPSG:32641", allow_override=True, inplace=True)
                vd[f"THISSEN_LOCATION{SELECTED_WATER_TABLE}"] = vd.geometry.area / 1000000
                vd["THISSEN_AQUIFER"] = [mask_tmp.geometry.area[0] / 1000000] * len(gdf_tmp)
                vd["DATE_PERSIAN"] = [df["DATE_PERSIAN"].unique()[0]] * len(gdf_tmp)

                vd_result = vd_result.append(vd, ignore_index=True)
                
    return vd_result


vd_result = dd.from_pandas(Data, npartitions=4*multiprocessing.cpu_count())\
    .groupby(by=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'DATE_GREGORIAN'])\
        .apply(f, meta=object)\
            .compute()

vd_result = vd_result.droplevel(['MAHDOUDE_NAME', 'AQUIFER_NAME', 'DATE_GREGORIAN'])




Data = Data.merge(
    right=vd_result[['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME', 'DATE_PERSIAN', SELECTED_LEVEL] + [f"THISSEN_LOCATION{SELECTED_WATER_TABLE}" for SELECTED_WATER_TABLE in SELECTED_WATER_TABLE_LIST] + ['THISSEN_AQUIFER']],
    how='left',
    on=['MAHDOUDE_NAME', 'AQUIFER_NAME', 'LOCATION_NAME', 'DATE_PERSIAN']
).sort_values(["MAHDOUDE_NAME", "AQUIFER_NAME", "LOCATION_NAME", 'DATE_GREGORIAN']).rename(columns={SELECTED_LEVEL: 'LEVEL'})


# THISSEN
Data["THISSEN_LOCATION"] = np.where(Data["THISSEN_LOCATION_x"].isna(), Data["THISSEN_LOCATION_y"], Data["THISSEN_LOCATION_x"])
Data["THISSEN_AQUIFER"] = np.where(Data["THISSEN_AQUIFER_x"].isna(), Data["THISSEN_AQUIFER_y"], Data["THISSEN_AQUIFER_x"])
