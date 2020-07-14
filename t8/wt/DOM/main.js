function write_hello() {
    if (document.getElementById("img").getAttribute("src") === "loader.gif") {
        document.getElementById("img").src = "woof.gif";
        console.log("hello")
    } else {
        document.getElementById("img").src = "loader.gif";
        console.log("bye")
    }
}