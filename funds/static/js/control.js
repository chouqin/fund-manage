$('document').ready(function(){
    $('input, textarea, select').uniform();
    $("#cdate").datepicker({ showOn: 'button',buttonImageOnly: true, buttonImage: '/static/images/icon_cal.png', altField: 'input#cdate', altFormat: 'yy-mm-dd'});
    $("#edate").datepicker({ showOn: 'button', buttonImageOnly: true, buttonImage: '/static/images/icon_cal.png', altField: 'input#edate', altFormat: 'yy-mm-dd' });
    
    $('tr:odd').addClass('alt');
    $('#project_add_form input.teacher').autocomplete({
        source: ['教师1', '教师2', '俞勇', '茅旭初'],
        select: function(event, ui){
            //ui.item.option.selected = true;
            $(this).data('uiItem', ui.item.value);
            $(this).val('1234');
            //alert($(this).val());
            //self._trigger('selected', event, {
                //item: ui.item.option
            //});
        },
        change: function(event, ui) {
            if( !ui.item) {
                $(this).val('');
                //select.val('');
                //input.data('autocomplete').term = '';
                return false;
            }
        }
    });
    $('#addteacher').click(function(){
        //alert("here");
        $('<input class="teacher" type="text" name="teachers"></input>')
        .insertBefore($(this))
        .autocomplete({
            source: ['教师1', '教师2', '俞勇', '茅旭初'],
            select: function(event, ui){
                //ui.item.option.selected = true;
                $(this).data('uiItem', ui.item.value);
                $(this).val('1234');
                //alert($(this).val());
                //self._trigger('selected', event, {
                    //item: ui.item.option
                //});
            },
            change: function(event, ui) {
                if( !ui.item) {
                    $(this).val('');
                    //select.val('');
                    //input.data('autocomplete').term = '';
                    return false;
                }
            }
        });
        //$(this).before();
        return false;
    });
    $("#datepicker").datepicker({clickInput:true});
     //$(".datepicker").datepicker('option', $.datepicker.regional['zh-CN']);
     ////$("#datepicker").datepicker($.datepicker.regional['zh-CN']);//该句执行失效，因为之前有$("#datepicker").datepicker();了
     //$(".datepicker").datepicker('option', 'dateFormat','yy-mm-dd');//set dateFormat
});
