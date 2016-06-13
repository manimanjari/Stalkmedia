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
        $scope.tag = '/images/?q=' + $scope.image
        $http.get($scope.tag).success(function(data,status,headers,config){
        $scope.tag_data={}
        for(i=0;i<data.length;i++){
            $scope.tag_data[i]=data[i];
        }
      }).error(function(data,status,headers,config){
        })
    }

});
