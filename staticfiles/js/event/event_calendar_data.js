 
  var today = new Date();
  year = today.getFullYear();
  month = today.getMonth();
  day = today.getDate();
  
  /******/ 
  // (() => { 
    
    // webpackBootstrap

// /******
//  	"use strict";
// var __webpack_exports__ = {};
/*!*******************************************!*\
  !*** ./resources/assets/js/bills/bill.js ***!
  \*******************************************/




  var author = $('#author').val();
//   console.log(author);
  var myCalendar = $('#myEvent').fullCalendar({
    height: 'auto',
    defaultView: 'month',
    editable: true,
    selectable: true,
    header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay,listMonth'
    },


    events: "/api/events/",
    

    });



  




// $(document).on('click', '.delete-btn', function (event) {
//   var id = $(event.currentTarget).data('id');
//   deleteItem(billUrl + '/' + id, tableName, 'Bill');
// });
/******/ 
// })();