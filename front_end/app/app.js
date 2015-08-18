'use strict';

// Declare app level module which depends on views, and components
angular.module('trackerApp', [
  'ngRoute',
  'ngResource',
  'trackerApp.mapView',
  'trackerApp.mapDetail',
  'trackerApp.mapDirective',
  'trackerAppServices'
]).
config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.when('/maps', {
            templateUrl: "maps/maps.html",
            controller: 'AllMapsCtrl'
            })
            .when("/maps/:mapId", {
                templateUrl: "map_detail/map-detail.html",
                controller: "MapDetailController"
            })
            .otherwise({redirectTo: '/maps'});
}]);
