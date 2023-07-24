if (typeof window !== "undefined")
{

    
    window.addEventListener("scroll", () => {

        const header_nav = document.querySelector(".nav-container")
        if (window.scrollY > 0){
            header_nav.classList.add("sticky");
            console.log("here")
        }
        else{
            header_nav.classList.remove("sticky")
        }
        console.log("here")

        //scroll to top page  
    const topBtn = document.querySelector(".scroll-to-top-btn");
        if (window.pageYOffset > 100){
            topBtn.classList.add("active-top-btn");
            console.log("here")
        }else {
            topBtn.classList.remove("active-top-btn");
        }
    })
    // window.addEventListener('scroll', function(){
    //     var header_nav = document.getElementsByClassName("nav-container")
    // })


}


