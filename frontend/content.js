function getComments() {
  return Array.from(
    document.querySelectorAll(
      "ytd-comment-thread-renderer yt-attributed-string span"
    )
  )
    .map(el => el.innerText.trim())
    .filter(Boolean);
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "FETCH_COMMENTS") {
    const comments = getComments();

    if (comments.length === 0) {
      sendResponse({ status: "No comments found" });
      return;
    }

    sendCommentsToServer(comments);
    sendResponse({ status: "Comments sent to server" });
  }
});

function sendCommentsToServer(commentsArray) {
  fetch("http://127.0.0.1:8000/preprocess", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ comments: commentsArray })
  })
    .then(res => res.json())
    .then(data => {
      chrome.storage.local.set({ sentiments: data });
      console.log("Sentiment result:", data);
    })
    .catch(err => console.error("API error:", err));
}
