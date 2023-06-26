$(document).ready(function () {

    //When page loads...
    $(".tab_content, .tab_content_child").slideUp(); //Hide all content
    $("ul.tabs2 li:first").addClass("active").slideDown(); //Activate first tab
    $("ul.tabs_child li:first").addClass("active").slideDown(); //Activate first tab
    $(".tab_content:first").slideDown(); //Show first tab content
    $(".tab_content_child:first").slideDown(); //Show first tab content


    //On Click Event
    $("ul.tabs2 li").click(function () {

        $("ul.tabs2 li").removeClass("active"); //Remove any "active" class
        $(this).addClass("active"); //Add "active" class to selected tab
        $(".tab_content").slideUp(); //Hide all tab content

        var activeTab = $(this).find("a").attr("href"); //Find the href attribute value to identify the active tab + content
        $(activeTab).slideDown(); //Fade in the active ID content
        return false;
    });
    //On Click child tabs Event
    $("ul.tabs_child li").click(function () {
        $("ul.tabs_child li").removeClass("active"); //Remove any "active" class
        $(this).addClass("active"); //Add "active" class to selected tab
        $(".tab_content_child").slideUp(); //Hide all tab content
        var activeTab = $(this).find("a").attr("href"); //Find the href attribute value to identify the active tab + content
        $(activeTab).slideDown(); //Fade in the active ID content
        return false;
    });
});