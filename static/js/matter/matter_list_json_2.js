/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
var __webpack_exports__ = {};
/*!*******************************************!*\
  !*** ./resources/assets/js/bills/bill.js ***!
  \*******************************************/
    
    $('#matterDatatable').DataTable({
      "scrollX": true,
      "processing" : true,
      "serverSide" : true,
      "searching" : true,
      // "pageLength" : 5,
      "paging":true,
      stateSave: true,
      select:true,
      "order" : [],
      "ajax" : {
        url: "{% url 'matter_2_json' %}",
        method:"GET",
        // data:{action: 'fillTable'}          
      },
    
    "columnDefs":[
      {				
        "orderable":false,
      },
    ],
    dom: 'Bfrtip',
  //  dom: '<"top"fl>rt<"bottom"ipB><"clear">',
  buttons: [
    'copy', 'csv', 'excel', 'pdf', 'print'
  ],
  });  
  // console.log('called');
// }

// });







  
/******/ 

})();