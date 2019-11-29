function responsive() {
    var x = document.getElementById("navLink");
    if (x.className === "navLink") {
        x.className += "responsive";
    } else {
        x.className = "navLink";
    }
}