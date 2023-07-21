if (typeof window !== "undefined")
{

    //scroll to top page  
    const topBtn = document.querySelector(".scroll-to-top-btn");
    window.addEventListener("scroll",() => {
        if (window.pageYOffset > 100){
            topBtn.classList.add("active-top-btn");
            
        }else {
            topBtn.classList.remove("active-top-btn");
        }
    })
    


}


