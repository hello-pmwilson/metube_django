//Load Videos
//and load more when viewer has scrolled to the bottom
//quantityToLoad is a multiple of 3 and 4 so the apropriate number of videos loads
//no matter the viewport
//TO DO: set start with to look for index given in the url OR 0
//TO DO: set videosToLoad to actually pull videos from DB
let startWith = 0;
const quantityToLoad = 24;
const videosToLoad = [];

// When DOM loads, render the first 24 posts
document.addEventListener('DOMContentLoaded', loadVideos);

// If scrolled to bottom, load the next 24 posts
const smidge = 1 //in some views the possible scrollY is off a smidge to trigger load
window.onscroll = () => {
    if (window.innerHeight + window.scrollY + smidge >= document.body.offsetHeight) {
        loadVideos(); //load the next set of videos
    }
};


function loadVideos() {

    // Set start and end, updated startWith
    const start = startWith;
    const end = start + quantityToLoad;
    startWith = end;
    //create filler video and add to DOM
    //TO DO: abstract functions further
    for(let i = start; i < end; i++) {
        const generalVideo = document.getElementById('general-video');
        let newContent = document.createElement('div');
        newContent.className = "video";
        generalVideo.appendChild(newContent);
    }

};
