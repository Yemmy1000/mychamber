
// var dataTable = $('#personContactDatatable').DataTable({
    var dataTable = $('#'+tabelName).DataTable({
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
            url: "/api/person-contact-list/",
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

    columns: [
        {
            data: 'personPix',
            orderable: false,
            searchable: false,
            className: "center",
            render: function(personPix){
                return '<img class="rounded-circle" src="'+personPix+'" style="width:30px;" alt="">';                    
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
                    '<li><a class="dropdown-item small clsUpdatePersonContact" id="clsUpdatePersonContact" href="update-person/'+id+'">Edit</a></li>'+
                    '<li><hr class="dropdown-divider"></li>'+
                    '<li>'+
                        '<a class="dropdown-item small clsDeletePersonContact" style="color:red;" data-id="'+id+'" data-toggle="modal" data-target="#removePersonContact" href="#">Remove</a>'+
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
.appendTo( '#eventDatatable_wrapper .col-md-6:eq(0)' );
// console.log('called');
// }

// let ggg = 'Goooooooooo';