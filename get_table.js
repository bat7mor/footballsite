$(document).ready(function() {
    $('#results_table').dataTable( {
        "ajax": "https://raw.githubusercontent.com/bat7mor/footballsite/gh-pages/gameinfo.txt"
    } );
} );
