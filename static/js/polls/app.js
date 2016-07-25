var pollApp = angular.module('pollApp', []);

pollApp.config(function($interpolateProvider, $httpProvider){
    $interpolateProvider.startSymbol('{$').endSymbol('$}');
    $httpProvider.defaults.headers.common['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
});