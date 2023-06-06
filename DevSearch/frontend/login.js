const form = document.querySelector("#form");
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = {
        username: form.username.value,
        password: form.password.value,
    };
    console.log("Data: ", formData);
    fetch("http://127.0.0.1:8000/api/users/token/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("DATA: ", data.access);
            if (data.access) {
                localStorage.setItem("token", data.access);
                window.location = "http://127.0.0.1:5500/project-list.html";
            } else {
                alert("username or password did not work");
            }
        });
});
