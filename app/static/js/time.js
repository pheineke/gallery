function updateTime() {
    let date_div = document.getElementById('date');
    let time_div = document.getElementById('time');
    

    setInterval(() => {
        let currentdate = new Date();
        let hours   = "00" + currentdate.getHours();
        let minutes = "00" + currentdate.getMinutes();
        let seconds = "00" + currentdate.getSeconds();

        let month   = "00" + (currentdate.getMonth() + 1);
        let year    = currentdate.getFullYear();

        let time = hours.slice(-2) + ":"  
                    + minutes.slice(-2) + ":" 
                    + seconds.slice(-2);

        time_div.innerHTML = time;

        let date = currentdate.getDate() + "."
                    + month.slice(-2) + "." 
                    + year;

        date_div.innerHTML = date;
    }, 1000); // Jede Sekunde aktualisieren
}

document.addEventListener("DOMContentLoaded", function() {
    updateTime();
});