var module = angular.module("stalkmediaApp", ['ngRoute']);
module.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

module.controller("TagController", function($scope, $http) {

    $scope.image = ""
    $scope.search = function(image) {
        console.log($scope.image)
        $scope.tag = '/images/?q=' + $scope.image
        $http.get($scope.tag).success(function(data,status,headers,config){
        $scope.tag_urls={}
        for(i=0;i<data.length;i++){
            $scope.tag_data=data[i];
            $scope.tag_urls[i]=$scope.tag_data.url
        }
      }).error(function(data,status,headers,config){
        })
    }

});
