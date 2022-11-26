

var dataTable = $('#eventDatatable').DataTable({
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
            url: "/api/events/",
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
        { 'data': 'title' },
        { 'data': 'matter'},
        { 
            data: 'description',
            // orderable: true,
            // searchable: true,
            // className: "center",
            render: function(descr){
                if (descr.length > 20) {
                    let subStr = descr.substring(0, 20);
                    return subStr + "...";
                } else {
                    return descr;
                }
            } 
        },
        { 'data': 'start',
            render: function(st){
                return moment(st).format('MMMM dddd, YYYY');
            }
        },
        { 'data': 'priority' },
        { 'data': 'category' },
        { 'data': 'status' },
        {
            data: 'id',
            orderable: false,
            searchable: false,
            className: "center",
            render: function(id){
                return '<div class="btn-group">'+
                // '<button type="button" class="btn btn-dark btn-sm">Open</button>'+
                '<button type="button" class="btn btn-secondary btn-sm dropdown-bs-toggle dropdown-toggle-split" id="dropdownMenuReference1" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" data-reference="parent">'+
                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-down"><polyline points="6 9 12 15 18 9"></polyline></svg>'+
                '</button>'+
                '<div class="dropdown-menu" id="'+id+'" aria-labelledby="dropdownMenuReference1">'+
                '<a class="dropdown-item clsViewEvent" data-id="'+id+'" data-bs-toggle="modal" data-bs-target="#ViewEventModal" href="#">View</a>'+
                '<a class="dropdown-item clsUpdateEvent" data-id="'+id+'" data-bs-toggle="modal" data-bs-target="#UpdateEventModal" href="#">Update</a>'+
                    '<div class="dropdown-divider"></div>'+
                    '<a class="dropdown-item clsDeletePersonContact" style="color:red;" data-id="'+id+'" data-bs-toggle="modal" data-bs-target="#DeleteEventModal" href="#">Delete</a>'+
                '</div>'+'</div>';                    
            }, 
        }
    ],
 


});  
// dataTable.ajax.url('/api/events/').load();
// dataTable.searchPanes.container().prependTo(dataTable.table().container());
// dataTable.searchPanes.resizePanes();
dataTable.buttons().container()
.appendTo( '#eventDatatable_wrapper .col-md-6:eq(0)' );
// console.log('called');
// }

// let ggg = 'Goooooooooo';