var createBoxTab = function (idTab) {

    var tab = $(idTab);
    var editBtn = $('#action-edit');
    var deleteBtn = $('#action-delete');
    var boxTable = $('.box-table .box-typical-body');
    var currentRow = {
        row: null,
        dataset: null
    };

    var setBoxTableHeight = function () {
        var height = $(window).height() - boxTable.offset().top - 38;
        var minHeight = 250; //.box-typical-body (tables.less)
        var scrollHeight;
        if (height <= minHeight) {
            scrollHeight = minHeight + 5;
        } else {
            scrollHeight = height - 42;
        }

        boxTable.css('max-height', height + 'px');
        $('.dataTables_scrollBody').css({
            'height': scrollHeight,
            'max-height': scrollHeight
        });
    };

    var table = tab.DataTable({
        select: {
            style: 'single'
        },
        bScrollInfinite: true,
        bScrollCollapse: true,
        sScrollY: '10px',
        bLengthChange: false,
        bAutoWidth: false,
        searching: true,
        sDom: 'lrt',
        language: {
            zeroRecords: "Aucune formation n'a été trouvé.",
            infoEmpty: "Aucune formation.."
        }
    });

    $(window).resize(function () {
        setBoxTableHeight();
    }).resize();

    $('#datatable-custom-search').on('keyup', function () {
        table.search(this.value).draw();
    });

    table
    .on('select', function (e, dt, type, indexes) {
        editBtn.removeClass('disabled');
        deleteBtn.removeClass('disabled');
        currentRow.row = table.row(indexes[0]);
        currentRow.dataset = table.row(indexes[0]).node().dataset;
    })
    .on('deselect', function (e, dt, type, indexes) {
        editBtn.addClass('disabled');
        deleteBtn.addClass('disabled');
        currentRow.row = null;
        currentRow.dataset = null;
    });

    $(idTab + ' tbody a').on('click', function (e) {
        e.stopPropagation();
    });

    editBtn.click(function (event) {
        if (!$(this).hasClass('disabled')) {
            location.href = currentRow.dataset.edit;
        }
    });

    deleteBtn.click(function (event) {
        if (!$(this).hasClass('disabled')) {

            swal({
                    title: "Êtes-vous sûr ?",
                    text: "Voulez-vous supprimer cette formation ?",
                    type: "warning",
                    showCancelButton: true,
                    confirmButtonClass: "btn-danger",
                    confirmButtonText: "Oui",
                    cancelButtonText: "Non",
                    closeOnConfirm: false,
                    closeOnCancel: true
                },
                function (isConfirm) {
                    if (isConfirm) {
                        $.get(currentRow.dataset.delete, function () {
                            currentRow.row.remove().draw();
                            swal({
                                title: "Supprimée !",
                                text: "La formation a bien été supprimée.",
                                type: "success",
                                confirmButtonClass: "btn-success"
                            });
                        });
                    }
                });
        }
    });
};