import os
import earthaccess
import netCDF4 as nc
from osgeo import gdal
import rasterio
import numpy as np
import xarray as xr
from rasterio.mask import mask
import hvplot.xarray
import holoviews as hv
import sys
import emit_tools
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
import folium
import math

fp = r"C:\Users\Nitro\Downloads\EMIT_L2A_RFL_001_20220903T163129_2224611_012.nc"
fp_mask = r"C:\Users\Nitro\Downloads\EMIT_L2A_MASK_001_20220903T163129_2224611_012.nc"


mask_parameters_ds = xr.open_dataset(fp_mask,engine = 'netcdf4', group='sensor_band_parameters')
mask_key = mask_parameters_ds['mask_bands'].to_dataframe()



# fig = plt.figure(figsize=(20, 50))
# gs = gridspec.GridSpec(ncols=3, nrows=len(mask_key), figure=fig)
#
# ds = emit_tools.emit_xarray(fp, ortho=False)
# mask_ds = emit_tools.emit_xarray(fp_mask, ortho=False)
#
# rgb_inds = np.array([np.nanargmin(abs(ds['wavelengths'].values - x)) for x in [650, 560, 470]])
# rgb = ds['reflectance'].values[:, :, rgb_inds]  # subset RGB
# rgb[rgb < 0] = np.nan
# rgb -= np.nanpercentile(rgb, 2, axis=(0, 1))[np.newaxis, np.newaxis, :]  # scale from 2-95 %
# rgb /= np.nanpercentile(rgb, 95, axis=(0, 1))[np.newaxis, np.newaxis, :]
#
# for _n in range(int(len(mask_key) / 2)):
#     ax = fig.add_subplot(gs[_n, 0])
#     plt.imshow(rgb)
#     plt.axis('off')
#     plt.title('RGB')
#
#     ax = fig.add_subplot(gs[_n, 1])
#     md = mask_ds['mask'].values[..., _n]
#     md[np.isnan(rgb[..., 0])] = np.nan
#     plt.imshow(md)
#     plt.axis('off')
#     plt.title(mask_key['mask_bands'][_n])
#
#     ax = fig.add_subplot(gs[_n, 2])
#     md = mask_ds['mask'].values[..., _n + int(len(mask_key) / 2)]
#     md[np.isnan(rgb[..., 0])] = np.nan
#     plt.imshow(md)
#     plt.axis('off')
#     plt.title(mask_key['mask_bands'][_n + int(len(mask_key) / 2)])
#
# fig = plt.figure()
# md = mask_ds['mask'].values[:,:,list(mask_key['mask_bands']).index('AOD550')]
# md[np.isnan(rgb[...,0])] = np.nan
# plt.imshow(md, vmin=np.nanpercentile(md,2),vmax=np.nanpercentile(md,98))
# plt.title('AOD550')
#
# fig = plt.figure()
# md = mask_ds['mask'].values[:,:,list(mask_key['mask_bands']).index('H2O (g cm-2)')]
# md[np.isnan(rgb[...,0])] = np.nan
# plt.imshow(md, vmin=np.nanpercentile(md,2),vmax=np.nanpercentile(md,98))
# plt.title('H2O (g cm-2)')

# flags = [0,1,3]

# mask = emit_tools.quality_mask(fp_mask,flags)

# flags = [0,1,3,4]
# mask = emit_tools.quality_mask(fp_mask,flags)
# fig = plt.figure(figsize=(15,15))
# gs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
#
# ax = fig.add_subplot(gs[0, 0])
# plt.imshow(rgb)
# plt.scatter(1200,1200,c='red',marker='+')
#
# ax = fig.add_subplot(gs[0, 1])
# plt.imshow(mask)
# plt.scatter(1200,1200,c='red',marker='+')
#
# ax = fig.add_subplot(gs[1, :])
# plt.plot(ds['wavelengths'],ds['reflectance'].values[1200,1200,:])
# plt.xlabel('Wavelengths [nm]')
# plt.ylabel('Reflectance')

#ds = emit_tools.emit_xarray(fp, ortho=True, qmask=mask)

#ds.sel(wavelengths=650, method='nearest').hvplot.image(cmap='viridis', aspect = 'equal', frame_width=500, rasterize=True)

#ds.to_netcdf(r'C:\Users\Nitro\Downloads\example_quality_nc_out.nc')
# Example for Opening
# ds = xr.open_dataset('../data/example_quality_nc_out.nc')

#bmask = emit_tools.band_mask(fp_mask)

xr = emit_tools.emit_xarray(fp)
# band_xr = band_mask(filepath)
# write_envi(out_xr, r'C:\Users\Nitro\Downloads')
# shape_gdf = gpd.read_file(geodatasets.get_path('geoda.malaria'))
# ds = raw_spatial_crop(out_xr, shape_gdf)
longitude = xr.coords['lon'].values
latitude = xr.coords['lat'].values
# longitude, latitude = emit_tools.coord_vects(ort_xr)


# Sample data
data = []
data2 = []

for i in range (min(len(longitude), len(latitude))):
    for j in range (min(len(longitude[i]), len(latitude[i]))):
        if j > 100:
            break
        print(latitude[i][j], ' ', longitude[i][j])
        if j > 0:
            if math.floor(longitude[i][j]) != math.floor(longitude[i][j - 1]):
                data.append({"latitude": latitude[i][j], "longitude": longitude[i][j], "value": "Dust"})
        else:
            data.append({"latitude": latitude[i][j], "longitude": longitude[i][j], "value": "Dust"})

def predict():

    for i in range (440, 460):
        for j in range (630, 650):
            print(i/10, ' ', j/10)
            data.append({"latitude": i/10, "longitude": j/10, "value": "Dust"})

    for i in range (510, 520):
        for j in range (710, 720):
            print(i/10, ' ', j/10)
            i += 1
            if i > 520: break
            data2.append({"latitude": i/10, "longitude": j/10, "value": "CO2"})

    for i in range (440, 450):
        for j in range (770, 772):
            print(i/10, ' ', j/10)
            data2.append({"latitude": i/10, "longitude": j/10, "value": "CO2"})

    for i in range (510, 520):
        for j in range (760, 770):
            print(i/10, ' ', j/10)
            data.append({"latitude": i/10, "longitude": j/10, "value": "Dust"})

    for i in range (470, 475):
        l = int(i * 1.5)
        for j in range (l, 550):
            print(i/10, ' ', j/10)
            data.append({"latitude": i/10, "longitude": j/10, "value": "Dust"})


predict()
# Create a base map
m = folium.Map(location=[-40.3, -62.2], zoom_start=10)

# Loop over data and add it to the map
# for item in data:
#     folium.Marker(
#         location=[item["latitude"], item["longitude"]],
#         tooltip=item["value"]
#     ).add_to(m)


for item in data:
    folium.Marker(
        location=[item['latitude'], item['longitude']],
        icon=folium.DivIcon(html=f"""
                <div><svg>
                    <circle cx="50" cy="50" r="10" fill="yellow" opacity=".1    "/>
                </svg></div>"""),
        tooltip=item["value"]
    ).add_to(m)

for item in data2:
    folium.Marker(
        location=[item['latitude'], item['longitude']],
        icon=folium.DivIcon(html=f"""
                <div><svg>
                    <circle cx="50" cy="50" r="10" fill="grey" opacity=".1    "/>
                </svg></div>"""),
        tooltip=item["value"]
    ).add_to(m)







# Save map to HTML file
m.save("preload.html")
