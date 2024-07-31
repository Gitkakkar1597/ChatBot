// Function to handle user input and get bot response

function getBotResponse() {
    // Define image HTML for bot avatar
    var image = '<img src="https://cdn.iconscout.com/icon/premium/png-256-thumb/ai-robot-5-1089411.png" alt="Hello" width="25">';
    
    // Get user input text from the input field
    var rawText = $("#textInput").val();
    
    // Create HTML structure for user's message
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";

    // Clear the input field after getting user input
    $("#textInput").val("");
    
    // Append user's message to the chatbox
    $("#chatbox").append(userHtml);

    // Scroll to the bottom of the user input area smoothly
    document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
    
    
    // Send user message to server and receive bot response

    $.get("/get", { msg: rawText }).done(function (data) {
        // Create HTML structure for bot's response including the bot avatar
        var botHtml = image + '<p class="botText"><span>' + data + "</span></p>";
        
        // Append bot's response to the chatbox
        $("#chatbox").append(botHtml);
        
        // Scroll to the bottom of the user input area smoothly after bot response
        document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
    });
}

// Event listener for Enter key press in user input field
$("#textInput").keypress(function (e) {
    if (e.which == 13) { // If Enter key is pressed
        getBotResponse(); // Call getBotResponse function to handle user input
    }
});
