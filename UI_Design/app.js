<div class="dropdown">
      <div class="select">
        <span class="selected">MEN</span>
        <div class="caret"></div>
      </div>
      <ul class="menu">
        <li>Shirts</li>
        <li>Suits</li>
        <li>Tees & Polos</li>
      </ul>
    </div>

<div class="dropdown">
      <div class="select">
        <span class="selected">WOMEN</span>
        <div class="caret"></div>
      </div>
      <ul class="menu">
        <li>Tops</li>
        <li>Bottoms</li>
        <li>Dresses & Jumpsuits</li>
        <li>Shoes</li>
        <li>Jewelry</li>
      </ul>
    </div>
<script src="app.js"></script>
//Get all dropdown from document
const dropdowns = document.querySelectorAll('.dropdown');

//Loop through all dropdown elements
dropdowns.forEach(dropdown => {
    //get inner elements from each ropdown
    const select = dropdown.querySelector('.select');
    const caret = dropdown.querySelector('.caret');
    const menu = dropdown.querySelector('.menu');
    const options = dropdown.querySelectorAll('.menu li');
    const selected = dropdown.querySelector('.selected');

    /*
    We are using this method in order to have
    multiple dropdown menus on the page work
    */ 

    //Adding click event to select element
    select.addEventListener('click',() => {
        select.classList.toggle('select-clicked');
        caret.classList.toggle('caret-rotate');
        menu.classList.toggle('menu-open');
    });

    options.forEach(option => {
        option.addEventListener('click', () => {
            selected.innerText = option.innerText;
            select.classList.remove('select-clicked');
            caret.classList.remove('caret-rotate');
            menu.classList.remove('menu-open');

            options.forEach(option => {
                option.classList.remove('active');
            });
            option.classList.add('active');
        });

    });
});

.dropdown {
    min-width: 15em;
    display: inline-block;
    position: relative;
    margin: 2em;
}

.dropdown * {
    box-sizing: border-box;
}

.select{
    background-color: #2a2f3b;
    color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 2px #2a2f3b solid;
    border-radius: .5em;
    padding: 1em;
    cursor: pointer;
    transition: background 0.3s;
}

.select-clicked {
    border: 2px #26489a solid;
    box-shadow: 0 0 0.8em #26489a;
}

.select:hover{
    background: #323741;
}

.caret{
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid #fff;
    transition: 0.3s;
}

.caret-rotate{
    transform: rotate(180deg);
}

.menu{
    list-style: none;
    padding: .2em .5em;
    background: #323741;
    border: 1px #363a43 solid;
    box-shadow: 0 0.5m 1em rgba(0,0,0,0.2);
    border-radius: .5em;
    color: #9fa5b5;
    position: absolute;
    top: 3em;
    left: 50%;
    width: 100%;
    transform: translateX(-50%);
    opacity: 0;
    display: none;
    z-index: 1;
}

.menu li{
    padding: 0.7em 0.5em;
    margin: 0.3em 0;
    border-radius: .5em;
    cursor: pointer;
}

.menu li:hover{
    background: #2a2d35;
} 

.active{
    background: #23242a;
}

.menu-open {
    display: block;
    opacity: 1;
}






.row .col-2{
    border-radius: 5px;
    margin: auto;
    height: 100%;
    padding-left: 10px;
}

.row .col-3{
    border-radius: 5px;
    margin: auto;
    height: 100%;
    width: 50%;
    
}

.col-2 img{
    padding: 10px;
    margin: 5px;
    height: 600px;
    width: 100%;
    background: #f5f5f5;
}