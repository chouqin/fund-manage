$('document').ready(function(){
    //var autocomleteOption = {
        //source: ['教师1', '教师2', '俞勇', '茅旭初'],
        //select: function(event, ui){
            ////ui.item.option.selected = true;
            //$(this).data('uiItem', ui.item.value);
            //$(this).val('1234');
            ////alert($(this).val());
            ////self._trigger('selected', event, {
                ////item: ui.item.option
            ////});
        //},
        //change: function(event, ui) {
            //if( !ui.item) {
                //$(this).val('');
                ////select.val('');
                ////input.data('autocomplete').term = '';
                //return false;
            //}
        //}
    //};

    $('input, textarea').uniform();
    $('#cdate').datepicker();
    $('#edate').datepicker();
    //$("#date").datepicker();
    //$("#cdate").datepicker({ showOn: 'button',buttonImageOnly: true, buttonImage: '/static/images/icon_cal.png', altField: 'input#cdate', altFormat: 'yy-mm-dd'});
    //$("#edate").datepicker({ showOn: 'button', buttonImageOnly: true, buttonImage: '/static/images/icon_cal.png', altField: 'input#edate', altFormat: 'yy-mm-dd' });
    $("#cdate").datepicker('option', $.datepicker.regional['zh-CN']);
    $("#cdate").datepicker('option', 'dateFormat','yy-mm-dd');//set dateFormat
    //$( "#cdate" ).datepicker( "option", "autoSize", true );
    $( "#cdate" ).datepicker( "option", "changeMonth", true );
    $( "#cdate" ).datepicker( "option", "changeYear", true );
    $("#edate").datepicker('option', $.datepicker.regional['zh-CN']);
    $("#edate").datepicker('option', 'dateFormat','yy-mm-dd');//set dateFormat
    //$( "#cdate" ).datepicker( "option", "autoSize", true );
    $( "#edate" ).datepicker( "option", "changeMonth", true );
    $( "#edate" ).datepicker( "option", "changeYear", true );
    $('tr:odd').addClass('alt');
    $('#project_add_form input.teacher').autocomplete({
        source: function(request, response){
            url = "/teacher/search/" + request.term;

            $.getJSON(url, function(data) {
                response(data);
            });
        },
        select: function(event, ui){
            $(this).val(ui.item.label);
            $(this).next().val(ui.item.value);
            return false;
        },
        change: function(event, ui) {
            if( !ui.item) {
                $(this).val('');
                $(this).next().val('');
                return false;
            }
        }
    });
    $('#addteacher').click(function(){
        //alert("here");
        $('<input class="teacher" type="text" name="teachers"></input> <input class="teache_id" type="hidden" name="teachers"></input>')
        .insertBefore($(this))
        .autocomplete({
            source: function(request, response){
                url = "/teacher/search/" + request.term;

                $.getJSON(url, function(data) {
                    response(data);
                });
            },
            select: function(event, ui){
                $(this).val(ui.item.label);
                $(this).next().val(ui.item.value);
                return false;
            },
            change: function(event, ui) {
                if( !ui.item) {
                    $(this).val('');
                    $(this).next().val('');
                    return false;
                }
            }
        });
        //$(this).before();
        return false;
    });
    //$("#datepicker").datepicker({clickInput:true});
});
