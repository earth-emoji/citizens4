$( document ).ready(function() {

    load_data("/api/organizations/", function(json) {
        for(var i = 0; i < json.length; i++) {
            $("#orgs").append("<li><a href='/organizations/"+ json[i].slug + "/'>" + json[i].name +"</a></li>");
        }
    });

    // Submit post on submit
    $('#org-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        
        var url = "/api/organizations/";
        var data = { 
            name : $('#name').val(),
            desc: $('#desc').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#org-form")[0].reset();
            var content = "<li><a href='/organizations/"+ json.slug + "/'>" + json.name +"</a></li>";
            $("#orgs").append(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });


});
