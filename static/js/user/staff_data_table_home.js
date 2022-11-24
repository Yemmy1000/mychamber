

var dataTable = $('#staffDatatable').DataTable({
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
            url: "/api/users/",
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
        {
            data: 'email',
            // orderable: true,
            // searchable: true,
            // className: "center"
        },

        {
            data: 'last_login',
            // orderable: true,
            // searchable: true,
            // className: "center",
            render: function(ed){
                let dd = moment(ed).format('LLL');
                if (dd==='Invalid date'){
                    return '';
                }else{
                    return dd;
                }                            
            } 
        },
        {
            data: 'id'
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