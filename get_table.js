$(document).ready(function() {
    $('#results_table').dataTable( {
    	type: "POST",
    	dataType: 'jsonp',
        "ajax": "http://localhost:8000/gameinfo.txt"
    } );
} );
