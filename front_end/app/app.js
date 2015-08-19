'use strict';

angular.module('trackerApp', [
  'ngRoute',
  'ngResource',
  'trackerApp.mapView',
  'trackerApp.mapDetail',
  'trackerApp.mapDirective',
  'trackerAppServices',
  'trackerApp.newMap',
  'trackerApp.userAuth'
])

.config(['$resourceProvider', function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
}])

.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.when('/maps', {
            templateUrl: "maps/maps.html",
            controller: 'AllMapsCtrl'
            })
            .when("/maps/:mapId", {
                templateUrl: "map_detail/map-detail.html",
                controller: "MapDetailController"
            })
            .when('/newMap', {
                templateUrl: "newmap/newmap.html",
                controller: "NewMapController"
            })
            .otherwise({redirectTo: '/maps'});
}])

.controller('TrackerController', ['$scope', '$location', '$http', 'User', function($scope, $location, $http, User){
    var token = sessionStorage.getItem(User.token_name);

    if(token){
        $http.defaults.headers.common.Authorization = ' Token ' + token;
        User.getInfo().then(function(){
            $location.path('/maps');
            $scope.user = User;
        });
    };

    $scope.logout = function(){
        User.logout();
        $scope.user = null;
        $location.path('/login');
    };

    $scope.$on('$routeChangeStart', function(event, next){
        if(next.$$route != undefined){
            var nextRoute = next.$$route.originalPath;
            if (User.info.id === undefined && (nextRoute != '/register' && nextRoute != '/login')){
                $location.path('/login');
            };
        };
    });

}])
