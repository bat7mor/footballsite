$(document).ready(function() {
    $('#results_table').dataTable( {
        "ajax": "/gameinfo.txt"
    } );
} );
