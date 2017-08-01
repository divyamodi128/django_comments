
var post = angular.module('post', []).config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

// var post = angular.module('post', []);
post.controller('postCtrl', function ($scope, $http) {

    $scope.postcall = function () {

        $http({
            url: "http://127.0.0.1:8000/posts/",
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
            $scope.PostListObj = response;
        }).error(function (error) {
            alert(error);
        });
    }
})
.directive('myPostlist', function() {
    return {
        templateUrl: 'post_list.html'
    };
});


post.controller('postDetailCtrl', function ($scope, $http) {

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


post.controller('userCtrl', function ($scope, $http) {
    $scope.usercall = function () {
        $http({
            url: $scope.posts.user,
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

