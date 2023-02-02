const createNav = () => {
    let nav = document.querySelector('.navbar');

    nav.innerHTML = `
    <nav class="navbar">
      <div class="nav">
        <a href="index.html"
          ><img
            src="img/final_logo.png"
            class="brand-logo"
            alt=""
        /></a>

        <div class="nav-items">
          <div class="search">
            <input
              type="text"
              class="search-box"
              placeholder="search brand, product"
            />
            <button class="search-btn">search</button>
          </div>
        </div>
      </div>

      <ul class="links-container">
        <li class="link-item">
          <a href="#" class="link">MEN</a>
          <ul class="cat-level2">
            <li><a href="#">shirts</a></li>
          </ul>
        </li>
      </ul>
    </nav>
    `;
};

createNav()