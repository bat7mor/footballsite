$(document).ready(function() {
    $('#results_table').dataTable( {
        "ajax": "./gameinfo.txt", 
        "columns": [ {"name": "Date", "orderable": true}, {"name": "Home Team", "orderable": true}, {"name": "Away Team", "orderable": true}, {"name": "Score", "orderable": false} ] 
    } );
} );
