onload = main;

const URLDOMAIN = ""

function getResponse(inputValue) {
    let xhr = new XMLHttpRequest();
    let url = `${URLDOMAIN}/send_message?query=${encodeURIComponent(inputValue)}`;

    xhr.open("GET", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            if (xhr.status == 200) {
                let response = JSON.parse(xhr.responseText);
                
                const chatBox = document.getElementById("chat-box");
                const systemMessage = document.createElement("div");

                systemMessage.classList.add("message", "system");
                console.log(response.filtered_data);
                for (code in response.filtered_data) {
                    productLink = document.createElement("a");
                    productLink.innerHTML = response.filtered_data[code];
                    productLink.href = `${URLDOMAIN}/inspect/${response.filtered_data[code]}`;
                    systemMessage.appendChild(productLink);

                    br = document.createElement("br");
                    systemMessage.appendChild(br);
                }

                chatBox.appendChild(systemMessage);

                // Scroll to the bottom of the chat box
                chatBox.scrollTop = chatBox.scrollHeight;
            } else {
                console.error("Error:", xhr.responseText);
            }
        }
    };
    xhr.send();
}

function main() {
    Array.from(document.getElementsByClassName("inspect-item")).forEach(element => {
        element.addEventListener("click", function () {
            window.location.href = `${URLDOMAIN}/inspect/${element.id}`;
        });
    });

    // Open modal when the upload button is clicked
    document.getElementById("upload-product").addEventListener("click", function () {
        document.getElementById("uploadModal").style.display = "block";
    });

    // Close modal when the close button is clicked
    document.getElementById("close-modal").addEventListener("click", function () {
        document.getElementById("uploadModal").style.display = "none";
    });

    // Close modal when clicking outside of the modal content
    window.addEventListener("click", function (event) {
        if (event.target === document.getElementById("uploadModal")) {
            document.getElementById("uploadModal").style.display = "none";
        }
    });

    // Handle form submission (upload PDF)
    document.getElementById('uploadForm').addEventListener('submit', async function (event) {
        event.preventDefault();  // Prevent default form submission

        // Get the file input and the file itself
        const fileInput = document.getElementById('fileInput');
        const file = fileInput.files[0];

        if (!file) {
            alert('Please select a PDF file to upload.');
            return;
        }

        // Create FormData to send the file
        const formData = new FormData();
        formData.append('file', file);

        try {
            // Send the file via a POST request to the Django endpoint
            const response = await fetch('/analyze-layout/', {
                method: 'POST',
                body: formData,
            });

            // Handle the response
            const data = await response.json();
            const responseMessage = document.getElementById('responseMessage');

            if (response.ok) {
                responseMessage.innerHTML = `<p style="color: green;">${data.message}</p>`;
            } else {
                responseMessage.innerHTML = `<p style="color: red;">${data.message}</p>`;
            }

        } catch (error) {
            console.error('Error:', error);
            document.getElementById('responseMessage').innerHTML = `<p style="color: red;">Error occurred while uploading.</p>`;
        }
    });

    document.getElementById("open-chat").addEventListener("click", function () {
        document.getElementById("chatModal").style.display = "block";
        document.getElementById("chatModal").style.transform = "translateY(0)";
    });

    // Close the chat modal when the close button is clicked
    document.getElementById("close-chat").addEventListener("click", function () {
        document.getElementById("chatModal").style.transform = "translateY(100%)";
        setTimeout(() => {
            document.getElementById("chatModal").style.display = "none";
        }, 300);  // Match with transition time
    });

    document.getElementById("send-message").addEventListener("click", function () {
        const messageText = document.getElementById("chat-input").value.trim();

        if (messageText) {
            const chatBox = document.getElementById("chat-box");
            const userMessage = document.createElement("div");
            userMessage.classList.add("message", "user");
            userMessage.innerHTML = `<p>${messageText}</p>`;
            chatBox.appendChild(userMessage);

            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;

            // Clear the input field
            document.getElementById("chat-input").value = "";
            getResponse(messageText)
        }
    });
}