var foldBtns = document.getElementsByClassName("fold-button");
    for (var i = 0; i<foldBtns.length; i++){
        foldBtns[i].addEventListener("click", function(e) {
            if(e.target.parentElement.className=="one-post folded"){
                e.target.innerHTML="Свернуть";
                e.target.
                parentElement.
                className="one-post";
                console.log(e.target.parentElement.className)
                console.log("if")
            }
            else{
                e.target.innerHTML="Развернуть";
                e.target.
                parentElement.
                className="one-post folded";
                console.log(e.target.parentElement.className)
                console.log("Else")
        }
    });
}