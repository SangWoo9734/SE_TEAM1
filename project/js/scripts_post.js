/*!
* Start Bootstrap - Blog Post v4.3.0 (https://startbootstrap.com/template/blog-post)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-post/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

    // configuration of our firebase
    var firebaseConfig = {
        apiKey: "AIzaSyD6ncJWml82Xzk_dVYydIC8NzBUawuJb9E",
        authDomain: "se-termproject-team1.firebaseapp.com",
        projectId: "se-termproject-team1",
        storageBucket: "se-termproject-team1.appspot.com",
        messagingSenderId: "197301464509",
        appId: "1:197301464509:web:775de202359b76b06836d4"
        };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    var db = firebase.firestore();
    // user status listener
    firebase.auth().onAuthStateChanged(function(user) {
    if (user) { // In log-in status, display sign-out button
        var login = document.getElementById("login");
        var logout = document.getElementById("logout");

        login.style.display = 'none';
        logout.style.display = 'block';
    }
    else { // In log-out status, display sign-in button
        var login = document.getElementById("login");
        var logout = document.getElementById("logout");

        login.style.display = 'block';
        logout.style.display = 'none';
    }
});

var postInfoRef = db.collection('Post');

// Add Post in Html
function addQuery(querySnapshot){
    var num = 0;
    if (querySnapshot) {
            //Extract the required data for each post and output it on the web
            querySnapshot.forEach(function(doc){
                num += 1;
                let docs = doc.data();
                var userId = docs['UID'].split('@')[0];
                var userIdSecret = userId.replace(userId.substr(3), "*".repeat(userId.substr(3).length));
                var post =  '<tr class = "post">\n' +
                '<td class = "post-num">' + num + '</td>\n' +
                '<td class = "post-link"><div onclick = "getPost(\'' + doc.id + '\')">' + docs['Title'] + '</div></td>\n' +
                '<td class = "post-writer">' + userIdSecret + '</td>\n' +
                '</tr>';
        
                $("#post-list").append(post);
                
            });
        //call Error Code
        } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
        }
    
    $("#post-list").append('<tr><td colspan = "3" class = "post-last post"></td></tr>');
};

// When loading a post list screen, all the posts can be printed
function allPost(){
    postInfoRef.get().then(function (querySnapshot){
        addQuery(querySnapshot);
    }).catch(function(error) {
        console.log("Error getting document:", error);
    });
};

allPost(postInfoRef);

// Filter the posts and hand over the results.
function searchPost(){

    // Get words from search bar
    var words  = document.getElementById('search-word').value;

    // Remove all post in post list
    $(".post").detach();

    // If there are no search terms, show all posts and print out error messages
    if (!words){
        allPost(postInfoRef);
        return alert("검색어를 확인해주세요.");
    }
    var num = 0;
    
    // Loads post information from which containing search terms.
    postInfoRef.get().then(function (querySnapshot){
        if (querySnapshot) {
            querySnapshot.forEach(function(doc){
                let docs = doc.data();
                if(docs["Title"].includes(words) || docs['Content'].includes(words)){
                    num += 1;
                    var userId = docs['UID'].split('@')[0];
                    var userIdSecret = userId.replace(userId.substr(3), "*".repeat(userId.substr(3).length));

                    var post =  '<tr class = "post">\n' +
                    '<td class = "post-num">' + num + '</td>\n' +
                    '<td class = "post-link"><div onclick = "getPost(\'' + doc.id + '\')">' + docs['Title'] + '</div></td>\n' +
                    '<td class = "post-writer">' + userIdSecret + '</td>\n' +
                    '</tr>';
                    $("#post-list").append(post);
                }
            });

            if (num == 0){
                var post = '<tr class = "post">\n' +
                '<td class = "post-num post-none" colspan = "3"> No Search Results </td>\n' + '</tr>\n' + '<tr ><td class = "post-last post" colspan = "3"></td></tr>';
        
                $("#post-list").append(post);
            }else{
                $("#post-list").append('<tr class = "post-last post"><td colspan = "3"></td></tr>');
            }

        } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
        }
        // Call error message.
    }).catch((error) => {
        console.log("Error getting documents: ", error);
        var post = '<tr class = "post">\n' +
        '<td class = "post-last" colspan = "3"> No Search Results </td>\n' + '</tr>';
        
        $("#post-list").append(post);
    });

    
};

// React search function with ENTER key
function enterkey() {
    if (window.event.keyCode == 13) {
        searchPost();
    }
}

// Move to Specific Post
function getPost(id){
    window.location.href="post.html?index=" + id;
}