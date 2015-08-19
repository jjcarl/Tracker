//angular.module('trackerApp.newMapDirective', [])
// .directive('newmap', function() {
//     return {
//         require: '^NewMapController',
//         restrict: 'E',
//         transclude: true,
//         link: function(scope, element, attrs) {
//             var polygon;
//             var polyMap;

//             var drawMap = function() {
//                 var mapInfo = {
//                     zoom: 13,
//                     center: new google.maps.LatLng(40.233671, -111.658673),
//                     mapTypeId: google.maps.MapTypeId.SATELLITE
//                 };

//                 polyMap = new google.maps.Map(element[0], mapInfo);
                
//                 var areaOptions = {
//                     strokeColor: '#FF0000',
//                     strokOpacity: 1.0,
//                     strokeWeight: 2,
//                     fillColor: '#FF0000',
//                     fillOpacity: 0.35,
//                     editable: true
//                 };
//                 polygon = new google.maps.Polygon(areaOptions)
//                 polygon.setMap(polyMap);

//                 google.maps.event.addListener(polyMap, 'click', addArea);
//             }

//             var addArea = function(event) {
//                 scope.area = polygon.getPath();

//                 scope.area.push(event.latLng);

//                 var spot = new google.maps.Marker({
//                     spot: event.latLng,
//                     title: '#' + scope.area.getLength(),
//                     polyMap: polyMap,
//                 });
//             }
//             google.maps.event.addDomListener(window, 'load', drawMap);
//         }
//     }
// })