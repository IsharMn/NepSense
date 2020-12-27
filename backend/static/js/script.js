window.addEventListener("load", () => {
    var table = document.querySelectorAll(".table-row")
    console.log(table)

    for (i = 0; i < table.length; i++) {
        element = table[i]
        diff = element.children[4];
        img = diff.children[0];
        if (parseInt(diff.innerText) < 0){
            diff.style.color="red"
            img.src = "/static/images/decrease.gif"
        }
        else if (parseInt(diff.innerText) > 0){
            diff.style.color = "green"
            img.src = "/static/images/increase.gif"
        }
        else {
            diff.style.color = "blue"
            img.src = "/static/images/nil.gif"
        }
    };
})