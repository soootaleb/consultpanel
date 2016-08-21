var signatureEdition = function (idTab) {
    var uploadCropElement = document.getElementById(idTab);
    var image_url = uploadCropElement.getAttribute('image-url');
    var uploadButton = $("#signature_file_input_button");
    var fileInput = $("#signature_file_input");
    var formSiganture = $("#form_save_siganture");
    var fileInputSave = $("#input_image_base64");
    var saveButton = $("#signature_save_button");
    var uploadCrop;


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
    /*
    if(typeof image_url  !== typeof undefined && image_url !== false){
        uploadCrop.bind({
            url: image_url
        });
    }*/

    uploadButton.click( function (e) {
        fileInput.click();
    });

    fileInput.change( function (ev) {
        formSiganture.show();
        readFile(this);
    });

    saveButton.click( function (ev) {
        uploadCrop.result({
            type: 'canvas',
            size: 'viewport'
        }).then(function (base64) {
            console.log("base64 : "+base64);
            fileInputSave.val(base64);
            formSiganture.submit();
        });

    });
};

var cropSignatureImage = function (idTab) {
    console.log("CRooping function");
    var uploadCropElement = document.getElementById(idTab);
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