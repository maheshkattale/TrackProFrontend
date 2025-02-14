$(document).ready(function() {
    var table = $('#dataTable').DataTable();
 
    var buttons = new $.fn.dataTable.Buttons(table, {
        buttons: [{
          extend : 'excel',
          text : '<span class="btn-shadow  btn btn-info exportButton" >Export <i class="fa fa-download"></i></span> '        
        }]
   }).container().appendTo($('#exportButton'));
});

// $(document).ready(function() {
//   var table = $('#mainExportButton').DataTable();

//   var buttons = new $.fn.dataTable.Buttons(table, {
//       buttons: [{
//         extend : 'excel',
//         text : '<span class="btn-shadow  btn btn-info exportButton" >Export <i class="fa fa-download"></i></span> '        
//       }]
//  }).container().appendTo($('#mainExportButton'));
// });