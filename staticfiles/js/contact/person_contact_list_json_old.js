$(document).ready(function() {

    function fill_person_contact_table(){
        var dt_table = $('.personContactDatatable').dataTable({
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
                        return '<img class="rounded-circle" src="/media/'+pix+'" style="width:50px;" alt="">';                    
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
                        '<button type="button" class="btn btn-dark btn-sm">Open</button>'+
                        '<button type="button" class="btn btn-dark btn-sm dropdown-toggle dropdown-toggle-split" id="dropdownMenuReference1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" data-reference="parent">'+
                        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-down"><polyline points="6 9 12 15 18 9"></polyline></svg>'+
                        '</button>'+
                        '<div class="dropdown-menu" id="'+id+'" aria-labelledby="dropdownMenuReference1">'+
                            '<a class="dropdown-item clsViewPersonContact" hx-post="{{ request.path }}?id={{ id }}" hx-target=".modal-body" href="#">View</a>'+                        
                            '<a class="dropdown-item clsUpdatePersonContact" data-toggle="modal" data-id="'+id+'" data-target="#updatePersonContact" href="#">Update</a>'+
                            '<div class="dropdown-divider"></div>'+
                            '<a class="dropdown-item clsDeletePersonContact" style="color:red;" data-id="'+id+'" data-toggle="modal" data-target="#removePersonContact" href="#">Remove</a>'+
                        '</div>'+'</div>';                    
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
    }

});

