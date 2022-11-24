// $(document).ready(function() {
//     $('.datatable').DataTable( {
//     ajax: {
//         url: '{% url "person_contact_json" %}',
//         type: 'GET',
//         dataSrc: "",
//     },    
//         columns: [
//             {   data: "personPix" },
//             {   data: "firstName" },
//             {   data: "familyName" },
//             {   data: "homeAddress" },
//             {   data: "firstPhone" },
//             {   data: "Action" },
//         ],
// });
// } );


/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
var __webpack_exports__ = {};
/*!*******************************************!*\
  !*** ./resources/assets/js/bills/bill.js ***!
  \*******************************************/


// var tableName = '#tblBills';
// $(tableName).DataTable({
//   processing: true,
//   serverSide: true,
//   'order': [[2, 'desc']],
//   ajax: {
//     url: billUrl
//   },
//   columnDefs: [{
//     'targets': [0],
//     'className': 'text-center',
//     'width': '8%'
//   }, {
//     'targets': [4],
//     'orderable': false,
//     'className': 'text-center',
//     'width': '8%'
//   }, {
//     'targets': [3],
//     'className': 'text-right',
//     'width': '10%'
//   }, {
//     targets: '_all',
//     defaultContent: 'N/A'
//   }],
//   columns: [{
//     data: function data(row) {
//       var showLink = billUrl + '/' + row.id;
//       return '<a href="' + showLink + '">' + row.bill_id + '</a>';
//     },
//     name: 'bill_id'
//   }, {
//     data: function data(row) {
//       var showLink = patientUrl + '/' + row.patient.id;
//       return '<a href="' + showLink + '">' + row.patient.user.full_name + '</a>';
//     },
//     name: 'patient.user.first_name'
//   }, {
//     data: function data(row) {
//       return row;
//     },
//     render: function render(row) {
//       if (row.bill_date === null) {
//         return 'N/A';
//       }

//       return moment(row.bill_date).utc().format('Do MMM, Y h:mm A');
//     },
//     name: 'bill_date'
//   }, {
//     data: function data(row) {
//       return !isEmpty(row.amount) ? '<p class="cur-margin">' + getCurrentCurrencyClass() + ' ' + addCommas(row.amount) + '</p>' : 'N/A';
//     },
//     name: 'amount'
//   }, {
//     data: function data(row) {
//       var url = billUrl + '/' + row.id;
//       var data = [{
//         'id': row.id,
//         'url': url + '/edit',
//         'viewUrl': url
//       }];
//       return prepareTemplateRender('#billActionTemplate', data);
//     },
//     name: 'patient.user.last_name'
//   }]
// });

// var dt_table = 

$('.personContactDatatable').dataTable({
    language: dt_language,  // global variable defined in html
    order: [[ 0, "desc" ]],
    // lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
    columns: [
        {
            data: 'personPix',
            orderable: false,
            searchable: false,
            className: "center",
            render: function(pix){
                return '<img class="rounded-circle" src="/media/'+pix+'" style="width:30px;" alt="">';                    
            },               
            
        },{
            data: 'firstName',
            orderable: true,
            searchable: true,
            className: "center"
        },
        {
            data: 'familyName',
            orderable: true,
            searchable: true,
            className: "center"
        },
        {
            data: 'homeAddress',
            orderable: false,
            searchable: true,
            className: "center"
        },
        {
            data: 'firstPhone',
            orderable: false,
            searchable: true,
            className: "center"
        },
        {
            data: 'sex',
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
                    '<li><a class="dropdown-item small clsViewPersonContact" id="clsViewPersonContact"  href="view-person/'+id+'">View</a></li>'+
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
    ajax: PERSON_CONTACT_LIST_JSON_URL,
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