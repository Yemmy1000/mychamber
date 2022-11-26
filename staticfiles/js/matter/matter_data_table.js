var dataTable = $('#matterDatatable').DataTable({
    // "scrollX": true,
    // "processing" : true,
    // "serverSide" : true,
    // "searching" : true,
    // searchPanes: true,
    // lengthChange: false,
    // "pageLength" : 5,
    // "paging":true,
    // stateSave: true,
    // select:true,
    // "order" : [],
    order:[[2, 'asc'],],
    buttons: [
        'copy', 'excel', 'pdf', 'colvis' 
    ],
    ajax: {
            url: "/api/matters",
            type: 'GET',
            dataSrc: "",
        },

    // "columnDefs":[
    //     {				
    //     "orderable":false,
    //     },
    // ],
    // dom: 'Bfrtip',
    //  dom: '<"top"fl>rt<"bottom"ipB><"clear">',
    dom: '<"row"<"col-md-12"<"row"<"col-md-6"B><"col-md-6"f> > ><"col-md-12"rt> <"col-md-12"<"row"<"col-md-5"i><"col-md-7"p>>> >',

    "columns": [
        { 'data': 'file_no' },
        { 'data': 'claim_no'},
        { 'data': 'title' },
        { 'data': 'client_contact' },
        { 'data': 'created',
            render: function(st){
            return moment(st).format('LLL');
            } 
        },
        { 'data': 'updated',
            render: function(st){
            return moment(st).format('LLL');
            }
         },
        {   data: 'file_no',
            orderable: false,
            searchable: false,
            className: "center",
            render: function(file_no){
                return '<div class="btn-group">'+
                '<button class="btn btn-secondary btn-sm dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Actions'+
                  '</button>'+
                  '<ul class="dropdown-menu" id="'+file_no+'" aria-labelledby="dropdownMenuReference1" style="min-width: 7rem !important"; z-index: 10000px;>'+
                    '<li><a class="dropdown-item small clsViewMatter" id="clsViewMatter"  href="view-matter/'+file_no+'">View</a></li>'+
                    '<li><a class="dropdown-item small clsUpdateMatter" id="clsUpdateMatter" href="update-matter-info/'+file_no+'">Edit</a></li>'+
                    '<li><a class="dropdown-item small clsMatterUpdate" id="clsMatterUpdate" href="/matter-update/'+file_no+'">Update</a></li>'+
                    '<li><hr class="dropdown-divider"></li>'+
                    '<li>'+
                        '<a class="dropdown-item small " style="color:red;" data-id="'+file_no+'" data-bs-toggle="modal" data-bs-target="#RemoveMatter" href="#">Remove</a>'+
                    '</li>'+
                '</ul>'+
                '</div>';                    
            }, 
        }
    ],



});  
// dataTable.ajax.url('/api/events/').load();
// dataTable.searchPanes.container().prependTo(dataTable.table().container());
// dataTable.searchPanes.resizePanes();
dataTable.buttons().container()
.appendTo('#eventDatatable_wrapper .col-md-6:eq(0)');
// console.log('called');
// }

