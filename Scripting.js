function buttClick(){
    var searchedItem = document.getElementById('searchID').innerHTML;
    var theTable = '<div>' + '<tr>' + ' ' + searchedItem + ' ' + '</tr>' + '</div>';
    var topOfDoc = '<!DOCTYPE html><html><head>'
    var upToBody = '</head><body>';
    var endOfDoc = '</body></html>' ;
    var thePage = topOfDoc + upToBody + theTable + endOfDoc
    
    
    var newPage = window.open("");
    newPage.document.write(thePage);


}