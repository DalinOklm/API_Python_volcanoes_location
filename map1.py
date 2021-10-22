import folium
from folium.vector_layers import CircleMarker
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])#NAME NAME,LOCATION,STATUS,ELEV,TYPE,TIMEFRAME
long = list(data['LON'])
name = list(data['NAME'])
location_v_1 = list(data['LOCATION'])
status_v_1 = list(data['STATUS'])
elev_v_1 = list(data['ELEV'])
type_v_1 = list(data['TYPE'])
time_frame_1 = list(data['TIMEFRAME'])



map = folium.Map(location=[38.58,-113.09], zoom_start=3, titles="Mapbox Bright")
#map = folium.Map(location=[22.9375,30.5595], zoom_start=5, titles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

#30.5595° S, 22.9375°

for lt, ln, name_volcano,location_v,status_v,elev_v,type_v,time_frame in zip(lat,long, name,
location_v_1,status_v_1,elev_v_1,type_v_1,time_frame_1):
    if int(elev_v) >= 2000 and int(elev_v) < 4000:
        color_v = "orange"
    elif int(elev_v) > 4000:
        color_v = "red"
    else: color_v = "green"
    info_v = 'name:'+str(name_volcano)+'<br>'+'<br>'+"location: "+str(location_v)+"status: "+str(status_v)+'<br>'+'<br>'+'elev: '+str(elev_v)+'<br>'+'<br>'+"type: "+str(type_v)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6,popup=info_v , fill_color = color_v, color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")