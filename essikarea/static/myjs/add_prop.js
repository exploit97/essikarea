
    $("document").ready(function () { 
        $("#genre").click(function () {
          var genreId = $(this).val();
          var STUDIO ='ST'; 
          if (genreId == STUDIO){
           
           $("#sqft").attr("hidden",false);
          
           
          
          };
        });
    });