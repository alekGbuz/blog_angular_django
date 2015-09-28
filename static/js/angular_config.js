'use strict';
var BlogApp = angular.module('BlogApp', ['ngResource','ngRoute','ui.bootstrap','BlogAppDirectives','angularFileUpload']);

BlogApp.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

BlogApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';    }
])

BlogApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

BlogApp.config(['$routeProvider','$locationProvider',
  function($routeProvider,$locationProvider) {


    $routeProvider.
    when ('/',{
        templateUrl:'index_first_page.html',
        controller:'FirstPageCtrl'
    }).
    when('/articles_by_category/:categorySlug', {
        templateUrl: 'category_articles.html',
        controller: 'BlogArticleCategoryCtrl'
      }).
    when('/detail_article/:articleSlug',{
        templateUrl:'detail_article.html',
        controller: 'BlogArticleCtrl'
    }).
    when('/articles_by_keys',{
         templateUrl: 'articles_by_keys.html',
         controller: 'BlogKeyArticleCtrl'
    }).
    when('/detail_page/:pageSlug',{
        templateUrl: 'site_page.html',
        controller: 'SitePageCtrl'
    }).
    when('/connect',{
        templateUrl:'connect.html',
        controller: 'ConnectCtrl'
    }).
    otherwise({
        redirectTo: '/'
      });

    $locationProvider.html5Mode(true);


  }]);


BlogApp.run(function ($rootScope, $location) {
    var history = [];
    var history_forward = [];
    $rootScope.$on('$routeChangeSuccess', function() {
        history.push($location.$$path);
    });

    $rootScope.previousUrl = function () {
       history_forward.push(history.slice(-2)[1]);
       var prevUrl = history.length>1 ? history.splice(-2)[0]:'/' ;
       jQuery(".list-unstyled li a").removeClass('active_category');
       $location.path(prevUrl);
    };

    $rootScope.forwardUrl = function(){
        var nextUrl = history_forward.pop();
        jQuery(".list-unstyled li a").removeClass('active_category');
        $location.path(nextUrl);
    }

});