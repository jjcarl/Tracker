angular.module('trackerApp.mapDirective', [])
.directive('map', function() {
    return {
        restrict: 'E',
        scope: {
            points: '=points',
        },
        link: function(scope, element, attrs) {

            var orderedPoints = [];

            for (var i = 0; i < scope.points.length; i++) {

                orderedPoints[i] = {

                    lat: scope.points[i].lat,
                    lng: scope.points[i].lng

                }
            }

            var mapInfo = {
                zoom: 12,
                center: new google.maps.LatLng(40.233671, -111.658673),
                mapTypeId: google.maps.MapTypeId.SATELLITE
            };
            
            polyMap = new google.maps.Map(element[0], mapInfo);

            polygon = new google.maps.Polygon({
                paths: orderedPoints,
                strokeColor: '#FF0000',
                strokOpacity: 1.0,
                strokeWeight: 2,
                fillColor: '#FF0000',
                fillOpacity: 0.35,
            });
            
            polygon.setMap(polyMap);

        }
    }
})