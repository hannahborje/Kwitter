/*
  TDP013
  Laboration 1
  lab1.js
  Per Jonsson, Hannah Börjesson IP2

  Uppfyller kravet att meddelanden som publiceras ska valideras med JavaScript
*/

var validateInput = function()
{
    var reset = "";
    var errorMsg = "Ditt inlägg måste vara mellan 1 och 140 tecken"; // KRAV
    var tweetLength = document.getElementById("textarea").value.length;
    var invalidTweet = (tweetLength == 0 || tweetLength > 140);
       
    // Skicka felmeddelande om tweeten är felaktig (KRAV), annars återställ
    document.getElementById("error").innerHTML = (invalidTweet) ? errorMsg : reset;
    // Skicka tweeten om den är giltig
    if (!(invalidTweet)) createTweet();
};

var createTweet = function()
{
    // Hämta innehållet till tweet:en
    var tweet = document.getElementById("textarea").value;
    // Skapa behållare till tweet
    var tweetDiv = document.createElement("div");
    tweetDiv.id = "tweetmsg";
    // Skapa ny tweet-text 
    var msgNode = document.createTextNode(tweet);
    // Lägg till texten till div:en
    tweetDiv.appendChild(msgNode);
    // Skapa knapp för att markera läst text
    var disableButton = document.createElement("input");
    disableButton.type = "checkbox";
    disableButton.id = "checkbox";
    // Lägg knappen bredvid tweet:en
    tweetDiv.appendChild(disableButton);
    // Gör så att man kan markera den som oläst också
    disableButton.onclick = markAsRead;

    // Infoga meddelandena
    // KRAV: Tweets ska visas i ordningen "senast först"
    var tweets = document.getElementById("tweet");
    tweets.insertBefore(tweetDiv, tweets.childNodes[0]);
    
    // Återställ textarean efter varje tweet
    var textarea = document.getElementById("textarea");
    textarea.value = "Sjung ut!";
};

var resetText = function()
{
    // Gör textrutan tom
    var reset = "";
    document.getElementById("textarea").value = reset;
};

var markAsRead = function(event)
{
    // Markera som läst och ta bort knappen
    // KRAV: Det ska vara tydlig skillnad mellan lästa/olästa tweets
    var node = event.target.parentNode;
    node.style.opacity = "0.2";
    node.removeChild(node.childNodes[1]);
};
