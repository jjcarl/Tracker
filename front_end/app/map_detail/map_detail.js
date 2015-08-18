'use strict';

angular.module('trackerApp.mapDetail', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/maps/:mapId', {
    templateUrl: 'map_detail/map-detail.html',
    controller: 'MapDetailController'
  });
}])

.controller('MapDetailController', ["$scope", "$routeParams", "Map", function($scope, $routeParams, Map) {
    Map.get({mapId: $routeParams.mapId}, function(response){
        $scope.map = response
        });
}]);