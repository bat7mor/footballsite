$(document).ready(function() {
    $('#results_table').dataTable( {
        "ajax": "./gameinfo.txt", 
        "bFilter": true,
        "columns": [ {"name": "Date", "orderable": true}, {"name": "Home Team", "orderable": true}, {"name": "Away Team", "orderable": true}, {"name": "Score", "orderable": false}, {"name": "Point Spread", "orderable": false}, {"name": "Our Predicted Score", "orderable": false} ] ,

        //function adapted from https://datatables.net/examples/api/multi_filter_select.html
        initComplete: function() {
        	var api = this.api();
        	api.columns().indexes().flatten().each( function ( i ) {
                var column = api.column( 1 );
                var select = $('#homeSelect')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        if (val == "Filter By Home Team") {
                        	val = "";
 						}; 

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
 				var column2 = api.column(2);
 				var select = $('#awaySelect')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        if (val == "Filter By Away Team") {
                        	val = "";
                        };

                        column2
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

            } );

        }
    } );

	// populate select boxes
	// adapted from http://developerdan77.wordpress.com/2011/10/14/dynamically-populate-a-select-element-from-json-data-with-jquery/
	$(function(){
	    //Use Jquery's getJSON, it automaticly parses the data into a usable json object
	 	$.getJSON( './teams.json', function( data ){
		  //Go through each object in the json data
		  $.each( data, function( key, val){
			  //The array index as a value of the option
			  $('#homeSelect').append('<option id="' + val + '">' + val + '</option>');
			  $('#awaySelect').append('<option id="' + val + '">' +  val + '</option>');

		   });
	 	});

	});


} );
