function to_redis(){
    var data_dict = {};
    var keyword_arr = new Array();
    var inputs = $('.queue-input')
    inputs.each(function(i,item){
        var keyword = $(item).val()
        if(keyword.length > 0){
            keyword_arr.push(keyword)
        }
    })

    data_dict['keyword'] = JSON.stringify(keyword_arr);
    data_dict['csrfmiddlewaretoken'] = $('input[name="csrfmiddlewaretoken"]').val();
     $.ajax({
        type:"POST",
        url: "",
        data:data_dict,

        success:function(data){
            alert('success');
        }
    })
}