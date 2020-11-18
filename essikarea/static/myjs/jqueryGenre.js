
    $("document").ready(function () { 
  $("#genre").click(function () {
    var genreId = $(this).val();
    var MAISON ='MA', LOT= 'PA'; 
    if (genreId == MAISON){
     
     $("#bedrooms").attr("hidden",false);
     $("#rooms").attr("hidden",false);
     $("#kitchen").attr("hidden",false);
     $("#bathrooms").attr("hidden",false);
     $("#garage").attr("hidden",false);
     $("#lot_size").attr("hidden",true); 
     $("#veranda").attr("hidden",false); 
     
    
    }

   else if (genreId == LOT){
      $("#veranda").attr("hidden",true); 
      $("#lot_size").attr("hidden",false);
      $("#bedrooms").attr("hidden",true); 
      $("#rooms").attr("hidden",true); 
      $("#kitchen").attr("hidden",true); 
      $("#bathrooms").attr("hidden",true);
      $("#garage").attr("hidden",true);
      $("#sqft").attr("hidden",true);
     
      
     
     }
  

    else {
   
     $("#bedrooms").attr("hidden",true); 
     $("#rooms").attr("hidden",true); 
     $("#kitchen").attr("hidden",true); 
     $("#bathrooms").attr("hidden",true);
     $("#garage").attr("hidden",true);
   
     $("#lot_size").attr("hidden",true); 
     $("#veranda").attr("hidden",true); 
     
    };  
});
});

 

 
     