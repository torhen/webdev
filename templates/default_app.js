"use strict"
var mymap = L.map('mapid').setView([47.37174, 8.54226], 10)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mymap)