$('document').ready(function(){
    $('input, textarea, select').uniform();
    $('#cdate').datepicker();
    $('#edate').datepicker();
    $("#cdate").datepicker('option', $.datepicker.regional['zh-CN']);
    $("#cdate").datepicker('option', 'dateFormat','yy-mm-dd');//set dateFormat
    $( "#cdate" ).datepicker( "option", "changeMonth", true );
    $( "#cdate" ).datepicker( "option", "changeYear", true );
    $("#edate").datepicker('option', $.datepicker.regional['zh-CN']);
    $("#edate").datepicker('option', 'dateFormat','yy-mm-dd');//set dateFormat
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
    $('button').button();
    $('button.project-add-device').click(function(){
        $('#submit_type').val('add_device');
        $('form').submit();
        return false;
    });
    $('button.project-add-business').click(function(){
        $('#submit_type').val('add_business');
        $('form').submit();
        return false;
    });
    $('button.project-add').click(function(){
        $('#submit_type').val('save');
        $('form').submit();
        return false;
    });
});
