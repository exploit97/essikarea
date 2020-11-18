
  $("document").ready(function () { 
$("#type").click(function () {
  var typeId = $(this).val();
  var VENDRE ='AV', LOUER ='AL' 
  if (typeId == VENDRE){
    $("#sell_price").attr("hidden",false); 
    $("#price").attr("hidden",true); 
  
  
  }
  else {
    $("#sell_price").attr("hidden",true); 
    $("#price").attr("hidden",false);
  };
 
});


});

