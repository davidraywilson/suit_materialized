$(function () {
    var type = $('#id_link_type');
    var t_value = $(type).val();

    var page_link = $('.control-group.field-page');
    var cat_link = $('.control-group.field-category');
    var custom_link = $('.control-group.field-link');

    $(document).ready(function () {

        if (t_value == 'page') {
            $(page_link).show();
            $(cat_link).hide();
            $(custom_link).hide();
        }

        else if (t_value == 'category') {
            $(page_link).hide();
            $(cat_link).show();
            $(custom_link).hide();
        }

        else if (t_value == 'custom') {
            $(page_link).hide();
            $(cat_link).hide();
            $(custom_link).show();
        }

        else {
            $(page_link).hide();
            $(cat_link).hide();
            $(custom_link).hide();
        }

    });

    $(type).change(function () {

        var t_value = $('#id_link_type').val();

        if (t_value == 'page') {
            $(page_link).show();
            $(cat_link).hide();
            $(custom_link).hide();
        }

        else if (t_value == 'category') {
            $(page_link).hide();
            $(cat_link).show();
            $(custom_link).hide();
        }

        else if (t_value == 'custom') {
            $(page_link).hide();
            $(cat_link).hide();
            $(custom_link).show();
        }

        else {
            $(page_link).hide();
            $(cat_link).hide();
            $(custom_link).hide();
        }

    });

});
