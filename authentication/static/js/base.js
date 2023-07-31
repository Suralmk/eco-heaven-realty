if (typeof window !== 'undefined') {
  window.addEventListener('scroll', () => {
    //fixed nav bar
    const headerNav = document.querySelector('.nav-container')
    const heroContainer = document.querySelector('.hero-container')
    if (window.scrollY > 0) {
      headerNav.classList.add('sticky')
      heroContainer.classList.add('hero-contain')
    } else {
      headerNav.classList.remove('sticky')
    }

    //scroll to top page
    const topBtn = document.querySelector('.scroll-to-top-btn')
    if (window.pageYOffset > 100) {
      topBtn.classList.add('active-top-btn')
      console.log('here')
    } else {
      topBtn.classList.remove('active-top-btn')
    }
  })

  //expandable content of  frequently asked questions
  const title = document.querySelectorAll('.answer-to-questions')
  title.forEach(title => {
    title.addEventListener('click', () => {
      title.classList.toggle('active')
    })
  })

  //user profile drop down
  const userProfile = document.querySelectorAll('.user')
  const userSetting = document.querySelector('.user-setting')
  function showUser () {
    userSetting.classList.toggle('showuser')
  }
  for (var i in userProfile) {
    userProfile[i].onclick = function () {
      showUser()
    }
  }

  //to show company drop down
  const companyDropDown = document.querySelector('.nav-company-btn')

  const companySetting = document.querySelector('.company-drop-down-setting')
  function showCompany () {
    companySetting.classList.toggle('show-company-drop-down')
    companyDropDown.classList.toggle('active-company-setting')
  }
  companyDropDown.addEventListener('click', showCompany)

  //cateagory drop down menu
  const cateagoryDropDown = document.querySelector('.nav-cateagory-btn')
  const cateagoryDropDownSetting = document.querySelector('.cateagory-drop-down-setting')

  function showCateagory () {
    cateagoryDropDownSetting.classList.toggle("show-catagory-drop-down")
    cateagoryDropDown.classList.toggle("active-catagory-setting")
  }
  cateagoryDropDown.addEventListener('click', showCateagory)

 
 //change passwrd setting from user profile
 const changePassword = document.querySelector("#change-password");
 const changePasswordContainer = document.querySelector(".change-passwprd-contain")
 changePassword.addEventListener("click", showChangePassword)
  function showChangePassword(){
    changePasswordContainer.classList.toggle("change-passwprd-container")
  }
 
  //change username
  const changeUsername = document.querySelector("#change-username");
  const changeUsernameContainer = document.querySelector(".change-username-contain")
  changeUsername.addEventListener("click", showChangePassword)
   function showChangePassword(){
    changeUsernameContainer.classList.toggle("change-username-container")
   }
   
 // Close button
    const closeBtn = document.querySelector(".close-btn")
    closeBtn.addEventListener("click", closeChangePassword)
    function closeChangePassword(){
        changePasswordContainer.classList.remove("change-passwprd-container")
        changeUsernameContainer.classList.remove("change-username-container")
    }
  //remove event listner when body element is clicked
  const body = document.getElementsByTagName('body')
  function removeEvent () {}
}
