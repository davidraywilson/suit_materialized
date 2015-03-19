/// this file replaces the default one in filebrowser/static/filebrowser/js
/// These changes work with the latest tinymce

var FileBrowserDialogue = {
    fileSubmit: function (FileURL) {

        var win = parent.tmce_win;
        var editor_id = parent.tmce_id;
        var fieldElm = win.document.getElementById(editor_id);
        // insert information now
        fieldElm.value = FileURL;

        // change width/height & show preview
        if (win.ImageDialog) {
            if (win.ImageDialog.getImageData)
                win.ImageDialog.getImageData();
            if (win.ImageDialog.showPreviewImage)
                win.ImageDialog.showPreviewImage(FileURL);
        }

        parent.tmfb_win.close();

    }
};
