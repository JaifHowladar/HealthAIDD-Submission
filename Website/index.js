const scanText = document.querySelector("#loading-text");

const scan = () => {
    setTimeout(() => {
        scanText.textContent = "Starting Scan";
    }, 0);

    setTimeout(() => {
        scanText.textContent = "Starting Scan .";
    }, 1000);

    setTimeout(() => {
        scanText.textContent = "Starting Scan ..";
    }, 2000);

    setTimeout(() => {
        scanText.textContent = "Starting Scan ...";
    }, 3000);

    setTimeout(() => {
        scanText.textContent = "Scanning";
    }, 5000);

    setTimeout(() => {
        scanText.textContent = "Thermals";
    }, 10000);

    setTimeout(() => {
        scanText.textContent = "Scan Completed.";
    }, 13000);

}

scan();
