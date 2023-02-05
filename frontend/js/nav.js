

function myQuery() {
  localStorage.setItem("query", document.getElementById("searchid").value);
  window.location.href = "http://localhost:5500/frontend/product-list.html?";
}

const createNav = function () {
  let nav = document.querySelector("#navbar");

  nav.innerHTML = `
    <nav id="navbar">
      <div class="nav">
        <a href="index.html"
          ><img
            src="img/final_logo.png"
            class="brand-logo"
            alt=""
        /></a>

        <div class="nav-items">
        <div class="search">
        <form class = "form-bar">
        <input
        type="text"
        class="search-box"
        id="searchid"
        placeholder="search brand, product"
      />
      <button class="search-btn" type="button" onclick="myQuery()">search</button>
      </form>
          </div>
        </div>
      </div>

      

      <div class="cat">
  <select name="catm" id="catm" onchange="categorycall('men')">
    <option value="" selected disabled hidden>MEN</option>
    <option value="">All</option>
    <option value="New Arrivals">New Arrivals</option>
    <option value="Labels We Love">Labels We Love</option>
    <option value="Tops">Tops</option>
    <option value="Underwear & Lounge">Underwear & Lounge</option>
    <option value="Suiting">Suiting</option>
    <option value="Clearance Men">Clearance Men</option>
    <option value="Express x NBA">Express x NBA</option>
    <option value="Pants">Pants</option>
    <option value="Accessories & Shoes">Accessories & Shoes</option>
    <option value="Outerwear">Outerwear</option>
    <option value="Accessories">Accessories</option> 
  </select>

  <select name="catw" id="catw" onchange="categorycall('men')">
    <option value="" selected disabled hidden>WOMEN</option>
    <option value="">All</option>
    <option value="Clearance  Women">Clearance  Women</option>
    <option value="Tops">Tops</option>
    <option value="Jeans">Jeans</option>
    <option value="Labels We Love">Labels We Love</option>
    <option value="Jewelry">Jewelry</option>
    <option value="Accessories">Accessories</option>
    <option value="Dresses">Dresses</option>
    <option value="Petite Clothing">Petite Clothing</option>
    <option value="New Arrivals">New Arrivals</option>
    <option value="Work">Work</option>
    <option value="Jackets & Coats">Jackets & Coats</option>
    <option value="Bottoms">Bottoms</option>
    <option value="Sweaters & Cardigans">Sweaters & Cardigans</option>
    <option value="Accessories & Shoes">Accessories & Shoes</option>
    <option value="Labels We Love">Labels We Love</option>
  </select>

  <select name="cat1" id="cat1" onchange="categorycall('men')">
    <option value="" selected disabled hidden>EXP</option>
    <option value="">All</option>
  </select>
</div>

      
    </nav>
    `;
};

createNav();

// function passProdDet(prodTitle, prodImg, prodPrice) {
//   return `<div class="product-container" id="product-list-div">
//       <div class="product-card">
//           <div class="product-image">
//             <img src="${prodImg}" class="product-thumb" alt="" />
//           </div>
//           <div class="product-info">
//             <p class="product-title">${prodTitle}</p>
//             <span class="price">$${prodPrice}</span>
//           </div>
//         </div>
//         </div>`;
// }

{
  /* <ul class="links-container">
        <li class="link-item">
          <a href="#" class="link">MEN</a>
          <ul class="cat-level2">
            <li><a href="#">shirts</a></li>
          </ul>
        </li>

        <li class="link-item">
          <a href="#" class="link">MEN</a>
          <ul class="cat-level2">
            <li><a href="#">shirts</a></li>
          </ul>
        </li>
      </ul> */
}
