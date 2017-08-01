var postdetail = angular.module('postdetail', []);
postdetail.controller('postDetailCtrl', function ($scope, $http) {

    $scope.postdetails = function () {

        $http({
            url: "http://127.0.0.1:8000/posts/1/",
            dataType: 'json',
            method: 'GET',
            data: '',
            // Origin: 'Access-Control-Allow-Origin',
            headers: {
                "Content-Type": "application/json",
                // "Access-Control-Allow-Origin": "*",
            }
        }).success(function (response) {
            // debugger;
            console.log(response)
            $scope.postdetailobj = response;
        }).error(function (error) {
            alert(error);
        });
    }
});

postdetail.controller('userDetailCtrl', function ($scope, $http) {
    $scope.userdetail = function () {
        $http({
            url: $scope.user,
            dataType: 'json',
            method: 'GET',
            data: '',
            // Origin: 'Access-Control-Allow-Origin',
            headers: {
                "Content-Type": "application/json",
                // "Access-Control-Allow-Origin": "*",
            }
        }).success(function (response) {
            // debugger;
            console.log(response)
            $scope.userName = response;
        }).error(function (error) {
            alert(error);
        });
    }
})
.directive('userLink', function() {
    return {
        template: '<a href="{{userName.url}}"><span ng-bind="userName.username"></span></a>'
    };
});
