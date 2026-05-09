const username =
    localStorage.getItem("ipl_username");

document.getElementById(
    "playerName"
).innerText =
    "Welcome " + username;
