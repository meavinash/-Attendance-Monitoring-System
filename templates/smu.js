
document.getElementById("myButton").addEventListener("click", goPython);
        function goPython(){

            jquery.ajax({
              url: "/attendance/"
            }).done(function() {
             alert('finished python script');
            });
}
