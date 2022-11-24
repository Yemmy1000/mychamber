/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
var __webpack_exports__ = {};
/*!*******************************************!*\
  !*** ./resources/assets/js/bills/bill.js ***!
  \*******************************************/

$('#matterDatatable').dataTable({
    language: dt_language,  // global variable defined in html
    order: [[ 0, "desc" ]],
    // lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
    columns: [
        {
            data: 'file_no',
            orderable: true,
            searchable: true,
            className: "center",           
            
        },
        {
            data: 'client_contact',
            orderable: true,
            searchable: false,
            className: "center",
            render: function(client_contact){
                var wordsArray = client_contact.split(" ");
                var word_id = wordsArray[0];
                var word_name = wordsArray[1]+" "+wordsArray[2]+" "+wordsArray[3];
            return '<a href="../../contact/view-person/'+word_id+'">'+ word_name +'</a>';
            }
        }, 
        {
            data: 'created',
            orderable: true,
            searchable: true,
            className: "center",
            render: function(mydate){
                var ddate = new Date(mydate);               
                return  ddate. toLocaleDateString();
                // return  mydate;
            }
        },
        {
            data: 'updated',
            orderable: true,
            searchable: true,
            className: "center",
            render: function(mydate){
                var ddate = new Date(mydate);               
                return  ddate. toLocaleDateString();
                // return  mydate;
            }
        },
        {
            data: 'file_no',
            orderable: false,
            searchable: false,
            className: "center",
            render: function(file_no){
                return '<div class="btn-group">'+
                '<button class="btn btn-secondary btn-sm dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Actions'+
                  '</button>'+
                  '<ul class="dropdown-menu" id="'+file_no+'" aria-labelledby="dropdownMenuReference1" style="min-width: 7rem !important">'+
                    '<li><a class="dropdown-item small clsViewMatter" id="clsViewMatter"  href="view-matter/'+file_no+'">View</a></li>'+
                    '<li><a class="dropdown-item small clsUpdateMatter" id="clsUpdateMatter" href="update-matter-client/'+file_no+'">Update</a></li>'+
                    '<li><hr class="dropdown-divider"></li>'+
                    '<li>'+
                        '<a class="dropdown-item small " style="color:red;" data-id="'+file_no+'" data-bs-toggle="modal" data-bs-target="#removePersonContact" href="#">Remove</a>'+
                    '</li>'+
                '</ul>'+
                '</div>';                    
            }, 
        }
    
    ],
    searching: true,
    processing: true,
    serverSide: true,
    stateSave: true,
    ajax: MATTER_LIST_JSON_URL,
    dom: '<"row"<"col-md-12"<"row"<"col-md-6"B><"col-md-6"f> > ><"col-md-12"rt> <"col-md-12"<"row"<"col-md-5"i><"col-md-7"p>>> >',
    buttons: {
        buttons: [
            { extend: 'copy', className: 'btn' },
            { extend: 'csv', className: 'btn' },
            { extend: 'excel', className: 'btn' },
            { extend: 'print', className: 'btn' }
        ]
    },
});
// $(document).on('click', '.delete-btn', function (event) {
//   var id = $(event.currentTarget).data('id');
//   deleteItem(billUrl + '/' + id, tableName, 'Bill');
// });
/******/ })()
;