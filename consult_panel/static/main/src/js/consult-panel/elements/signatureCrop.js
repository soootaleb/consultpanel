var signatureEdition = function (idTab) {
    var uploadCropElement = $(idTab);
    var uploadButton = $("#signature_file_input_button");
    var fileInput = $("#signature_file_input");
    var saveButton = $("#save_button");
    var uploadCrop;

    console.log(uploadButton);
    function popupResult(result) {
        var html;
        if (result.html) {
            html = result.html;
        }
        if (result.src) {
            html = '<img src="' + result.src + '" />';
        }
        swal({
            title: '',
            html: true,
            text: html,
            allowOutsideClick: true
        });
        setTimeout(function () {
            $('.sweet-alert').css('margin', function () {
                var top = -1 * ($(this).height() / 2),
                    left = -1 * ($(this).width() / 2);

                return top + 'px 0 0 ' + left + 'px';
            });
        }, 1);
    }

    function readFile(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                uploadCrop.bind({
                    url: e.target.result
                });
            };

            reader.readAsDataURL(input.files[0]);
        }
        else {
            swal("Erreur - Votre navigateur est trop vieux...");
        }
    }

    uploadCrop = new Croppie(uploadCropElement, {
        viewport: {width: 300, height: 180},
        boundary: {width: 600, height: 380},
        showZoomer: true,
        enableOrientation: true
    });

    uploadButton.click( function (e) {
        fileInput.click();
    });

    fileInput.on("change", function () {
        saveButton.toggle();
        readFile(this);
    });

    saveButton.click( function (ev) {
        uploadCrop.result({
            type: 'canvas',
            size: 'viewport'
        }).then(function (resp) {
            popupResult({
                src: resp
            });
        });

    });
}

var cropSignatureImage = function (idTab) {
    console.log("CRooping function");
    var el = document.getElementById(idTab);
    var vanilla = new Croppie(el, {
        viewport: {width: 300, height: 180},
        boundary: {width: 600, height: 380},
        showZoomer: true,
        enableOrientation: true
    });
    console.log("CRooping function 1");
    vanilla.bind({
        url: '/static/main/img/video-preview.jpg',
        orientation: 1
    });
//on button click
    vanilla.result('canvas').then(function (base64Image) {
        // do something with cropped base64 image here
    });
};