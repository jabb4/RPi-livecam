window.addEventListener("load", () => {
    const loader = document.querySelector(".loader-div");
    loader.classList.add("loader--hidden");
    loader.addEventListener("transitionend", () => {
        document.body.removeChild(loader);
    });
    var main = document.getElementById("main");
    main.style.display = "flex";
});