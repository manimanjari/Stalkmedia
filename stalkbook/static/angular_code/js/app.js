var module = angular.module("sampleApp", ['ngRoute']);
module.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})
module.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/home', {
                templateUrl: static_url + 'angular_code/html/test1.html',
                controller: 'RouteController1'
            }).
            when('/secret', {
                templateUrl: static_url + 'angular_code/html/test2.html',
                controller: 'RouteController2'
            }).
            when('/login', {
                templateUrl: static_url + 'angular_code/html/test1.html',
                controller: 'RouteController1'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);

module.controller("RouteController1", function($scope) {
    $scope.test="This is working test1"
});
module.controller("RouteController2", function($scope) {
    $scope.test="This is working test2"
})
