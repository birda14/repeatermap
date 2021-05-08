import mapboxgl, { Map, NavigationControl, Popup } from 'mapbox-gl/dist/mapbox-gl.js';
import repeaters from './data/repeaters'

document.addEventListener('DOMContentLoaded', (event) => {

    mapboxgl.accessToken = 'pk.eyJ1IjoiYWFyb25ibWFjZG9uYWxkIiwiYSI6ImNrb2Y4M2cwaTAzNzEydnA3czNkcWNjZXoifQ.8sEtwzjSSsyChEtmIMAuBA';

    const map = new Map({
        container: 'map_container',
        style: 'mapbox://styles/mapbox/streets-v11',
        zoom: 3,
        center: [-96.466667,62.4]
    });

    map.addControl(new NavigationControl());
    
    map.on('load', () => {
        // if (navigator.geolocation) {
        //     navigator.geolocation.getCurrentPosition((event) => {
        //         map.jumpTo({
        //             center: [event.coords.longitude, event.coords.latitude]
        //         })
        //     });
        // }

        map.addSource('repeaters', {
            'type': 'geojson',
            'data': repeaters
        });

        map.addLayer({
            'id': 'repeaters',
            'type': 'circle',
            'source': 'repeaters',
            'paint': {
                'circle-radius': 5,
                'circle-color': '#ff0000'
            },
            'filter': [
                '==',
                '$type',
                'Point'
            ]
        });
    });

    map.on('click', 'repeaters', (event) => {
        var coordinates = event.features[0].geometry.coordinates.slice();
        var callsign    = event.features[0].properties.Callsign;
        var frequency   = event.features[0].properties.Frequency;

        while (Math.abs(event.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += event.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        new Popup()
            .setLngLat(coordinates)
            .setHTML('<h3>' + callsign + '</h3><p>' + frequency + '</p>')
            .addTo(map);
    });

    map.on('mouseenter', 'repeaters', function () {
        map.getCanvas().style.cursor = 'pointer';
    });

    map.on('mouseleave', 'repeaters', function () {
        map.getCanvas().style.cursor = '';
    });
});