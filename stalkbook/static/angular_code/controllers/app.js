var module = angular.module("stalkmediaApp", ['ngRoute']);
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

module.controller("TagController", function($scope, $http) {

    $scope.image = ""
    console.log($scope.image)
    $scope.search = function(image) {

        console.log($scope.image)
        $http({
          method: 'GET',
          url: "http://127.0.0.1:8000/images/?q" + $scope.image
          
        }).then(function successCallback(response) {
              console.log(response)
          }, function errorCallback(response) {
                alert("error");
         });
         console.log(url)

      }

});
module.controller("RouteController1", function($scope) {
    $scope.test="flickr photos"
});
module.controller("RouteController2", function($scope) {
    $scope.test="insta photos"
});