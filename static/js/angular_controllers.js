'use strict';

BlogApp.controller('IndexPageCtrl',['$scope','$http','$upload','$route','$location', function($scope,$http,$upload,$route,$location){
    $scope.findKey = '';
    $scope.page_title = '';

    jQuery(".list-unstyled").on('click', 'a', function(){
        jQuery(".list-unstyled li a").removeClass('active_category');
        jQuery(this).addClass('active_category');
    });


    $scope.findArticles = function(){
       jQuery(".list-unstyled li a").removeClass('active_category');
       $scope.keys = $scope.findKey.replace(/[&\/\\#,+()$~%.'":*?<>{}]/g, '') ;
       if ($scope.keys ==''){
           alert('Пустая строка для поиска');
       }
       else if ($scope.keys.length > 30) {
            alert ('Сделайте запрос короче');
        }
      else if ($scope.keys.length<3){
            alert('Совсем короткий запрос');
      }
       else {
          if ($location.$$path=='/articles_by_keys')
             $route.reload();
          else
            $location.url('/articles_by_keys');
       }
    }

}]);

BlogApp.controller('ConnectCtrl',['$scope','$http','$upload',function($scope,$http,$upload){
    $scope.$parent.page_title ='Связаться';
    $scope.message={'title':'','content':'','email':''}
    $scope.sendButton = function (){
        return $scope.message.title=='' || $scope.message.content=='' || !validateEmail($scope.message.email);
    }

    var validateEmail = function(email){
        var re = /\S+@\S+\.\S+/;
        return re.test(email);

    }

    $scope.send = function (){

//        var files = document.getElementById('upload-file').files;
//        if (files.length >0){
//            var file = files[0];
//        }
//        $scope.upload = $upload.upload({
//                url:'/my_api/send_message/',
//                method: 'POST',
//                data: $scope.message,
//                file: file
//            }).success(function (data, status, headers, config) {
//                file = null;
//                $scope.message={'title':'','content':''}
//           });
//

         $http.post('/my_api/send_message/',$scope.message).success(
            function(data){
             $scope.message={'title':'','content':''};
             alert('Сообщение отправлено');
            }
         )
    }

}]);

BlogApp.controller('FirstPageCtrl',['$scope','$http',function($scope,$http){
     $scope.$parent.page_title= 'Главная';
     $http.get('my_api/index_first_page/').success(
            function(data){
                $scope.firstPage = data;
       });

}]);

BlogApp.controller('BlogKeyArticleCtrl',['$scope','$http', function($scope,$http){
    $scope.$parent.page_title = 'Посты по запросу';

    $http.get('/my_api/articles_by_keys?keys='+$scope.$parent.keys).success(
            function(data){
                $scope.find_articles = data;
                $scope.find_filtered_articles = $scope.find_articles.slice(0,5);
                $scope.totalItems = data.length;
    });
    $scope.currentPage = 1;
    $scope.pageChanged = function() {
          $scope.find_filtered_articles = $scope.find_articles.slice(($scope.currentPage-1)*5,$scope.currentPage*5)
     };
}]);


BlogApp.controller('BlogArticleCategoryCtrl',['$scope','$resource','$routeParams', function($scope,$resource,$routeParams){
    $scope.$parent.page_title = 'Посты по категориям';


    $scope.category_slug = $routeParams.categorySlug;
    var Articles = $resource('/my_api/articles_by_category/'+$scope.category_slug+'/');
    $scope.articles = Articles.query(
        function(data){
        $scope.filter_articles = $scope.articles.slice(0,5);
        $scope.totalItems = data.length;
        }
    );
    $scope.currentPage = 1;
    $scope.pageChanged = function() {
          $scope.filter_articles = $scope.articles.slice(($scope.currentPage-1)*5,$scope.currentPage*5)
     };

}]);


BlogApp.controller('BlogArticleCtrl',['$scope','$http','$routeParams', function($scope, $http, $routeParams){
    $scope.article_slug = $routeParams.articleSlug;
    $http.get('/my_api/detail_article/'+$scope.article_slug+'/').success(
        function(data){
            $scope.article = data.article;
            $scope.$parent.page_title = data.article.title;
            $scope.prev_article = data.prev_article;
            $scope.next_article = data.next_article;
        }
    )
}]);


BlogApp.controller('SitePageCtrl',['$scope','$http','$routeParams', function($scope, $http, $routeParams){
    $scope.page_slug = $routeParams.pageSlug;
    $http.get('/my_api/site_page/'+$scope.page_slug+'/').success(
        function(data){
            $scope.page = data;
            $scope.$parent.page_title = data.name;
        }
    )
}]);
