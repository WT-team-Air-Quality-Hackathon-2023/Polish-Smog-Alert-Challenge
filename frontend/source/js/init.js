export function init() {
    setupGeolocation();
}

function setupGeolocation() {
    navigator.geolocation.getCurrentPosition(
        sendGeolocationData, 
        () => sendGeolocationData({
            coords: {
                latitude: "50.049683",
                longitude: "19.944544"
            }
        })
    );
}

function sendGeolocationData(coords) {
    fetch("/api/pollution", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            latitude: coords.coords.latitude,
            longitude: coords.coords.longitude
        }),
    })
    .then(res => res.json())
    .then(res => {
        setLungDarkness(res.lungs_coverage);
        setCurrentPollutionValue(res.current_value);
        setLocation(res.address);
    });
}

function setLungDarkness(opacity) {
    document.querySelector(".lung--dark").setAttribute("style", `opacity: ${opacity}`);
}

function setLocation(location) {
    document.querySelector(".location-text").innerText = location;
}

function setCurrentPollutionValue(pollutionValue) {
    document.querySelector(".pollution-value").innerText = pollutionValue;
}
