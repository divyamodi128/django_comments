var app1 = angular.module('app1', []);
app1.controller('Ctrl1', function ($scope, $http) {  
    
    $scope.firstCall = function () {  
  
        $http({  
            url: "http://127.0.0.1:8000/posts/1/get/",  
            dataType: 'json',  
            method: 'GET',  
            data: '',  
            // Origin: 'Access-Control-Allow-Origin',
            headers: {  
                "Content-Type": "application/json" ,
                // "Access-Control-Allow-Origin": "*",
            }  
        }).success(function (response) {  
            // debugger;
            $scope.CommentList = response;  
        }).error(function (error) {  
            alert(error);  
        });  
    }  
});