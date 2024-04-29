document.addEventListener("DOMContentLoaded", function () {
    const loader = document.querySelector(".loader-div");
    var form = document.getElementById("PIC-form");
    var main = document.getElementById("main");

    form.addEventListener("submit", function (event) {

        // Add a class to the message div
        main.style.display = "none";
        loader.classList.add("loader--show");
    });
});