function fill_table(uid){

/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
var __webpack_exports__ = {};
/*!*******************************************!*\
  !*** ./resources/assets/js/bills/bill.js ***!
  \*******************************************/


$('#userDatatable').dataTable({
    language: dt_language,  // global variable defined in html
    order: [[ 0, "desc" ]],
    // lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
    columns: [
        // {
        //     data: 'avatar',
        //     orderable: false,
        //     searchable: false,
        //     className: "center",
        //     render: function(pix){
        //         return '<img class="rounded-circle" src="/media/'+pix+'" style="width:30px;" alt="">';                    
        //     },               
            
        // },
        // {
        //     data: 'username',
        //     orderable: true,
        //     searchable: true,
        //     className: "center"
        // },
        {
            data: 'email',
            orderable: true,
            searchable: true,
            className: "center"
        },
        {
            data: 'user_type',
            orderable: true,
            searchable: true,
            className: "center"
        },
        {
            data: 'date_joined',
            orderable: true,
            searchable: true,
            className: "center"
        },
        {
            data: 'last_login',
            orderable: true,
            searchable: true,
            className: "center"
        },
        {
            data: 'id',
            orderable: false,
            searchable: false,
            className: "center",
            render: function(id){
                return '<div class="btn-group">'+
                '<button class="btn btn-secondary btn-sm dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Actions'+
                  '</button>'+
                  '<ul class="dropdown-menu" id="'+id+'" aria-labelledby="dropdownMenuReference1" style="min-width: 7rem !important">'+
                  '<a class="dropdown-item clsViewEvent" data-id="'+id+'" data-bs-toggle="modal" data-bs-target="#ViewUserModal" href="#">View</a>'+
                  '<li><a class="dropdown-item small clsUpdatePersonContact" id="clsUpdatePersonContact" href="update-person/'+id+'">Update</a></li>'+
                    '<li><hr class="dropdown-divider"></li>'+
                    '<li>'+
                        '<a class="dropdown-item small clsDeletePersonContact" style="color:red;" data-id="'+id+'" data-toggle="modal" data-target="#removePersonContact" href="#">Remove</a>'+
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
    ajax: USER_LIST_JSON_URL,
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

  }