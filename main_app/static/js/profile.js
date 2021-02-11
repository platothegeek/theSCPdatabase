$(document).ready(function(){
    $( "#myPgBtn" ).click(function() {
        $("#myPgBtn").css("color", "#9b0000");
        $("#saveBtn").css("color", "white");
        $("#myPages").css("display", "block");
        $("#savedPages").css("display", "none");
    })
    $( "#saveBtn" ).click(function() {
        $("#saveBtn").css("color", "#9b0000");
        $("#myPgBtn").css("color", "white");
        $("#myPages").css("display", "none");
        $("#savedPages").css("display", "block");
    })
}
)