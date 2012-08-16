function deletePost(url)
{
    var xmlHTTP = null;
    xmlHTTP = new XMLHttpRequest();
    xmlHTTP.open("POST", url, false);
    xmlHTTP.send();

    window.location = "../";
}
