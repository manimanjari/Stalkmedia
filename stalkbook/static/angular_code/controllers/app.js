var module = angular.module("sampleApp", ['ngRoute']);
module.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})
module.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/flickr', {
                templateUrl: static_url + 'angular_code/partial_views/flickr_view.html',
                controller: 'RouteController1'
            }).
            when('/instagram', {
                templateUrl: static_url + 'angular_code/partial_views/insta_view.html',
                controller: 'RouteController2'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);

module.controller("RouteController1", function($scope) {
    $scope.test="flickr photos"
});
module.controller("RouteController2", function($scope) {
    $scope.test="insta photos"
});