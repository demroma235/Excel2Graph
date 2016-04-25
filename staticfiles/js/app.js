/**
 * Created by Roman on 25.04.2016.
 */
(function(){
    'use strict';
    angular
        .module('Excel2Graph', [])
        .controller('AppController', ['$scope', function($scope){

            $scope.myData = {};
            $scope.myData.doClick = function(item, event) {

                var responsePromise = $http.get("/result");

                responsePromise.success(function (data, status, headers, config) {
                    $scope.myData.fromServer = data.title;
                });
                responsePromise.error(function (data, status, headers, config) {
                    alert("AJAX failed!");
                });
            }
        }])
});