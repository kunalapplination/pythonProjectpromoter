
function testData(path,playerName) {
    console.log("path, "+path+"!")
        console.log("playerName, "+playerName+"!")

}
function xPathEvent(xpathToExecute){
  var result = [];
  var nodesSnapshot = document.evaluate(xpathToExecute, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null );
  for ( var i=0 ; i < nodesSnapshot.snapshotLength; i++ ){
    result.push( nodesSnapshot.snapshotItem(i) );
  }
  return result;
}

xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]")[0].textContent='Vishal'; // team 1
xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[3]")[0].textContent='Kunal';  // team 1
xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div[3]")[0].textContent='Sumit';  // team 2
xPathEvent("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[3]")[0].textContent='Kumar';  // team 2