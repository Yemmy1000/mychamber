/******/
(() => { // webpackBootstrap
    /******/
    "use strict";
    var __webpack_exports__ = {};
    /*!**************************************************!*\
      !*** ./resources/assets/js/patients/patients.js ***!
      \**************************************************/


    var tableName = '#matterDatatable';
    $('#matterDatatable').DataTable({
        processing: true,
        serverSide: true,
        'order': [
            [1, 'asc']
        ],
        ajax: {
            url: MATTER_LIST_JSON_URL,
            // data: function data(_data) {
            //     _data.status = $('#filter_status').find('option:selected').val();
            // }
        },
        columnDefs: [{
            'targets': [0, 5],
            'orderable': false,
            'className': 'text-center',
            'width': '5%'
        }, {
            'targets': [6],
            'orderable': false,
            'className': 'text-center',
            'width': '8%'
        }, {
            targets: '_all',
            defaultContent: 'N/A'
        }],
        columns: [
        {
            data: 'file_no',
            // name: 'file_no'
        }
    
    
    
    ],
        'fnInitComplete': function fnInitComplete() {
            $('#filter_status').change(function() {
                $(tableName).DataTable().ajax.reload(null, true);
            });
        }
    });
    $(document).on('click', '.delete-btn', function(event) {
        var patientId = $(event.currentTarget).data('id');
        deleteItem(patientUrl + '/' + patientId, '#patientsTable', 'Patient');
    });
    $(document).on('change', '.status', function(event) {
        var patientId = $(event.currentTarget).data('id');
        updateStatus(patientId);
    });

    window.updateStatus = function(id) {
        $.ajax({
            url: patientUrl + '/' + +id + '/active-deactive',
            method: 'post',
            cache: false,
            success: function success(result) {
                if (result.success) {
                    tbl.ajax.reload(null, false);
                }
            }
        });
    };
    /******/
})();