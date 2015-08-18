'use strict';

angular.module('trackerApp.mapView', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/maps', {
    templateUrl: 'maps/maps.html',
    controller: 'AllMapsCtrl'
  });
}])

.controller('AllMapsCtrl', ['$scope', '$http',
    function($scope, $http) {
        $http.get('http://127.0.0.1:8000/areas/').then(function(response){
            $scope.maps = response.data.results
        });
}]);
