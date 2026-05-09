function enterLobby() {

    const username =
        document.getElementById("username").value;

    if(username.trim() === "") {

        alert("Enter username");

        return;
    }

    localStorage.setItem(
        "ipl_username",
        username
    );

    alert(
        "Welcome " + username
    );
}
