var module = angular.module("stalkmediaApp", ['ngRoute']);
module.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

module.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            otherwise({
                redirectTo: '/'
            });
    }]);

module.controller("TagController", function($scope, $http) {

    $scope.image = ""
    $scope.search = function(image) {
        if ($scope.image != ""){
           $scope.tag = '/images/?q=' + $scope.image
           $http.get($scope.tag).success(function(data, status, headers, config){
           $scope.tag_data = {}
           if (data.length == 0){
              $scope.measure = 0;
              $scope.message = "Entered tag has no images associated with it";
           }
           else{
             for(i = 0; i < data.length; i++){
               $scope.measure = 1;
               $scope.tag_data[i] = data[i];
              }
           }
           })      
        }
        else{
          $scope.measure = 0;
            $scope.message = "You entered an empty tag"
        }
    }
 });
