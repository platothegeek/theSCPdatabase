$(document).ready(function(){
    $( "#AWCYBtn" ).click(function() {
        $("#AWCYBtn").css("color", "#9b0000");
        $("#MCDBtn").css("color", "white");
        $("#TCIBtn").css("color", "white");
        $("#FCDBtn").css("color", "white");
        $("#GRUPBtn").css("color", "white");
        $("#AWCYcontent").css("display", "block");
        $("#TCIcontent").css("display", "none");
        $("#MCDcontent").css("display", "none");
        $("#FCDcontent").css("display", "none");
        $("#GRUPcontent").css("display", "none");
    })
    $( "#TCIBtn" ).click(function() {
        $("#TCIBtn").css("color", "#9b0000");
        $("#MCDBtn").css("color", "white");
        $("#AWCYBtn").css("color", "white");
        $("#FCDBtn").css("color", "white");
        $("#GRUPBtn").css("color", "white");
        $("#AWCYcontent").css("display", "none");
        $("#TCIcontent").css("display", "block");
        $("#MCDcontent").css("display", "none");
        $("#FCDcontent").css("display", "none");
        $("#GRUPcontent").css("display", "none");
    })
    $( "#MCDBtn" ).click(function() {
        $("#MCDBtn").css("color", "#9b0000");
        $("#AWCYBtn").css("color", "white");
        $("#TCIBtn").css("color", "white");
        $("#FCDBtn").css("color", "white");
        $("#GRUPBtn").css("color", "white");
        $("#AWCYcontent").css("display", "none");
        $("#TCIcontent").css("display", "none");
        $("#MCDcontent").css("display", "block");
        $("#FCDcontent").css("display", "none");
        $("#GRUPcontent").css("display", "none");
    })
    $( "#FCDBtn" ).click(function() {
        $("#FCDBtn").css("color", "#9b0000");
        $("#MCDBtn").css("color", "white");
        $("#TCIBtn").css("color", "white");
        $("#AWCYBtn").css("color", "white");
        $("#GRUPBtn").css("color", "white");
        $("#AWCYcontent").css("display", "none");
        $("#TCIcontent").css("display", "none");
        $("#MCDcontent").css("display", "none");
        $("#FCDcontent").css("display", "block");
        $("#GRUPcontent").css("display", "none");
    })
    $( "#GRUPBtn" ).click(function() {
        $("#GRUPBtn").css("color", "#9b0000");
        $("#MCDBtn").css("color", "white");
        $("#TCIBtn").css("color", "white");
        $("#AWCYBtn").css("color", "white");
        $("#FCDBtn").css("color", "white");
        $("#AWCYcontent").css("display", "none");
        $("#TCIcontent").css("display", "none");
        $("#MCDcontent").css("display", "none");
        $("#FCDcontent").css("display", "none");
        $("#GRUPcontent").css("display", "block");
    })
}
)