var tmce_id;
var tmce_value;
var tmce_type;
var tmce_win;
var tmfb_win;



function FileBrowser(id, value, type, win) {
    // Do custom browser logic
//    var url = '/site_media/images/tnwa_logo.png';
//    var fieldElm = win.document.getElementById(id);
//    fieldElm.value = url;
      var cmsURL = '/admin/filebrowser/browse/?pop=2';
    cmsURL = cmsURL + '&type=' + type;

    tmce_id = id;
    tmce_value = value;
    tmce_type = type;
    tmce_win = win;

    tmfb_win = tinymce.activeEditor.windowManager.open({
        url: cmsURL,
        title:'Choose or Upload a File',
        resizable:true,
        scrollbars:true,
        maximizable:true,
        width: 940,
        height: 600
        },{
        window: win,
        input: value,
        editor_id: id });
}



tinymce.init({
    selector: "textarea",
    theme: "modern",
    plugins: [
        "advlist autolink lists link image charmap hr anchor",
        "searchreplace wordcount visualblocks visualchars code fullscreen",
        "insertdatetime media nonbreaking table contextmenu directionality"
    ],
    menubar: "edit insert view format table tools",
    toolbar1: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
    image_advtab: true,
    content_css:'/static/admin_css/editor.css?v=4',
    width: "98%",
    height: 500,
    file_browser_callback : FileBrowser,
    style_formats : [
        {title : 'Header 1', block : 'h1'},
        {title : 'Header 2', block : 'h2'},
        {title : 'Header 3', block : 'h3'},
        {title : 'Header 4', block : 'h4'},
        {title : 'Header 5', block : 'h5'},
        {title : 'Header 6', block : 'h6'},
        {title : 'Div', block: 'div'},
        {title : 'Paragraph', block: 'p'},
        {title : 'Bulleted List', selector: 'ul', classes: 'bulletedList', style: {'list-style-type': 'disc'}}
    ]
});


// Applying the specified format
tinymce.activeEditor.formatter.apply('custom_format');