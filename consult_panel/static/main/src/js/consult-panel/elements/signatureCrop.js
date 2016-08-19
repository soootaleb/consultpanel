var cropSignatureImage = function (idTab) {
    console.log("CRooping function");
    var el = document.getElementById(idTab);
    var vanilla = new Croppie(el, {
        viewport: {width: 300, height: 180},
        boundary: {width: 500, height: 500},
        showZoomer: false,
        enableOrientation: true
    });
    console.log("CRooping function 1");
    vanilla.bind({
        url: 'http://placehold.it/500x500',
        orientation: 4
    });
//on button click
    vanilla.result('canvas').then(function (base64Image) {
        // do something with cropped base64 image here
    });
};