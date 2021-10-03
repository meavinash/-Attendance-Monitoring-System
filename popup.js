var button = document.getElementById("btn1");
button.addEventListener("click", function(){
    chrome.tabs.create({url:"templates/model.html"});
});