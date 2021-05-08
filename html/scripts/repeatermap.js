import { Map } from 'mapbox-gl/dist/mapbox-gl.js';
import repeaters from './data/repeaters.json'
 
mapboxgl.accessToken = 'pk.eyJ1IjoiYWFyb25ibWFjZG9uYWxkIiwiYSI6ImNrb2Y4M2cwaTAzNzEydnA3czNkcWNjZXoifQ.8sEtwzjSSsyChEtmIMAuBA';

var map = new Map({
    container: 'map_container',
    style: 'mapbox://styles/mapbox/streets-v11',
    // center: [43.5481351, -80.2457828],
    // zoom: 15
});

map.on('load', function () {
    map.addSource('repeaters', {
        'type': 'geojson',
        'data': repeaters
    });
});