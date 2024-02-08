// Function to handle user input and get bot response

function getBotResponse() {
    var image = '<img src="https://cdn.iconscout.com/icon/premium/png-256-thumb/ai-robot-5-1089411.png" alt="Hello" width="25">';
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";

    $("#textInput").val("");
    $("#chatbox").append(userHtml);

    document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
    
    // Send user message to server and receive bot response
    $.get("/get", { msg: rawText }).done(function (data) {
        var botHtml = image + '<p class="botText"><span>' + data + "</span></p>";
        
        $("#chatbox").append(botHtml);
        
        document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
    });
}

// Event listener for Enter key press in user input field
$("#textInput").keypress(function (e) {
    if (e.which == 13) { // If Enter key is pressed
        getBotResponse(); // Call getBotResponse function
    }
});
