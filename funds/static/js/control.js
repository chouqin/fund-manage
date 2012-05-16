$('document').ready(function(){
    $('input, textarea, select').uniform();
    $("#cdate").datepicker({ showOn: 'button',buttonImageOnly: true, buttonImage: '/static/images/icon_cal.png', altField: 'input#cdate', altFormat: 'yy-mm-dd'});
    $("#edate").datepicker({ showOn: 'button', buttonImageOnly: true, buttonImage: '/static/images/icon_cal.png', altField: 'input#edate', altFormat: 'yy-mm-dd' });
    
});
