 $(document).ready(function(){
    $( "#foundBtn" ).click(function() {
        $("#foundBtn").css("color", "#9b0000");
        $("#secBtn").css("color", "white");
        $("#scpBtn").css("color", "white");
        $("#objBtn").css("color", "white");
        $("#theFoundation").css("display", "block");
        $("#objectClasses").css("display", "none");
        $("#securityClearences").css("display", "none");
        $("#whatIsAScp").css("display", "none");
    })
    $( "#objBtn" ).click(function() {
        $("#objBtn").css("color", "#9b0000");
        $("#foundBtn").css("color", "white");
        $("#scpBtn").css("color", "white");
        $("#secBtn").css("color", "white");
        $("#theFoundation").css("display", "none");
        $("#objectClasses").css("display", "inline");
        $("#securityClearences").css("display", "none");
        $("#whatIsAScp").css("display", "none");
    })
    $( "#secBtn" ).click(function() {
        $("#secBtn").css("color", "#9b0000");
        $("#foundBtn").css("color", "white");
        $("#scpBtn").css("color", "white");
        $("#objBtn").css("color", "white");
        $("#theFoundation").css("display", "none");
        $("#objectClasses").css("display", "none");
        $("#securityClearences").css("display", "inline");
        $("#whatIsAScp").css("display", "none");
    })
    $( "#scpBtn" ).click(function() {
        $("#scpBtn").css("color", "#9b0000");
        $("#foundBtn").css("color", "white");
        $("#secBtn").css("color", "white");
        $("#objBtn").css("color", "white");
        $("#theFoundation").css("display", "none");
        $("#objectClasses").css("display", "none");
        $("#securityClearences").css("display", "none");
        $("#whatIsAScp").css("display", "inline");
    })
}
)