
   
      $("#ville").change(function () {
        var url = $("#searchForm").attr("data-arrondissements-url");  // get the url of the `load_cities` view
        var villeId = $(this).val();  // get the selected country ID from the HTML input

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
            data: {
                'ville': villeId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#arrondissement").html(data);  // replace the contents of the city input with the data that came from the server
              
            }
        });

    });
  
