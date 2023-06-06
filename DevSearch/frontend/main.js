const projectURL = "http://127.0.0.1:8000/api/projects/";
const token = localStorage.getItem("token");
const loginBtn = document.querySelector("#login-btn");
const logoutBtn = document.querySelector("#logout-btn");

if (token) {
    loginBtn.remove();
} else {
    loginBtn.remove();
}

logoutBtn.addEventListener("click", (e) => {
    e.preventDefault();
    localStorage.removeItem("token");
    window.location = "http://127.0.0.1:5500/login.html";
});

let getProjects = () => {
    fetch(projectURL)
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            buildProject(data);
        });
};
let buildProject = (projects) => {
    let projectsWrapper = document.querySelector("#projects--wrapper");
    projectsWrapper.innerHTML = ``;
    for (let i = 0; i < projects.length; i++) {
        const element = projects[i];
        const projectCard = `
            <div class="project--card">
                
            <img src="http://127.0.0.1:8000${element.featured_image}"/>

            <div>
                <div class="card--header">
                    <h3>${element.title}</h3>
                    <strong class="vote--option" data-vote="up" data-project="${element.id}">&#43;</strong>
                    <strong class="vote--option" data-vote="down" data-project="${element.id}">&#8722;</strong>
                </div>
                <i>${element.vote_ratio}% Positive feedback</i>
                <p>${element.description.substring(0, 150)}...</p>
            </div>
            
            </div>
        `;
        projectsWrapper.innerHTML += projectCard;
    }
    addVoteEvents();
};

const addVoteEvents = () => {
    const voteBtns = document.querySelectorAll(".vote--option");
    for (let i = 0; i < voteBtns.length; i++) {
        const element = voteBtns[i];
        element.addEventListener("click", (e) => {
            const vote = e.target.dataset.vote;
            const project = e.target.dataset.project;
            console.log(token);

            fetch(`http://127.0.0.1:8000/api/project/${project}/vote/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({
                    value: vote,
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log("Success: ", data);
                    getProjects();
                });
        });
    }
};

getProjects();
