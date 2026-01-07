document.getElementById("fetchButton").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "FETCH_COMMENTS" }, () => {
            setTimeout(displayProcessedData, 1000);
        });
    });
});

function displayProcessedData() {
    chrome.storage.local.get(["sentiments"], (result) => {
        const output = document.getElementById("output");

        if (!result.sentiments) {
            output.textContent = "No data received yet.";
            return;
        }

        const { positive, negative, neutral } = result.sentiments;

        output.textContent =
            `Positive: ${positive}\n` +
            `Negative: ${negative}\n` +
            `Neutral: ${neutral}`;
    });
}

document.addEventListener("DOMContentLoaded", displayProcessedData);
