(function() {
    document.getElementById("file_input").onchange = function(){
      var files = document.getElementById("file_input").files;
      var file = files[0];
      if(!file){
        return alert("No file selected.");
      }
      getSignedRequest(file);
    };
  })();