// Underlines current page in navbar
document.addEventListener("DOMContentLoaded", function () {
    var currentPage = window.location.pathname; // Get the current page filename
    var links = document.getElementsByClassName("navbar_item");

    for (var i = 0; i < links.length; i++) {
        var link = links[i];
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }
    }
});