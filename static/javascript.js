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

function cheBox(val){
    var checkBox = document.getElementById("myCheck");
    if (checkBox.checked == true){
        console.log('checked ' + val)
        var dataToSend = {
            id : val, 
            done : true,
        };
        fetch(`${window.origin}/update`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(dataToSend),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        }).then(function(responce){
            if (responce.status !== 200){
                console.log(`Responce status was not 200: ${responce.status}`)
            }
            responce.json().then(function(data){
                console.log(data)
            })
        })
        
    } else {
        console.log('unchecked ' + val)
        var dataToSend = {
                id : val,
                done : false,
            };
            fetch(`${window.origin}/update`, {
                method: "POST",
                credentials: "include",
                body: JSON.stringify(dataToSend),
                cache: "no-cache",
                headers: new Headers({
                    "content-type": "application/json"
                })
            })
    }
}