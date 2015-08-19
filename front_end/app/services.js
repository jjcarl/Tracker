'use strict';


var trackerAppServices = angular.module('trackerAppServices', ['ngResource']);

trackerAppServices.factory("Map", ['$resource', function($resource) {
    return $resource('http://127.0.0.1:8000/areas/:mapId/', {}, {
    })
}]);