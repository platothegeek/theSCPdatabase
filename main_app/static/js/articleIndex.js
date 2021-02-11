function goToSeries1() {
    console.log("SERIES 1")
    const topPage = document.getElementById('logoScp')
    const targetLi = document.getElementById("seriesOneMarker")
    console.log(targetLi.offsetTop - 180)
    targetLi.scrollIntoView();
    topPage.scrollIntoView();
};
function goToSeries2() {
    console.log("SERIES 2")
    const targetLi = document.getElementById("seriesTwoMarker")
    const topPage = document.getElementById('logoScp')
    console.log(targetLi.offsetTop)
    targetLi.scrollIntoView();
    topPage.scrollIntoView();
};
function goToSeries3() {
    console.log("SERIES 3")
    const topPage = document.getElementById('logoScp')
    const targetLi = document.getElementById("seriesThreeMarker")
    console.log(targetLi.offsetTop)
    targetLi.scrollIntoView();
    topPage.scrollIntoView();
};
function goToSeries4() {
    console.log("SERIES 4")
    const topPage = document.getElementById('logoScp')
    const targetLi = document.getElementById("seriesFourMarker")
    console.log(targetLi.offsetTop)
    targetLi.scrollIntoView({ behavior: 'smooth'});
    topPage.scrollIntoView();
};