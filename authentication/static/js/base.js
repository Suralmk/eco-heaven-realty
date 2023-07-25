if (typeof window !== "undefined")
{


    window.addEventListener("scroll", () => {
        //fixed nav bar
        const headerNav = document.querySelector(".nav-container")
        const heroContainer = document.querySelector(".hero-container")
        if (window.scrollY > 0){
            headerNav.classList.add("sticky");
            heroContainer.classList.add("hero-contain");
        }
        else{
            headerNav.classList.remove("sticky")
        }


        //scroll to top page  
    const topBtn = document.querySelector(".scroll-to-top-btn");
        if (window.pageYOffset > 100){
            topBtn.classList.add("active-top-btn");
            console.log("here")
        }else {
            topBtn.classList.remove("active-top-btn");
        }
    })

    //expandable content of  frequently asked questions
    const  title = document.querySelectorAll(".answer-to-questions");
    title.forEach(title => {
        title.addEventListener("click", () =>{
            title.classList.toggle("active");
        });
    });


    //user profile drop down
    const  userProfile = document.querySelectorAll(".user");
    const userSetting = document.querySelector(".user-setting");
    function showUser(){
        userSetting.classList.toggle("showuser")
     }
     for (var i in userProfile) {
        userProfile[i].onclick= function() {
          showUser();
        };
    }
    //to show company drop down
    const  companyDropDown = document.querySelector("#company-drop-down");
    const companySetting = document.querySelector(".company-drop-down-setting");
    function showCompany(){
        companySetting.classList.toggle("show-company-drop-down")
        companyDropDown.classList.toggle("active-setting")
     }
     companyDropDown.addEventListener("click", showCompany)
    

    //remove event listner when body element is clicked
    const body = document.getElementsByTagName("body");
    function removeEvent(){

    }
}