'use strict';

// Declare app level module which depends on views, and components
angular.module('trackerApp', [
  'ngRoute',
  'trackerApp.mapView',
  'trackerApp.view2',
  'trackerApp.mapDirective'
]).
config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/view2'});
}]);
