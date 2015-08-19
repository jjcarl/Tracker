'use strict';

angular.module('trackerApp.userAuth', ['ngRoute'])

.config(['$routeProvider', function($routeProvider){
    $routeProvider.when('/login', {
        templateUrl: 'user-auth/login.html',
        controller: 'LoginController'
    })
    .when('/register', {
        templateUrl: 'user-auth/register.html',
        controller: 'CreateUserController'
    })
}])
.controller('LoginController', ['$scope', '$location', 'User', function($scope, $location, User) {
    $scope.credentials = {};

    $scope.login = function(){
        User.login($scope.credentials).then(function(){
            $scope.credentials = {};
            $location.path('/maps');
        }, function(data) {
            $scope.alerts.push({msg: data.data.non_field_errors[0]});
        });
    };
        $scope.alerts = [];
        $scope.closeAlert = function(index){
            $scope.alerts.splic(index, 1)
    };
}])
.controller('CreateUserController', ['$scope', '$location', 'User', function($scope, $location, User){
    $scope.user_info = {}

    $scope.register = function(){
        User.registration($scope.user_info).then(function(){
            $scope.user_info = {};
            $location.path('/maps');
        }, function(data){
            $scope.alerts.push({msg: data.data.non_field_errors[0]})
        });
    };
    $scope.alerts = [];
    $scope.closeAlert = function(index){
        $scope.alerts.splice(index, 1)
    };
}])