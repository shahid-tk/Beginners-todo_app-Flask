function sendCheBox(elm){
    var dataToSend = { done : elm.checked, id : $(elm).data("dataid") };
    $.post("/update", dataToSend).done(function(data){
        console.log(data);
        window.location.reload(true);
    });
    console.log(dataToSend);
    if (elm.checked){

    }
}
