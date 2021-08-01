window.dashExtensions = Object.assign({}, window.dashExtensions, {
            default: {
                function0: function(feature, latlng, context) {
                    return L.control.mousePosition().addTo(map);;
                },
                function1: function(el, x) {
                        this.on('mousemove', function(e) {
                            var lat = e.latlng.lat;
                            var lng = e.latlng.lng;
                            var coord = [lat, lng];
                        });
                        return coord;
                    }

                    ,
                function2: function(feature, latlng, context) {
                    return L.control.mousePosition().addTo(map);;
                },
                function3: function(el, x) {
                        this.on('mousemove', function(e) {
                            var lat = e.latlng.lat;
                            var lng = e.latlng.lng;
                            var coord = [lat, lng];
                        });
                        return coord;
                    }

                    ,
                function4: function(feature, latlng, context) {
                    return L.control.mousePosition().addTo(map);;
                },
                function5: function(feature, latlng, context) {
                    return L.control.mousePosition();
                },
                function6: function(el, x) {
                    this.on('mousemove', function(e) {
                        var lat = e.latlng.lat;
                        var lng = e.latlng.lng;
                        var coord = [lat, lng];
                    });

                    , function7:
                        map.on('mousemove', function(e) {
                            document.getElementById('info').innerHTML = / * innerHTML property sets or returns the HTML between the start and end tags of the table row * /
                            // e.point is the x, y coordinates of the mousemove event relative
                            // to the top-left corner of the map
                            JSON.stringify(e.containerPoint) + '<br />' +
                                // e.lngLat is the longitude, latitude geographical position of the event
                                JSON.stringify(e.latlng);
                            / * JSON.stringify () method may be an arbitrary sequence of values ​​into JSON JavaScript string * /
                        });




                    , function8:
                        var lat, lng;

                    map.addEventListener('mousemove', function(ev) {
                        lat = ev.latlng.lat;
                        lng = ev.latlng.lng;
                    });

                    document.getElementById("transitmap").addEventListener("contextmenu", function(event) {
                        // Prevent the browser's context menu from appearing
                        event.preventDefault();

                        // Add marker
                        // L.marker([lat, lng], ....).addTo(map);
                        alert(lat + ' - ' + lng);

                        return false; // To disable default popup.
                    });




                    , function9:
                        var lat, lng;

                    map.addEventListener('mousemove', function(ev) {
                        lat = ev.latlng.lat;
                        lng = ev.latlng.lng;
                    });

                    document.getElementById("transitmap").addEventListener("contextmenu", function(event) {
                        // Prevent the browser's context menu from appearing
                        event.preventDefault();

                        // Add marker
                        // L.marker([lat, lng], ....).addTo(map);
                        alert(lat + ' - ' + lng);

                        return false; // To disable default popup.
                    });




                    , function10: function(feature, latlng, context) {
                            return L.circleMarker(latlng);
                        }, function11: function(feature, latlng, context) {
                            return L.marker([41.77, -88.15]);
                        }, function12: function(feature, latlng, context) {
                            return L.marker([41.77, -88.15]);
                        }, function13:

                        map.on('dblclick', function(e) {
                            var marker = L.marker(e.latlng).addTo(map);
                            var markerpopup = L.popup({});
                            //Set popup lat lng where clicked
                            markerpopup.setLatLng(e.latlng);
                            //console.log(e.layer._latlng);
                            //Set popup content
                            markerpopup.setContent("Popup");
                            //Bind marker popup
                            marker.bindPopup(markerpopup);
                            //Add marker to geojson layer
                            drawnItems.addLayer(marker);
                        });


                    , function14:

                        map.on('mouseover', function(e) {
                            var marker = e.latlng;
                            console.log(e.latlng);
                        });


                    , function15:

                        map.on('mouseover', function(e) {
                            var marker = e.latlng;
                            console.log(marker);
                        });


                }
            });