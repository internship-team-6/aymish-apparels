const searchQuery = function () {
  const q = document.getElementById("searchid").value;
  location.href = "./search-product-list.html?" + new URLSearchParams({ q: q });
};

const categorySelect = function (catlevel1Id, catlevel2NameObj) {
  const catlevel2Name = catlevel2NameObj.value;
  location.href =
    "./category-product-list.html?" +
    new URLSearchParams({
      catlevel1Id: catlevel1Id,
      catlevel2Name: catlevel2Name,
    });
};

const createNav = function () {
  let nav = document.querySelector("#navbar");
  nav.innerHTML = `
    <div class="nav">
      <a href="index.html"><img src="img/final_logo.png" class="brand-logo" alt="" /></a>
      <div class="nav-items">
        <div class="search">
          <form class="form-bar">
            <input type="text" class="search-box" id="searchid" placeholder="search brand, product" />
            <button class="search-btn" type="button" onclick="searchQuery()">search</button>
          </form>
        </div>
      </div>
    </div>
    <div class="cat" id="cat-level-1">
    </div>
    `;
  fetch("http://localhost:5000/navbar", {
    method: "GET",
    mode: "cors",
    headers: {
      "Access-Control-Allow-Origin": "*",
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const categories_arr = data;
      let cat_level_1 = document.getElementById("cat-level-1");
      for (let i = 0; i < categories_arr.length; i++) {
        let catlevel1Name = categories_arr[i]["name"];
        let catlevel1Id = categories_arr[i]["id"];
        cat_level_1.innerHTML += `
          <select name="${catlevel1Name}" id="${catlevel1Id}" onchange="categorySelect(${catlevel1Id}, this)">
            <option value="" selected disabled hidden>${catlevel1Name}</option>
            <option value="">All</option>
          </select>
        `;
        fetch(
          "http://localhost:5000/dropdown?" +
            new URLSearchParams({ catlevel1Id: catlevel1Id }),
          {
            method: "GET",
            mode: "cors",
            headers: {
              "Access-Control-Allow-Origin": "*",
              Accept: "application/json",
              "Content-Type": "application/json",
            },
          }
        )
          .then((response) => response.json())
          .then((data) => {
            cat_level_1_id_element = document.getElementById(catlevel1Id);
            for (let i = 0; i < data.length; i++) {
              let val = data[i]["name"];
              cat_level_1_id_element.innerHTML += `
                <option id="${val}" value="${val}">
                  ${val}
                </option>
              `;
            }
          });
      }
    });
};

onload = createNav();

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
