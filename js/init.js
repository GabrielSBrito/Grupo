(function($){
  $(function(){

    $('.button-collapse').sideNav();
  

  }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function () {
    $('select').material_select();
});

var x = document.getElementById("myDatetime").value;
document.getElementById("demo").innerHTML = x;
    }