'use strict';

angular.module('trackerApp.newMap', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/newMap', {
        templateUrl: 'newmap/newmap.html',
        controller: 'NewMapController'
    });
}])

.controller('NewMapController', ['$scope', '$http', 'User', function($scope, $http, User) {
    $scope.area = []
    $scope.user = User;
    $scope.submit = function() {
        var name = $scope.name
        var description = $scope.description
        var user = $scope.user.info.id
        var lat = $scope.area[0].lat
        var lng = $scope.area[0].lng
        var points = $scope.area
        $http.post('http://127.0.0.1:8000/areas/', 
            {"name": name, 'description': description, 'user': user, 'lat': lat, 'lng': lng, 'points': points})
            .then(function(response){
                $scope.success = response.status
                $scope.posted = "Your map has been saved"
            }),
            function(response) {
                $scope.errors = response.status
            }
    }
}])

.directive('newmap', function() {
    return {
        restrict: 'E',
        scope: {
            area: '='
        },
        link: function(scope, element, attrs) {
            var polygon;
            var polyMap;

            var drawMap = function() {
                var mapInfo = {
                    zoom: 13,
                    center: new google.maps.LatLng(40.233671, -111.658673),
                    mapTypeId: google.maps.MapTypeId.SATELLITE
                };

                polyMap = new google.maps.Map(element[0], mapInfo);
                
                var areaOptions = {
                    strokeColor: '#FF0000',
                    strokOpacity: 1.0,
                    strokeWeight: 2,
                    fillColor: '#FF0000',
                    fillOpacity: 0.35,
                    editable: true
                };
                polygon = new google.maps.Polygon(areaOptions)
                polygon.setMap(polyMap);

                google.maps.event.addListener(polyMap, 'click', addArea);
            }

            var addArea = function(event) {


                var area = polygon.getPath();

                area.push(event.latLng);

                scope.area.push({lat: event.latLng.G, lng: event.latLng.K})

                var spot = new google.maps.Marker({
                    position: event.latLng,
                    title: '#' + area.getLength(),
                    polyMap: polyMap,
                });

                scope.$apply()
            }
            drawMap();
        }
    }
})