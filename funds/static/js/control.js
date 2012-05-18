$('document').ready(function(){

    $('input, textarea').uniform();
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
    $('#project-form input.teacher').autocomplete({
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
        $('<input class="teacher" type="text" name="teacher_name"></input> <input class="teache_id" type="hidden" name="teachers"></input>')
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
    //$('a').button();
    $('a.view').button();
    $('a.edit').button();
    $('a.delete').button();
    $('a.choose').button();
    $('a.return').button();
    $('a.teacher-add').button();
    $('a.project-edit').button();
    $('a.project-view').button();
    $('a.project-add').button();
    $('a.project-add-business').button();
    $('a.project-add-device').button();
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

    $.validator.addMethod(
        "regex",
        function(value, element, regexp) {
            var re = new RegExp(regexp);
            return this.optional(element) || re.test(value);
        },
        "请输入合法数据"
    );

    //$("#business-form #total").rules("add", { regex: "(^[0-9]+\.[0-9]+$)|(^[0-9]+$)" });
    //$("#device-form #price").rules("add", { regex: "(^[0-9]+\.[0-9]+$)|(^[0-9]+$)" });
    //$("#device-form #amount").rules("add", { regex: "^[0-9]+$" });

    $('#teacher-form').validate({
        messages: {
            name: '请输入教师姓名',
            title: '请输入教师职称'
        }
    });

    $('#project-form').validate({
        messages: {
            teacher_name: '请输入教师',
            name: '请输入项目名称',
            created_at: '请输入起始时间',
            ended_at: '请输入结束时间'
        }
    });

    $('#device-form').validate({
        messages: {
            name: '请输入设备名称',
            specification: '请输入设备规格',
            maker: '请输入生产厂商',
            price: '请正确输入单价',
            amount: '请正确输入数目',
            position: '请输入安装地点',
            usage: '请输入用途',
        }
    });

    $('#business-form').validate({
        messages: {
            total: '请正确输入数目',
        }
    });

});
