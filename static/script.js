let jobId = null;

function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) {
        alert("Please select a file");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    document.getElementById("progressContainer").style.display = "block";
    document.getElementById("status").innerText = "Uploading...";

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        jobId = data.job_id;
        document.getElementById("status").innerText = "Analyzing...";
        pollStatus();
    });
}

function pollStatus() {
    const interval = setInterval(() => {
        fetch(`/status/${jobId}`)
            .then(res => res.json())
            .then(data => {
                if (data.status === "completed") {
                    clearInterval(interval);
                    document.getElementById("progressContainer").style.display = "none";
                    document.getElementById("status").innerText = "Completed ✅";
                    document.getElementById("transcript").innerText = data.transcript;

                    const badge = document.getElementById("sentiment");
                    badge.innerText = data.sentiment;

                    badge.className = "badge " +
                        (data.sentiment === "Positive" ? "bg-success" :
                        data.sentiment === "Negative" ? "bg-danger" : "bg-secondary");
                }

                if (data.status === "error") {
                    clearInterval(interval);
                    document.getElementById("status").innerText = "Error ❌";
                }
            });
    }, 2000);
}
